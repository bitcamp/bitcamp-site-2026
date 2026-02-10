<template>
    <div class="exploration-container">
        <div class="exploration-message">
            <h1 class="title"><i> Bitcamp is a place for exploration.</i></h1> 
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

.exploration-message {
    background-color: transparent; 
    boarder: none;
    float: right;
    color: white;
    padding: 3rem 5rem;
    font-family: Aleo, serif;
    box-sizing: border-box;
    max-width: 100rem;
    text-align: center;
}

.title {
    color: #FFF9F0;
    text-align: center;
    font-family: 'Aleo', serif;
    font-size: 46.144px;
    font-style: italic;
    font-weight: 800;
    line-height: normal;

    /* The Glow effect behind the text */
    text-shadow: 0 0 20.82px rgba(255, 249, 240, 1); 
    margin-bottom: 1.5rem;

}

.description {
    color: var(#FFF7EB);
    text-align: center;
    font-family: 'Avenir', sans-serif;
    font-size: 24px;
    font-style: normal;
    font-weight: 400;
    line-height: normal;
    opacity: 0.9;
}

.exploration-container {
    padding-top: 40px;
    position: relative;
    width: 100%;
}

@media (max-width: 796px) {
    .exploration-message {
        border: 0;
        border-radius: 0;
        text-align: center;
        width: 100%;
        margin: 0;
        padding: 10vw;
        max-width: none;
        font-size: 5vw;
        box-shadow: none;
    }
}
</style>
