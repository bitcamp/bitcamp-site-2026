<template>
  <div class="bitbot_wrapper">
    <!-- Chat icon (always visible) -->
    <AnimatePresence>
      <motion.button
        v-if="!isOpen"
        class="chat_icon"
        @click="openChat"
        alt="Open BitBot chat"
        :initial="{ opacity: 0, scale: 0 }"
        :animate="{ opacity: 1, scale: 1 }"
        :exit="{ opacity: 0, scale: 0 }"
        :transition="{ duration: 0.2, delay: 0.1 }"
      >
        <img src="/bitcamp-brand/logos/bitbot_button.svg" alt="BitBot Icon" />
      </motion.button>
    </AnimatePresence>

    <!-- Chat panel -->
    <AnimatePresence>
      <motion.div
        v-if="isOpen"
        class="chat_panel"
        role="dialog"
        alt="BitBot chat window"
        :initial="{ opacity: 0, scale: 0.8 }"
        :animate="{ opacity: 1, scale: 1 }"
        :exit="{ opacity: 0, scale: 0.8 }"
        :transition="{ duration: 0.1 }"
      >
        <header class="chat_header">
          <div class="header_left">
            <img
              class="bot_pfp"
              src="/bitcamp-brand/logos/bitbot_pfp.svg"
              alt="BitBot"
            />
            <div class="header_text">
              <div class="title">BitBot</div>
              <div class="subtitle">Ask me anything Bitcamp related!</div>
            </div>
          </div>

          <motion.button
            class="close_button"
            @click="closeChat"
            alt="Close chat"
          >
            ✕
          </motion.button>
        </header>

        <div class="messages" ref="messagesRef">
          <div v-for="(m, idx) in messages" :key="idx" class="message_row">
            <!-- Bot message -->
            <div v-if="m.role === 'bot'" class="message_left">
              <img
                class="msg_bot_pfp"
                src="/bitcamp-brand/logos/bitbot_pfp.svg"
                alt="BitBot Profile Picture"
              />
              <div class="message_with_time">
                <div v-if="m.typing" class="typing">
                  <div class="dots">
                    <span></span><span></span><span></span>
                  </div>
                </div>
                <div v-else>
                  <div class="message bot">{{ m.text }}</div>
                  <div class="message_time bot">{{ m.time }}</div>
                </div>
              </div>
            </div>

            <!-- User message -->
            <div v-else class="message_right">
              <img
                class="msg_usr_pfp"
                src="/bitcamp-brand/logos/bb_user_pfp.svg"
                alt="User Profile Picture"
              />
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
            <button
              type="submit"
              class="send_button"
              :class="{ active: draft.trim().length > 0 }"
              alt="Send button"
            >
              <img
                src="/bitcamp-brand/logos/send-button.png"
                alt="Airplane silhouette"
              />
            </button>
          </form>
        </div>
      </motion.div>
    </AnimatePresence>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onBeforeUnmount, nextTick } from "vue";
import { AnimatePresence, motion } from "motion-v";

type Msg = {
  role: "bot" | "user";
  text: string;
  time: string;
  typing?: boolean;
};

const getCurrentTime = (): string => {
  const now = new Date();
  let hours = now.getHours();
  const minutes = now.getMinutes().toString().padStart(2, "0");
  const ampm = hours >= 12 ? "PM" : "AM";
  hours = hours % 12;
  if (hours === 0) hours = 12;
  return `${hours}:${minutes} ${ampm}`;
};

const isOpen = ref(false);
const messagesRef = ref<HTMLElement | null>(null);
const messages = ref<Msg[]>([
  {
    role: "bot",
    text: "Hey there! 👋 I’m BitBot! Feel free to ask me anything about Bitcamp!",
    time: getCurrentTime(),
  },
]);
const draft = ref("");

const openChat = async () => {
  isOpen.value = true;
  await nextTick();
  scrollMessagesToBottom();
};

const closeChat = () => {
  isOpen.value = false;
};

