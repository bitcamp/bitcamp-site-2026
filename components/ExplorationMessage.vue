<template>
    <div class="exploration-container">
        <div class="exploration-message">
            <h1 class="title"><i>Bitcamp is a place for exploration.</i></h1> 
            <p class="description">
                You have 36 hours to explore, learn, and create with world-class mentors and over 1,000 participants. Whether you're a seasoned hacker or new to it all, there's something for everyone.
            </p>
        </div>
    </div>
</template>

<script lang="ts">
export default {
    name: "ExplorationMessage",
};
</script>
<style scoped>

.exploration-container {
    padding-top: 40px;
    position: relative;
    width: 100%;
    display: flex;
    justify-content: center;
}

.exploration-message {
    background-color: transparent; 
    border: none;
    color: white;
    padding: 3rem 2rem;
    font-family: Aleo, serif;
    box-sizing: border-box;
    max-width: 100rem;
    text-align: center;
    margin: 0 auto; 
}

.title {
    color: #FFF9F0;
    text-align: center;
    font-family: 'Aleo', serif;
    font-size: clamp(36px, 4.5vw, 46.144px); 
    font-style: italic;
    font-weight: 800;
    line-height: 1.1;
    text-shadow: 0 0 20.82px rgba(255, 249, 240, 1); 
    margin-bottom: 1.5rem;
    width: clamp(322.893px, 50vw, 800px); 
    margin-left: auto;
    margin-right: auto;
}

.description {
    color: #FFF7EB; 
    text-align: center;
    font-family: 'Avenir', sans-serif;
    font-size: clamp(18px, 2vw, 24px); 
    font-style: normal;
    font-weight: 400;
    line-height: 1.5;
    opacity: 0.9;
    width: clamp(323px, 60vw, 752.48px); 
    margin-left: auto;
    margin-right: auto;
}

@media (max-width: 796px) {
    .exploration-container {
        padding-top: 0;
        height: auto;
        position: relative; 
        top: 9px; 

    }

    .exploration-message {
        position: relative; 
        top: 510px; 
        float: none;
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 100%;
    }

    .title {
        width: 322.8927001953125;
        height: 86;
        left: 0.11px;
        angle: 0 deg;
        opacity: 1;
        font-family: Aleo;
        font-weight: 800;
        font-style: Italic;
        font-size: 36px;
        leading-trim: NONE;
        line-height: 100%;
        letter-spacing: 0%;
        text-align: center;

    }

    .description {
        width: 323;
        height: 125;
        angle: 0 deg;
        opacity: 1;
        font-family: Avenir;
        font-weight: 400;
        font-style: Roman;
        font-size: 18px;
        leading-trim: NONE;
        line-height: 100%;
        letter-spacing: 0%;
        text-align: center;


    }
}

@media (max-width: 500px) {
     .exploration-container {
        padding-top: 0;
        height: auto;
        position: relative; 
        top: 4px; 
; 

    }
    .exploration-message {
        top: 510px; 
    }

    .title {
        width: 322.8927001953125;
        height: 86;
        left: 0.11px;
        angle: 0 deg;
        opacity: 1;
        font-family: Aleo;
        font-weight: 800;
        font-style: Italic;
        font-size: 36px;
        leading-trim: NONE;
        line-height: 100%;
        letter-spacing: 0%;
        text-align: center;


    }

    .description {
        font-family: Avenir;
        font-weight: 400;   
        font-style: Roman;
        font-size: 18px;
        leading-trim: NONE;
        line-height: 100%;
        letter-spacing: 0%;
        text-align: center;

    }
}
</style>