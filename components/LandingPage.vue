<template>
    <div class="gradient">
        <img src="../assets/img/images/better_landing.webp" class="background" alt="landing image" />
        <div class="content-wrapper">
            <div class="button-wrapper">
                <a target="_blank" href="https://register.bit.camp" class="register-button">REGISTER</a>
            </div>
        </div>
    </div>
</template>

<script lang="ts">

export default {
    name: 'LandingPage',
    components: {
    },
};
</script>

<style scoped>

.gradient {
    position: relative;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 75vw;
    height: auto;
    overflow: hidden;
    background-color: #0D2539;
    background-size: cover;
    width: 100%;
    aspect-ratio: 16 / 9;
}

.background {
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

.content-wrapper {
    position: absolute;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    color: white;
    z-index: 1;

    position: absolute;
    top: 51%;
    right: 38%;
    transform: translateY(-60%);
    width: auto;
}

.button-wrapper {
    width: 100%;
    padding: 0 0 3vw 3.2vw;
}

.register-button {
    background-color: #FF6F3F;
    border: none;
    border-radius: 5rem;
    border-style: solid;
    border-color: #E54D1A;
    color: white;
    font-family: Aleo, sans-serif;
    font-weight: bold;
    letter-spacing: 0.2rem;
    margin-bottom: 10%;
    cursor: pointer;
    transition: transform 0.2s, box-shadow 0.2s;

    font-size: clamp(1.3rem, 1.8vw, 2.8rem);
    padding: clamp(0.4rem, 0.8vw, 1.1rem)
             clamp(1.3rem, 2.5vw, 3.5rem);
    border-width: clamp(0.2rem, 0.25vw, 0.4rem);
}

@media (max-width: 402px) {
    .background {
        content: url("../assets/img/images/better_mobile.webp");
    }
    .register-button {
        border-radius: 5rem;
        letter-spacing: 0.25rem;
        font-size: clamp(1.1rem, 4vw, 1.9rem);
        padding: clamp(0.6rem, 3vw, 1.2rem)
             clamp(1.6rem, 6vw, 1.7rem);
        border-width: clamp(0.18rem, 0.4vw, 0.2rem);
    }

    .content-wrapper {
        top: 21%;
        right: 54%;
        transform: translateY(-60%);
    }

    .gradient {
        background-color: #0D2539;
        padding-bottom: calc(200%);
        aspect-ratio: 9 / 16;
    }
}
</style>