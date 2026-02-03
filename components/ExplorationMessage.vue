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
    padding-top: 4rem;
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
    color: #FFF7EB;
    text-align: center;
    font-family: 'Aleo', serif;
    font-size: 46.14px;
    font-style: italic;
    font-weight: 800;
    line-height: 100%; 
    letter-spacing: 0; 
    text-shadow: 0 0 20.82px rgba(255, 249, 240, 1); 
    margin-bottom: 1.5rem;
    width: 753px;
    max-width: 90vw;
    margin-left: auto;
    margin-right: auto;
}
.description {
    color: #FFF7EB; 
    text-align: center;
    font-family: 'Avenir', sans-serif;
    font-size: 24px;
    font-style: normal;
    font-weight: 400;
    line-height: 100%; 
    letter-spacing: 0; 
    opacity: 0.9;
    width: 752.4px;
    max-width: 90vw;
    margin-left: auto;
    margin-right: auto;
}

@media (max-width: 796px) {
    .exploration-container {
        padding-top: 0;
        height: auto;
        width: 100%;
        display: flex;
        justify-content: center;
    }
    .exploration-message {
        background: linear-gradient(180deg, #010B18 0%, #201F3A 50%, #0D2539 100%);
        padding: 3rem 2rem;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        width: 100%; /* FULL WIDTH */
        margin: 0 auto;
        border-radius: 0; /* Remove rounded corners for full width */
        box-shadow: none;
    }
    .title {
        width: 90%;
        max-width: 323px;
        height: auto;
        font-family: 'Aleo', serif;
        font-weight: 800;
        font-style: italic;
        font-size: 36px; 
        line-height: 110%; 
        letter-spacing: 0;
        text-align: center;
        margin-bottom: 1.5rem;
    }
    .description {
        width: 90%;
        max-width: 323px; 
        height: auto;
        font-family: 'Avenir', sans-serif;
        font-weight: 400;
        font-style: normal;
        font-size: 18px; 
        line-height: 140%; 
        letter-spacing: 0;
        text-align: center;
        margin: 0 auto;
    }
}

@media (max-width: 500px) {
    .exploration-container {
        padding-top: 0;
        height: auto;
        width: 100%;
        display: flex;
        justify-content: center;
    }
    .exploration-message {
        background: linear-gradient(180deg, #010B18 0%, #201F3A 50%, #0D2539 100%);
        padding: 2.5rem 1.5rem;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        width: 100%; /* FULL WIDTH */
        margin: 0 auto;
        border-radius: 0; /* Remove rounded corners for full width */
        box-shadow: none;
    }
    .title {
        width: 90%;
        max-width: 323px;
        height: auto;
        font-family: 'Aleo', serif;
        font-weight: 800;
        font-style: italic;
        font-size: 32px; 
        line-height: 110%;
        letter-spacing: 0;
        text-align: center;
        margin-bottom: 1.5rem;
    }
    .description {
        width: 90%;
        max-width: 323px;
        height: auto;
        font-family: 'Avenir', sans-serif;
        font-weight: 400;
        font-style: normal;
        font-size: 16px; 
        line-height: 140%;
        letter-spacing: 0;
        text-align: center;
        margin: 0 auto;
    }
}
</style>