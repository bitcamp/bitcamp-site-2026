<template>
    <div class="gradient">
        <img src="@/assets/img/images/mountains_new.svg" class="mountains" />
        <img src="@/assets/img/images/basic marshie (arms down).svg" class="marshie1" />
        <img src="@/assets/img/images/basic marshie (arms up).svg" class="marshie2" />
        <img src="@/assets/img/images/ufo.svg" class="ufo" />
        <img src="@/assets/img/images/ufo rays.svg" class="ufo-rays" />
        <img src="@/assets/img/images/text border.svg" class="text-border" />
        <img src="@/assets/img/images/title_and_tagline.svg" class="name" />
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
    height: 100vh;
    width: 100vw;
    overflow: hidden;
    background-size: cover;
    background-image: url("../assets/img/images/landing_gradient.webp");
    margin-bottom: 150px; /* can be removed, only so that tracks doesn't overlap */
}


.mountains {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    z-index: 3;
}

.ufo {
    position: absolute;
    top: 23%;
    left: 22%;
    z-index: 2;
    scale: 1.2;
}

.ufo-rays {
    position: absolute;
    top: 37%;
    left: 25%;
    z-index: 1;
    scale: 1.2;
}

.marshie1 {
    position: absolute;
    top: 50%;
    left: 28%;
    z-index: 2;
    scale: 1.2;
}

.marshie2 {
    position: absolute;
    top: 67%;
    left: 31%;
    z-index: 2;
    scale: 1.2;
}

.text-border {
    position: absolute;
    left: 36%;
    top: 10%;
    scale: 1.2;
}

.name {
    position: absolute;
    left: 50%;
    top: 35%;
    scale: 1.2;
}

.content-wrapper {
    position: absolute;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    color: white;
    z-index: 3;
    right: 20%;
    top: 55%;
    width: 50%;
    scale: 0.7;
}

.register-button {
    background-color: #FF6F3F;
    border: solid;
    border-color: #E54D1A;
    border-width: 0.5rem;
    border-radius: 20rem;
    color: white;
    font-family: Aleo, sans-serif;
    font-size: 4rem;
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
        background-color: #C4B500;
        padding-bottom: calc(339% - 239vw);
    }
}

@media (max-width: 500px) {
    .content-wrapper {
        width: 100%;
        margin-top: calc(298% - 232.5vw);
    }

    .gradient {
        background-color: #C4B500;
        padding-bottom: calc(341% - 240vw);
    }
}
</style>