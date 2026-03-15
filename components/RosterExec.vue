<template>
    <div id="exec" class="container">
        <div class="team-name">Co-Execs</div>
        <div class="section">
            <RosterCard name="Neha Veeragandham" position="Co-Executive Director" pronouns="she/her" linkedinUrl="https://www.linkedin.com/in/nehaveeragandham/" :imageSrc="nehaveeragandham" />
            <RosterCard name="Saloni Shah" position="Co-Executive Director" pronouns="she/her" linkedinUrl="https://www.linkedin.com/in/saloni-k-shah/" :imageSrc="salonishah" />
        </div>
    </div>
</template>

<script lang="ts">
import RosterCard from './RosterCard.vue'
import nehaveeragandham from '../assets/img/images/headshots/NehaVeeragandham.webp'
import salonishah from '../assets/img/images/headshots/SaloniShah.webp'

export default {
    name: 'RosterExec',
    components: { RosterCard },
    data() {
        return {
            nehaveeragandham,
            salonishah
        }
    }
};
</script>

<style scoped>
.container {
    display: flex;
    flex-direction: column;
}

.team-name {
    font-family: Aleo;
    font-weight: 700;
    font-size: 4vh;
    letter-spacing: 0%;
    text-align: center;
    color: #FFFFFF;
    width: 100%;
    padding-top: 5vh;
    padding-bottom: 2vh;
}

.section {
    display: flex;
    justify-content: center;
    align-content: center;
    flex-wrap: wrap;
    width: 100%;
}
</style>
