<template>
    <div id="old" class="container">
        <div class="team-name">Senior Advisors</div>
        <div class="section">
            <RosterCard name="Anjali Samavedam" position="Senior Advisor" pronouns="she/her" linkedinUrl="https://www.linkedin.com/in/anjali-samavedam/" :imageSrc="anjalisamavedam" />
            <RosterCard name="Beatrice Chung" position="Senior Advisor" pronouns="she/her" linkedinUrl="https://www.linkedin.com/in/beatricechung/" :imageSrc="beatricechung" />
            <RosterCard name="Sai Pranav Theerthala" position="Senior Advisor" pronouns="he/him" linkedinUrl="https://www.linkedin.com/in/sai-pranav-theerthala" :imageSrc="saipranavtheerthala" />
            <RosterCard name="Sharvari Tirodkar" position="Senior Advisor" pronouns="she/her" linkedinUrl="http://linkedin.com/in/stirodka/" :imageSrc="sharvaritirodkar" />
        </div>
    </div>
</template>

<script lang="ts">
import RosterCard from './RosterCard.vue'
import anjalisamavedam from '../assets/img/images/headshots/AnjaliSamavedam.webp'
import beatricechung from '../assets/img/images/headshots/BeatriceChung.webp'
import saipranavtheerthala from '../assets/img/images/headshots/SaiPranavTheerthala.webp'
import sharvaritirodkar from '../assets/img/images/headshots/SharvariTirodkar.webp'

export default {
    name: 'RosterSenior',
    components: { RosterCard },
    data() {
        return {
            anjalisamavedam,
            beatricechung,
            saipranavtheerthala,
            sharvaritirodkar
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
