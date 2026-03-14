<template>
    <div id="log" class="container">
        <div class="team-name">Logistics</div>
        <div class="section">
            <RosterCard name="Angela Wu" position="Logistics Organizer" pronouns="she/her" :imageSrc="angelawu" />
            <RosterCard name="Anoushka Arora" position="Logistics Organizer" pronouns="she/her" linkedinUrl="https://www.linkedin.com/in/anoushka-arora-b77929153/" :imageSrc="anoushkaarora" />
            <RosterCard name="Ben Losey" position="Logistics Organizer" pronouns="he/him" :imageSrc="benlosey" />
            <RosterCard name="Charis Wang" position="Logistics Organizer" pronouns="she/her" linkedinUrl="https://www.linkedin.com/in/charswng/" :imageSrc="chariswang" />
            <RosterCard name="Daanial Haris" position="Logistics Organizer" pronouns="he/him" :imageSrc="daanialharis" />
            <RosterCard name="James Barry" position="Logistics Organizer" pronouns="he/him" :imageSrc="jamesbarry" />
            <RosterCard name="Ryan Zhao" position="Logistics Organizer" pronouns="he/him" linkedinUrl="https://www.linkedin.com/in/ryanzhao27/" :imageSrc="ryanzhao" />
            <RosterCard name="Sneha Balur" position="Logistics Organizer" pronouns="she/her" linkedinUrl="https://www.linkedin.com/in/sneha-balur/" :imageSrc="snehabalur" />
            <RosterCard name="Stanley Xu" position="Logistics Organizer" pronouns="he/him" :imageSrc="stanleyxu" />
            <RosterCard name="Tiffany Liu" position="Logistics Organizer" pronouns="she/her" linkedinUrl="https://www.linkedin.com/in/tiffany-liu-776628244/" :imageSrc="tiffanyliu" />
            <RosterCard name="Zayan Ahmad" position="Logistics Organizer" pronouns="he/him" :imageSrc="zayanahmad" />
        </div>
    </div>
</template>

<script lang="ts">
import RosterCard from './RosterCard.vue'
import angelawu from '../assets/img/images/headshots/AngelaWu.webp'
import anoushkaarora from '../assets/img/images/headshots/AnoushkaArora.webp'
import benlosey from '../assets/img/images/headshots/BenLosey.webp'
import chariswang from '../assets/img/images/headshots/CharisWang.webp'
import daanialharis from '../assets/img/images/headshots/DaanialHaris.webp'
import jamesbarry from '../assets/img/images/headshots/JamesBarry.webp'
import ryanzhao from '../assets/img/images/headshots/RyanZhao.webp'
import snehabalur from '../assets/img/images/headshots/SnehaBalur.webp'
import stanleyxu from '../assets/img/images/headshots/StanleyXu.webp'
import tiffanyliu from '../assets/img/images/headshots/TiffanyLiu.webp'
import zayanahmad from '../assets/img/images/headshots/ZayanAhmad.webp'

export default {
    name: 'RosterLog',
    components: { RosterCard },
    data() {
        return {
            angelawu,
            anoushkaarora,
            benlosey,
            chariswang,
            daanialharis,
            jamesbarry,
            ryanzhao,
            snehabalur,
            stanleyxu,
            tiffanyliu,
            zayanahmad
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