const scrollMessagesToBottom = () => {
  const el = messagesRef.value;
  if (el) el.scrollTop = el.scrollHeight;
};

const autoResizeTextarea = (e: Event) => {
  const el = e.target as HTMLTextAreaElement;
  el.style.height = "auto";
  el.style.height = Math.min(el.scrollHeight, 200) + "px";
};

const sendMessage = async () => {
  const text = draft.value.trim();
  if (!text) return;
  messages.value.push({ role: "user", text, time: getCurrentTime() });
  draft.value = "";
  await nextTick();
  const textarea = document.querySelector(
    ".input_textarea"
  ) as HTMLTextAreaElement;
  if (textarea) textarea.style.height = "auto";
  scrollMessagesToBottom();

  // show typing indicator
  const typingMsg: Msg = {
    role: "bot",
    text: "",
    time: getCurrentTime(),
    typing: true,
  };
  messages.value.push(typingMsg);
  await nextTick();
  scrollMessagesToBottom();

  //random bot reply, replace w bot later
  setTimeout(async () => {
    // remove typing indicator
    const idx = messages.value.findIndex((m) => m.typing === true);
    if (idx !== -1) messages.value.splice(idx, 1);

    const response = await fetch("FUNCTION_URL", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ text })
    });

    messages.value.push({
      role: "bot",
      text: JSON.stringify(response['body']),
      time: getCurrentTime(),
    });
    await nextTick();
    scrollMessagesToBottom();
  }, 300);
};

const onInputKeydown = (e: KeyboardEvent) => {
  if (e.key === "Enter" && !e.shiftKey) {
    e.preventDefault();
    sendMessage();
  }
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Inter&display=swap");

@keyframes blink {
  0%,
  60%,
  100% {
    transform: translateY(0);
    opacity: 0.3;
  }
  30% {
    transform: translateY(-10px);
    opacity: 1;
  }
}

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
.chat_icon img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 50%;
}

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
  background: linear-gradient(90deg, #ad3928 0%, #ff6f3f 100%);
}

.header_left {
  display: flex;
  align-items: center;
  gap: 1.2vw;
}
.bot_pfp {
  width: 3vw;
  height: 3vw;
  object-fit: cover;
  border-radius: 50%;
  background-color: #f3f3f5;
}
.header_text .title {
  font-family: "aleo";
  font-size: 1.5vmax;
  font-weight: 700;
  letter-spacing: 0%;
}
.header_text .subtitle {
  font-family: "inter";
  font-weight: 400;
  font-size: 1vmax;
  letter-spacing: 0%;
  opacity: 0.75;
} /*THIS FONT IS NOT UPLOADED */

.close_button {
  background: rgba(255, 255, 255, 0);
  color: white;
  border: none;
  padding: 0.6vmax 0.6vmax;
  border-radius: 8px;
  cursor: pointer;
  font-size: 1.6vmax;
}
.close_button:focus {
  outline: 0.2vmax solid rgba(255, 255, 255, 0.25);
}

.msg_bot_pfp {
  width: 2.75vmax;
  height: 2.75vmax;
  object-fit: cover;
  border: 0px;
  border-radius: 50%;
  background: #ff6f3f;
}
.msg_usr_pfp {
  width: 2.75vmax;
  height: 2.75vmax;
  object-fit: cover;
  border: 0px;
  border-radius: 50%;
  background: #6b7282;
}

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
  font-family: "avenir";
  scrollbar-width: thin;
}

.messages::-webkit-scrollbar {
  width: 6px;
}

.messages::-webkit-scrollbar-thumb {
  background: rgba(0, 0, 0, 0.2);
  border-radius: 3px;
}

.message {
  max-width: 20.7vw;
  padding: 1vh 1vw;
  border-radius: 10px;
  line-height: 1.3;
  word-break: break-word;
  box-sizing: border-box;
  font-family: "avenir";
  white-space: pre-wrap;
  height: auto;
  overflow-wrap: anywhere;
}
.message.bot {
  background: #f3f3f5;
  align-self: start;
}
.message.user {
  background: #ff6f3f;
  align-self: end;
  color: white;
}

