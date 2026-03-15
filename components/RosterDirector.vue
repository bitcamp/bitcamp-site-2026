<template>
    <div id="dir" class="container">
        <div class="team-name">Directors</div>
        <div class="section">
            <RosterCard name="Olivia Zhang" position="Design Director" pronouns="she/her" linkedinUrl="https://www.linkedin.com/in/oliviaszhang" :imageSrc="oliviazhang" />
            <RosterCard name="Harleen Green" position="Events Director" pronouns="she/her" linkedinUrl="https://www.linkedin.com/in/harleengreen" :imageSrc="harleengreen" />
            <RosterCard name="Avanti Athavale" position="Experience Director" pronouns="she/her" linkedinUrl="https://www.linkedin.com/in/avantiathavale/" :imageSrc="avantiathavale" />
            <RosterCard name="Jessica Zhou" position="Logistics Director" pronouns="she/her" linkedinUrl="https://www.linkedin.com/in/jessica-zhou-2a53021b3/" :imageSrc="jessicazhou" />
            <RosterCard name="Naomi Kaul" position="Logistics Director" pronouns="she/her" linkedinUrl="https://www.linkedin.com/in/naomi-kaul-a1b1341ba/" :imageSrc="naomikaul" />
            <RosterCard name="Purva Jani" position="Marketing Director" pronouns="she/her" linkedinUrl="https://www.linkedin.com/in/purva-jani/" :imageSrc="purvajani" />
            <RosterCard name="Bhavini Pandey" position="Sponsorship Director" pronouns="she/her" linkedinUrl="https://www.linkedin.com/in/bhavini-pandey-05/" :imageSrc="bhavinipandey" />
            <RosterCard name="Nikita Arya" position="Finance Director" pronouns="she/her" :imageSrc="nikitaarya" linkedinUrl="http://www.linkedin.com/in/nikitaaryaa" />
            <RosterCard name="Arya Gijare" position="Tech Director" pronouns="she/her" linkedinUrl="https://www.linkedin.com/in/arya-gijare/" :imageSrc="aryagijare" />
            <RosterCard name="Mohe Edeen Abu Maizer" position="Tech Director" pronouns="he/him" linkedinUrl="https://www.linkedin.com/in/moheedeen/" :imageSrc="moheedeenabumaizer" />
        </div>
    </div>
</template>

<script lang="ts">
import RosterCard from './RosterCard.vue'
import aryagijare from '../assets/img/images/headshots/aryagijare.webp'
import avantiathavale from '../assets/img/images/headshots/AvantiAthavale.webp'
import bhavinipandey from '../assets/img/images/headshots/bhavinipandey.webp'
import harleengreen from '../assets/img/images/headshots/HarleenGreen.webp'
import jessicazhou from '../assets/img/images/headshots/jessicazhou.webp'
import moheedeenabumaizer from '../assets/img/images/headshots/MoheEdeenAbuMaizer.webp'
import naomikaul from '../assets/img/images/headshots/naomikaul.webp'
import nikitaarya from '../assets/img/images/headshots/nikitaarya.webp'
import oliviazhang from '../assets/img/images/headshots/OliviaZhang.webp'
import purvajani from '../assets/img/images/headshots/PurvaJani.webp'

export default {
    name: 'RosterDirector',
    components: { RosterCard },
    data() {
        return {
            aryagijare,
            avantiathavale,
            bhavinipandey,
            harleengreen,
            jessicazhou,
            moheedeenabumaizer,
            naomikaul,
            nikitaarya,
            oliviazhang,
            purvajani
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
