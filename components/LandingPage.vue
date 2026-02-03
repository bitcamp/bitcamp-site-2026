<template>
    <div class="gradient">
        <img src="../assets/img/images/flattened_landing.webp" class="dino-background" alt="landing image" />
        
            <div class="button-wrapper">
                <a target="_blank" href="https://register.bit.camp" class="register-button">REGISTER</a>
            </div>
            <div class="message-wrapper">
            <ExplorationMessage />
            </div>      
        </div>
    
</template>
<script lang="ts">
import ExplorationMessage from '~/components/ExplorationMessage.vue';
export default {
    name: 'LandingPage',
    components: {
        ExplorationMessage,
    },
};
</script>


<style scoped>
.gradient {
    position: relative;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 135vw;
    height: auto;
    overflow: hidden;
    background: linear-gradient(
    180deg,
    #010B18 0%,
    #201F3A 50%,
    #0D2539 100%
  );
  
    background-size: cover;
}
.dino-background {
    position: absolute;
    display: flex;
    flex-direction: column;
    top: 0;
    left: 0;
    width: 100%;
    height: auto;
    z-index: 0;
    object-fit: cover;
}
.message-wrapper {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 0; 
}
.button-wrapper {
    width: 100%;
    padding: 0 ;
    top:30vw;
    right:auto;
     position: absolute;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    color: white;
    z-index: 1;
    right:0;
    top: 50vw;
    width: 48%;
}
.register-button {
    background-color: #FFB353;
    border: none;
    border-radius: 2.5rem;
    color: #4F2525;
    font-family: Aleo, sans-serif;
    font-size: 3.4rem;
    font-weight: bold;
    padding: 1.7rem 4.8rem;
    letter-spacing: 0.2rem;
    margin-bottom: 10%;
    cursor: pointer;
    transition: transform 0.2s, box-shadow 0.2s;
}
.register-button:hover {
    transform: translateY(-4px);
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
}

<style scoped>
<style scoped>
/* ... keep your desktop styles exactly as they are ... */

@media (max-width: 796px) {
    .register-button {
        font-size: clamp(2rem, 7.5vw, 8rem);
        padding: calc(2.8vw + 1rem) calc(7.8vw + 2rem);
        border-radius: 4.5rem;
        background-color: #F2C042;
        letter-spacing: 0.4rem;
        text-decoration: none;
        display: inline-block;
        text-align: center;
    }
    
    .button-wrapper {
        position: absolute;
        top: 35vw; /* Keep button on the dino image */
        left: 50%;
        transform: translateX(-50%);
        width: 90%;
        max-width: 400px;
        display: flex;
        justify-content: center;
        z-index: 2;
    }
    
    .gradient {
        background: transparent;
        min-height: 100vh;
        padding-bottom: 0;
        flex-direction: column;
        justify-content: flex-start;
        position: relative;
        overflow: visible;
        display: block; /* Changed from flex */
    }
    
    /* CRITICAL CHANGES HERE */
    .message-wrapper {
        position: relative; /* Changed from absolute */
        top: auto; /* Remove top positioning */
        left: 0;
        width: 100%;
        height: auto;
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 1;
        margin-top: 80vw; /* This positions it BELOW the dino image */
    }

    .dino-background {
        display: flex;
        position: absolute; /* Keep as absolute */
        top: 0;
        left: 0;
        width: 100%;
        height: auto;
        z-index: 0;
    }
}

@media (max-width: 500px) {
    .button-wrapper {
        position: absolute;
        top: 30vw;
        left: 50%;
        transform: translateX(-50%);
        width: 90%;
        max-width: 350px;
        display: flex;
        justify-content: center;
        z-index: 2;
    }
    
    .gradient {
        background: transparent;
        min-height: 100vh;
        padding-bottom: 0;
        flex-direction: column;
        justify-content: flex-start;
        position: relative;
        overflow: visible;
        display: block; /* Changed from flex */
    }
    
    /* CRITICAL CHANGES HERE */
    .message-wrapper {
        position: relative; /* Changed from absolute */
        top: auto; /* Remove top positioning */
        left: 0;
        width: 100%;
        height: auto;
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 1;
        margin-top: 70vw; /* This positions it BELOW the dino image */
    }

    .dino-background {
        display: flex;
        position: absolute; /* Keep as absolute */
        top: 0;
        left: 0;
        width: 100%;
        height: auto;
        z-index: 0;
    }
}
</style>