.panel_footer {
  padding: 1.8vh 1.4vw;
  border-top: 1px solid rgba(0, 0, 0, 0.04);
  background: #fff;
}

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
  background: #f3f3f5;
  border-radius: 15px;
  border: 1px solid rgba(0, 0, 0, 0.08);
  font-size: 1vmax;
  font-family: "Avenir";
  resize: none;
  box-sizing: border-box;
  align-content: center;
}

.input_textarea:focus {
  outline: none;
  border-color: #ff6f3f;
  box-shadow: 0 0 0 2px rgba(255, 111, 63, 0.5);
}

.send_button {
  background: #6b7282;
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
  background: #ff6f3f;
}
.send_button:active {
  transform: translateY(1px);
}

.message_row {
  display: flex;
  flex-direction: column;
  width: 100%;
}

.message_left,
.message_right {
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
  gap: 0.2vmax;
}

.message_time {
  font-size: 0.75vmax;
  font-family: "Avenir";
  font-weight: 500;
}

.message_time.bot {
  text-align: left;
  color: rgba(0, 0, 0, 0.5);
  padding-left: 0.5vmax;
  margin-top: 0.2vmax;
}

.message_time.user {
  text-align: right;
  color: rgba(0, 0, 0, 0.5);
  padding-right: 0.5vmax;
  margin-top: 0.2vmax;
}

.typing {
  display: flex;
  align-items: center;
  min-height: 1em;
  padding: 1vh 1vw;
  background: #f3f3f5;
  border-radius: 10px;
  max-width: 20.7vw;
}

.typing .dots {
  display: flex;
  align-items: center;
  gap: 0.4vmax;
}

.typing .dots span {
  width: 0.6rem;
  height: 0.6rem;
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

@media screen and (max-width: 1199px) {
  .chat_panel {
    width: 35vw;
    height: 48vh;
  }

  .header_text .title {
    font-size: 2vw;
  }

  .messages {
    padding: 1vw;
    gap: 1vw;
    font-size: 1.1vw;
  }

  .message {
    max-width: 50vw;
    padding: 1vw 1vw;
    font-size: 1.25vw;
  }

  .message_time {
    font-size: 0.9vw;
  }

  .input_textarea {
    width: 100%;
    font-size: 1.6vw;
    overflow-y: hidden;
  }
}

@media screen and (max-width: 990px) {
  .chat_panel {
    width: 40vw;
    height: 48vh;
  }

  .header_text .title {
    font-size: 2vw;
  }

  .messages {
    padding: 1.5vw;
    gap: 1vw;
    font-size: 1.6vw;
  }

  .message {
    max-width: 50vw;
    padding: 1vw 1vw;
    font-size: 1.7vw;
  }

  .message_time {
    font-size: 0.9vw;
  }

  .input_textarea {
    width: 100%;
    font-size: 1.2vw;
    overflow-y: hidden;
  }
}

@media screen and (max-width: 796px) {
  .chat_panel {
    width: 45vw;
    height: 48vh;
  }

  .header_text .title {
    font-size: 2vw;
  }

  .messages {
    padding: 2vw;
    gap: 1vw;
    font-size: 1.6vw;
  }

  .message {
    max-width: 50vw;
    padding: 1vw 1vw;
    font-size: 1.8vw;
  }

  .message_time {
    font-size: 1.3vw;
  }

  .input_textarea {
    width: 100%;
    font-size: 1.6vw;
    overflow-y: hidden;
  }
}

/*mobile*/
@media screen and (max-width: 599.98px) {
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
    background: rgba(255, 255, 255, 0);
    color: white;
    border: none;
    padding: 2.5vw 2.5vw;
    min-width: 44px;
    min-height: 44px;
    border-radius: 8px;
    cursor: pointer;
    font-size: 4.5vw;
  }
  .close_button:focus {
    outline: 0.2vw solid rgba(255, 255, 255, 0.25);
  }

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
