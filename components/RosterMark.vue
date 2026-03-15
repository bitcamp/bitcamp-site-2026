<template>
    <div id="mark" class="container">
        <div class="team-name">Marketing</div>
        <div class="section">
            <RosterCard name="Anushka Agarwal" position="Marketing Organizer" pronouns="she/her" :imageSrc="anushkaagarwal" linkedinUrl="https://www.linkedin.com/in/anushka-agarwal-167922271" />
            <RosterCard name="Grace Yang" position="Marketing Organizer" pronouns="she/her" linkedinUrl="https://www.linkedin.com/in/graceyang2027/" :imageSrc="graceyang" />
            <RosterCard name="Habib Camara" position="Marketing Organizer" pronouns="he/him" :imageSrc="habibcamara" linkedinUrl="https://www.linkedin.com/in/habib-camara-4b4ab629a/" />
            <RosterCard name="Haswita Bokkisam" position="Marketing Organizer" pronouns="she/her" :imageSrc="haswitabokkisam" linkedinUrl="https://www.linkedin.com/in/haswita-bokkisam" />
            <RosterCard name="Isaac Lee" position="Marketing Organizer" pronouns="he/him" :imageSrc="isaaclee" linkedinUrl="https://www.linkedin.com/in/isaacjeelee" />
            <RosterCard name="Kai Chen" position="Marketing Organizer" pronouns="he/him" linkedinUrl="https://www.linkedin.com/in/kaiichen/" :imageSrc="kaichen" />
            <RosterCard name="Sameer Chawla" position="Marketing Organizer" pronouns="he/him" linkedinUrl="https://www.linkedin.com/in/sameer-chawla01/" :imageSrc="sameerchawla" />
            <RosterCard name="Srinidhi Guruvayurappan" position="Marketing Organizer" pronouns="she/her" :imageSrc="srinidhiguruvayurappan" linkedinUrl="https://www.linkedin.com/in/srinidhi-guruvayurappan-1a40a829a/" />
        </div>
    </div>
</template>

<script lang="ts">
import RosterCard from './RosterCard.vue'
import anushkaagarwal from '../assets/img/images/headshots/AnushkaAgarwal.webp'
import graceyang from '../assets/img/images/headshots/GraceYang.webp'
import habibcamara from '../assets/img/images/headshots/HabibCamara.webp'
import haswitabokkisam from '../assets/img/images/headshots/HaswitaBokkisam.webp'
import isaaclee from '../assets/img/images/headshots/IsaacLee.webp'
import kaichen from '../assets/img/images/headshots/KaiChen.webp'
import sameerchawla from '../assets/img/images/headshots/SameerChawla.webp'
import srinidhiguruvayurappan from '../assets/img/images/headshots/SrinidhiGuruvayurappan.webp'

export default {
    name: 'RosterMark',
    components: { RosterCard },
    data() {
        return {
            anushkaagarwal,
            graceyang,
            habibcamara,
            haswitabokkisam,
            isaaclee,
            kaichen,
            sameerchawla,
            srinidhiguruvayurappan
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
