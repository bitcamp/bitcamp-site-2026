<template>
    <div class="bitbot_wrapper">
        <!-- Chat icon (always visible) -->
        <button
            class="chat_icon"
            v-if="!isOpen"
            @click="openChat"
            alt="Open BitBot chat"
        >
            <img src="/bitcamp-brand/logos/bitbot_button.svg" alt="BitBot Icon" />
        </button>

        

        <!-- Chat panel -->
        <div v-else class="chat_panel" role="dialog" alt="BitBot chat window">
            <header class="chat_header">
                <div class="header_left">
                    <img class="bot_pfp" src="/bitcamp-brand/logos/bitbot_pfp.svg" alt="BitBot" />
                    <div class="header_text">
                        <div class="title">BitBot</div>
                        <div class="subtitle">Ask me anything Bitcamp related!</div>
                    </div>
                </div>

                <button class="close_button" @click="closeChat" alt="Close chat">✕</button>
            </header>

            <div class="messages" ref="messagesRef">
                <div
                    v-for="(m, idx) in messages"
                    :key="idx"
                    class="message_row"
                >

                    <!-- Bot message -->
                    <div v-if="m.role === 'bot'" class="message_left">
                        <img class="msg_bot_pfp" src="/bitcamp-brand/logos/bitbot_pfp.svg" alt="BitBot Profile Picture" />
                        <div class="message_with_time">
                            <div v-if="m.typing" class="typing">
                                <div class="dots"><span></span><span></span><span></span></div>
                            </div>
                            <div v-else>
                                <div class="message bot">{{ m.text }}</div>
                                <div class="message_time bot">{{ m.time }}</div>
                            </div>
                        </div>
                    </div>

                    <!-- User message -->
                    <div v-else class="message_right">
                        <img class="msg_usr_pfp" src="/bitcamp-brand/logos/bb_user_pfp.svg" alt="User Profile Picture" />
                        <div class="message_with_time">
                            <div class="message user">{{ m.text }}</div>
                            <div class="message_time user">{{ m.time }}</div>
                       </div>
                    </div>
                </div>
            </div>

            <!-- Footer with input -->
            <div class="panel_footer">
                <form class="input_form" @submit.prevent="sendMessage">
                    <textarea
                        v-model="draft"
                        class="input_textarea"
                        :class="{ filled: draft.trim().length > 0 }"
                        placeholder="Type your message"
                        @keydown="onInputKeydown"
                        @input="autoResizeTextarea"
                        rows="1"
                        alt="Type your message"
                    ></textarea>
                    <button type="submit" class="send_button" :class="{ active: draft.trim().length > 0 }" alt="Send button">
                        <img src="/bitcamp-brand/logos/send-button.png" alt="Airplane silhouette" />
                    </button>
                </form>
            </div>
        </div>
    </div>
</template>


<script setup lang="ts">
import { ref, onMounted, onBeforeUnmount, nextTick } from 'vue'

type Msg = { role: 'bot' | 'user'; text: string; time: string; typing?: boolean }

const getCurrentTime = (): string => {
    const now = new Date()
    let hours = now.getHours()
    const minutes = now.getMinutes().toString().padStart(2, '0')
    const ampm = hours >= 12 ? 'PM' : 'AM'
    hours = hours % 12
    if (hours === 0) hours = 12
    return `${hours}:${minutes} ${ampm}` 
}

const isOpen = ref(false)
const messagesRef = ref<HTMLElement | null>(null)
const messages = ref<Msg[]>([
    { role: 'bot', text: "Hey there! 👋 I’m BitBot! Feel free to ask me anything about Bitcamp!", time: getCurrentTime() },
])
const draft = ref('')

const openChat = async () => {
    isOpen.value = true
    await nextTick()
    scrollMessagesToBottom()
}
const closeChat = () => {
    isOpen.value = false
}

const scrollMessagesToBottom = () => {
    const el = messagesRef.value
    if (el) el.scrollTop = el.scrollHeight
}

const autoResizeTextarea = (e: Event) => {
    const el = e.target as HTMLTextAreaElement
    el.style.height = 'auto' 
    el.style.height = Math.min(el.scrollHeight, 200) + 'px'
}

