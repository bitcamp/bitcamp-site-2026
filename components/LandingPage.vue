<template>
    <div class="gradient">
        <img src="@/assets/img/images/mountains_new.svg" class="mountains" />
        <img src="@/assets/img/images/basic marshie (arms down).svg" class="marshie1" />
        <img src="@/assets/img/images/basic marshie (arms up).svg" class="marshie2" />
        <div class="ufo-group">
            <img src="@/assets/img/images/ufo.svg" class="ufo" />
            <img src="@/assets/img/images/ufo rays.svg" class="ufo-rays" />
        </div>
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
    top: 23vh;
    left: 22vw;
    z-index: 2;
    scale: 1.2;
}

.ufo-rays {
    position: absolute;
    top: 37vh;
    left: 25vw;
    z-index: 1;
    scale: 1.2;
}

.marshie1 {
    position: absolute;
    top: 50vh;
    left: 28vw;
    z-index: 2;
    scale: 1.2;
}

.marshie2 {
    position: absolute;
    top: 67vh;
    left: 31vw;
    z-index: 2;
    scale: 1.2;
}

.text-border {
    position: absolute;
    left: 36vw;
    top: 10vh;
    scale: 1.2;
}

.name {
    position: absolute;
    left: 50vw;
    top: 35vh;
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
    right: 37vw;
    top: 55vh;
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
        background-color: #FF6F3F;
        border: solid;
        border-color: #E54D1A;
        border-radius: 20rem;
        letter-spacing: 0.4rem;
        border-width: 0.5rem;
    }

    .content-wrapper {
        top: 35vh;
        left: -10vw;
        scale: 0.6;
    }

    .text-border {
        position: absolute;
        left: -30vw;
        top: -13vh;
        scale: 0.8;
    }

    .name {
        position: absolute;
        left: 2vw;
        top: 15vh;
        scale: 0.8;
    }

    .ufo {
        position: absolute;
        top: 40vh;
        left: 19vw;
        z-index: 2;
        scale: 0.9;
    }

    .ufo-rays {
        position: absolute;
        top: 47vh;
        left: 25vw;
        z-index: 1;
        scale: 0.9;
    }

    .marshie1 {
        position: absolute;
        top: 63vh;
        left: 37vw;
        z-index: 2;
        scale: 0.9;
    }

    .marshie2 {
        position: absolute;
        top: 78vh;
        left: 45vw;
        z-index: 2;
        scale: 0.9;
    }
}

/* @media (max-width: 500px) {
    .content-wrapper {
        width: 100%;
        margin-top: calc(298% - 232.5vw);
    }

    .gradient {
        background-color: #C4B500;
        padding-bottom: calc(341% - 240vw);
    }
} */
</style>