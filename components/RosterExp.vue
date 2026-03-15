<template>
    <div id="exp" class="container">
        <div class="team-name">Experience</div>
        <div class="section">
            <RosterCard name="Anannya Trehan" position="Experience Organizer" pronouns="she/her" linkedinUrl="https://www.linkedin.com/in/anannya-trehan/" :imageSrc="anannyatrehan" />
            <RosterCard name="Debarshi Dey" position="Experience Organizer" pronouns="he/him" :imageSrc="debarshidey" linkedinUrl="https://www.linkedin.com/in/debarshi-dey/" />
            <RosterCard name="Kathrine Natesan" position="Experience Organizer" pronouns="she/her" :imageSrc="kathrinenatesan" linkedinUrl="https://www.linkedin.com/in/kathrine-natesan-041a713a5/"/>
            <RosterCard name="Mazin Nadaf" position="Experience Organizer" pronouns="he/him" :imageSrc="mazinnadaf" linkedinUrl="https://www.linkedin.com/in/mazin-nadaf" />
            <RosterCard name="Michelle Rhee" position="Experience Organizer" pronouns="she/her" linkedinUrl="https://www.linkedin.com/in/michelle-rhee-900903292/" :imageSrc="michellerhee" />
            <RosterCard name="Michelle Yu" position="Experience Organizer" pronouns="she/her" linkedinUrl="https://www.linkedin.com/in/michelle-yu-57122b246/" :imageSrc="michelleyu" />
            <RosterCard name="Neha Dheenadhayalan" position="Experience Organizer" pronouns="she/her" :imageSrc="nehadheenadhayalan" linkedinUrl="https://www.linkedin.com/in/nehadheen" />
            <RosterCard name="Nithika Ramanathan" position="Experience Organizer" pronouns="she/her" linkedinUrl="https://www.linkedin.com/in/nithika-ramanathan/" :imageSrc="nithikaramanathan" />
            <RosterCard name="Sachi Verma" position="Experience Organizer" pronouns="she/her" :imageSrc="sachiverma" linkedinUrl="https://www.linkedin.com/in/sachiverma06" />
            <RosterCard name="Sifene Fufa" position="Experience Organizer" pronouns="she/her" :imageSrc="sifenefufa" linkedinUrl="https://www.linkedin.com/in/sifene-fufa-a8975b33b/" />
        </div>
    </div>
</template>

<script lang="ts">
import RosterCard from './RosterCard.vue'
import anannyatrehan from '../assets/img/images/headshots/AnannyaTrehan.webp'
import debarshidey from '../assets/img/images/headshots/DebarshiDey.webp'
import kathrinenatesan from '../assets/img/images/headshots/KathrineNatesan.webp'
import mazinnadaf from '../assets/img/images/headshots/MazinNadaf.webp'
import michellerhee from '../assets/img/images/headshots/MichelleRhee.webp'
import michelleyu from '../assets/img/images/headshots/MichelleYu.webp'
import nehadheenadhayalan from '../assets/img/images/headshots/NehaDheenadhayalan.webp'
import nithikaramanathan from '../assets/img/images/headshots/NithikaRamanathan.webp'
import sachiverma from '../assets/img/images/headshots/SachiVerma.webp'
import sifenefufa from '../assets/img/images/headshots/SifeneFufa.webp'

export default {
    name: 'RosterExp',
    components: { RosterCard },
    data() {
        return {
            anannyatrehan,
            debarshidey,
            kathrinenatesan,
            mazinnadaf,
            michellerhee,
            michelleyu,
            nehadheenadhayalan,
            nithikaramanathan,
            sachiverma,
            sifenefufa
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