const sendMessage = async () => {
    const text = draft.value.trim()
    if (!text) return
    messages.value.push({ role: 'user', text, time: getCurrentTime() })
    draft.value = ''
    await nextTick()
    scrollMessagesToBottom()

    // show typing indicator
    const typingMsg: Msg = { role: 'bot', text: '', time: getCurrentTime(), typing: true }
    messages.value.push(typingMsg)
    await nextTick()
    scrollMessagesToBottom()

    //random bot reply, replace w bot later
    setTimeout(async () => {
        // remove typing indicator
        const idx = messages.value.findIndex(m => m.typing === true)
        if (idx !== -1) messages.value.splice(idx, 1)

        messages.value.push({ role: 'bot', text: `Got it — you said: "${text}"`, time: getCurrentTime() })
        await nextTick()
        scrollMessagesToBottom()
    }, 300)
}

const onInputKeydown = (e: KeyboardEvent) => {
    if (e.key === 'Enter') {
        e.preventDefault()
        sendMessage()
    }
}

</script>

<style scoped>

@import url('https://fonts.googleapis.com/css2?family=Inter&display=swap');

.bitbot_wrapper {
    position: fixed;
    right: 35px;
    bottom: 30px;
    z-index: 9999;
    font-family: inherit;
}

.chat_icon {
    width: 4.75vmax;
    height: 4.75vmax;
    padding: 0;
    border: none;
    background: transparent;
    box-shadow: none;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
}
.chat_icon img { width: 100%; height: 100%; object-fit: cover; border-radius: 50% }

.chat_panel {
    width: 28vw;
    height: 64vh;
    display: flex;
    flex-direction: column;
    background: #fff;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 12px 40px rgba(22, 31, 41, 0.16);
    font-size: 1.1vmax;
}

.chat_header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 1.2vw 1.6vh;
    background: linear-gradient(90deg, #AD3928 0%, #FF6F3F 100%);
}

