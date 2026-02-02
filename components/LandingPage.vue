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
    background: linear-gradient(180deg, #010B18, #0D2539);
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
    width: 100%;
        left: 0;
        right: 0;
        top:0vw; 
        display: flex;
        justify-content: center;

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

@media (max-width: 796px) {
    .register-button {
        font-size: clamp(2rem, 7.5vw, 8rem);
        ;
        padding: calc(2.8vw + 1rem) calc(7.8vw + 2rem);
        border-radius: 4.5rem;
        background-color: #F2C042;
        letter-spacing: 0.4rem;
    }

    .content-wrapper {
        width: 100%;
        margin-top: calc(300% - 232.5vw);
    }

    .button-wrapper {
        padding: 0;
        width: auto;
    }
     .gradient {
        background:linear-gradient(160deg, #010B18 0%, #0D2539 100%);
        background-size: 100% 338px, cover;
        background-position: center 40%;
        padding-bottom: calc(339% - 239vw);
    }

}



@media (max-width: 500px) {
    .content-wrapper {
        width: 100%;
        margin-top: calc(298% - 232.5vw);
    }
   
    .gradient {
        background:linear-gradient(160deg, #010B18 0%, #0D2539 100%);
        background-size: 100% 338px, cover;
        background-position: center 40%;
        padding-bottom: calc(341% - 240vw);
    }
}

</style>