.header_left { display:flex; align-items:center; gap:1.2vw }
.bot_pfp { width: 3vw; height:3vw; object-fit:cover; border-radius: 50%; background-color: #F3F3F5}
.header_text .title { font-family: 'aleo'; font-size: 1.5vmax; font-weight: 700; letter-spacing: 0% }
.header_text .subtitle { font-family:'inter'; font-weight: 400; font-size: 1vmax; letter-spacing: 0%; opacity:0.75 } /*THIS FONT IS NOT UPLOADED */

.close_button {
    background: rgba(255,255,255,0.0);
    color: white;
    border: none;
    padding: .6vmax .6vmax;
    border-radius: 8px;
    cursor: pointer;
    font-size: 1.6vmax;
}
.close_button:focus { outline: .2vmax solid rgba(255,255,255,0.25) }

.msg_bot_pfp { width:2.75vmax; height:2.75vmax; object-fit:cover; border:0px; border-radius: 50%; background: #ff6f3f }
.msg_usr_pfp { width:2.75vmax; height:2.75vmax; object-fit:cover; border:0px; border-radius: 50%; background: #6B7282 }

.messages {
    padding: 1.6vmax;
    background: #ffffff 100%;
    flex: 1 1 auto;
    overflow-y: auto;
    overflow-x: hidden;
    display: flex;
    flex-direction: column;
    gap: 1.2vmax;
    color: rgba(0, 0, 0, 0.75);
    max-width: 100%;
    font-family: 'avenir';
}
.message {
    max-width: 20.7vw;
    padding: 1vh 1vw;
    border-radius: 10px;
    line-height: 1.3;
    word-break: break-word;
    overflow-wrap: break-word;
    box-sizing: border-box;
    font-family: 'avenir';
    white-space: pre-wrap; 
    height: auto;  
}
.message.bot { background: #F3F3F5; align-self: start }
.message.user { background: #FF6F3F; align-self: end; color: white}

.panel_footer { padding: 1.8vh 1.4vw; border-top: 1px solid rgba(0,0,0,0.04); background: #fff }

.input_form {
    width: 100%;
    display: flex;
    gap: 1.5vw;
    align-items: flex-end;
}

.input_textarea {
    flex: 1 1 auto;
    min-height: 5vh;
    max-height: 20vh;
    padding: 1.2vh 1.2vw;
    background: #F3F3F5;
    border-radius: 15px;
    border: 1px solid rgba(0,0,0,0.08);
    font-size: 1vmax;
    font-family: 'Avenir';
    resize: none;
    box-sizing: border-box;
    align-content: center;
}

.input_textarea:focus {
    outline: none;
    border-color: #FF6F3F;
    box-shadow: 0 0 0 2px rgba(255,111,63,0.5);
}

.send_button {
    background: #6B7282;
    color: #fff;
    border: none;
    padding: 1vw 1vh;
    border-radius: 15px;
    cursor: pointer;
    font-weight: 600;
    height: 5vh;
    width: 5vh;
    align-self: center;
    display: flex;
    align-items: center;
    justify-content: center;
}

.send_button.active {
    background: #FF6F3F;
}
.send_button:active { transform: translateY(1px) }
.message_text { white-space: pre-wrap }

.message_row {
    display: flex;
    flex-direction: column;
    width: 100%;
}

.message_left, .message_right {
    display: flex;
    gap: 1.2vmax;
}

.message_left {
    flex-direction: row;
    align-items: flex-start;
}

.message_right {
    flex-direction: row-reverse;
    align-items: flex-start;
}

.message_with_time {
    display: flex;
    flex-direction: column;
    gap: .2vmax;
}

.message_time {
    font-size: .75vmax;
    font-family: 'Avenir';
    font-weight: 500;
}

.message_time.bot { 
    text-align: left; 
    color: rgba(0,0,0,0.5); 
    padding-left: .5vmax;
    margin-top: .2vmax;
}

.message_time.user { 
    text-align: right; 
    color: rgba(0,0,0,0.5); 
    padding-right: .5vmax;
    margin-top: .2vmax;
}

.typing .dots {
  display: flex;
  align-items: center;
  gap: .4vmax;
}

.typing .dots span {
  width: .6rem;
  height: .6rem;
  background-color: #333;
  border-radius: 50%;
  display: inline-block;
  animation: blink 1.4s infinite both;
}

.typing .dots span:nth-child(2) {
  animation-delay: 0.2s;
}

.typing .dots span:nth-child(3) {
  animation-delay: 0.4s;
}


/*mobile*/
@media (max-width: 600px) {
    .bitbot_wrapper {
        right: 15px;
        bottom: 15px;
        position: fixed;
        margin: 0;
        z-index: 999999 !important;
    }

    .chat_panel {
        width: 100vw;
        height: 100dvh;
        max-width: none;
        max-height: none;
        border-radius: 0;
        position: fixed;
        top: 0;
        left: 0;
        font-size: 4vw;
    }

    .chat_header {
        padding: 4vw;
    }

    .bot_pfp {
        width: 10vw;
        height: 10vw;
    }

    .header_left {
        gap: 3vw;
    }

    .header_text .title {
        font-size: 5vw;
    }

    .header_text .subtitle {
        font-size: 3.5vw;
    }

    .messages {
        padding: 4vw;
        gap: 3vw;
        font-size: 3.6vw;
        flex: 1 1 0;
    }

    .close_button {
        background: rgba(255,255,255,0.0);
        color: white;
        border: none;
        padding: 1.6vw 1.6vw;
        border-radius: 8px;
        cursor: pointer;
        font-size: 4.5vw;
    }
    .close_button:focus { outline: .2vw solid rgba(255,255,255,0.25) }

    .message {
        max-width: 80vw;
        padding: 3vw 4vw;
        font-size: 3.8vw;
    }

    .msg_bot_pfp,
    .msg_usr_pfp {
        width: 10vw;
        height: 10vw;
    }

    .message_time {
        font-size: 3vw;
    }

    .panel_footer {
        padding: 4vw;
    }

    .input_form {
        width: 100%;
        gap: 3vw;
        align-items: flex-end;
    }

    .input_textarea {
        width: 100%;
        font-size: 4vw;
        padding: 3vw 4vw;
        min-height: 10vw;
        max-height: 50vw;
        overflow-y: hidden;
    }

    .chat_icon {
        width: 12vw;
        height: 12vw;
    }
}

</style>