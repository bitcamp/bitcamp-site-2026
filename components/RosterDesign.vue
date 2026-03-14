<template>
    <div id="design" class="container">
        <div class="team-name">Design</div>
        <div class="section">
            <RosterCard name="Aisiri Prasad" position="Design Organizer" pronouns="she/her" :imageSrc="aisiriprasad" linkedinUrl="https://www.linkedin.com/in/aisiriprasad" />
            <RosterCard name="Angela Zhang" position="Design Organizer" pronouns="she/her" linkedinUrl="https://www.linkedin.com/in/angela-zhang915/" :imageSrc="angelazhang" />
            <RosterCard name="Anning Cui" position="Design Organizer" pronouns="she/her" linkedinUrl="https://www.linkedin.com/in/cuianning/"/>
            <RosterCard name="Julie Lin" position="Design Organizer" pronouns="she/her" :imageSrc="julielin" linkedinUrl="https://www.linkedin.com/in/julie-xy-lin" />
            <RosterCard name="Leslie Kim" position="Design Organizer" pronouns="she/her" :imageSrc="lesliekim" linkedinUrl="https://www.linkedin.com/in/leslie-kim-0b05562b5" />
            <RosterCard name="Mykha Floresca" position="Design Organizer" pronouns="she/her" :imageSrc="mykhafloresca" linkedinUrl="https://www.linkedin.com/in/mykha-lizette-floresca-b97448247/" />
            <RosterCard name="Olivia King" position="Design Organizer" pronouns="she/her" :imageSrc="oliviaking" linkedinUrl="https://www.linkedin.com/in/olivia-king-9509b930a" />
            <RosterCard name="Tracy Anne Tan" position="Design Organizer" pronouns="she/her" linkedinUrl="https://www.linkedin.com/in/tracy-anne-tan-69a37a27b" :imageSrc="tracyannetan" />
            <RosterCard name="Tyler Song" position="Design Organizer" pronouns="he/him" :imageSrc="tylersong" linkedinUrl="https://www.linkedin.com/in/tyler-song-9a306b2a9" />
            <RosterCard name="Vivian Howe" position="Design Organizer" pronouns="she/her" linkedinUrl="https://www.linkedin.com/in/vivianhowe/" :imageSrc="vivianhowe" />
        </div>
    </div>
</template>

<script lang="ts">
import RosterCard from './RosterCard.vue'
import aisiriprasad from '../assets/img/images/headshots/AisiriPrasad.webp'
import angelazhang from '../assets/img/images/headshots/AngelaZhang.webp'
import julielin from '../assets/img/images/headshots/JulieLin.webp'
import lesliekim from '../assets/img/images/headshots/LeslieKim.webp'
import mykhafloresca from '../assets/img/images/headshots/MykhaFloresca.webp'
import oliviaking from '../assets/img/images/headshots/OliviaKing.webp'
import tracyannetan from '../assets/img/images/headshots/TracyAnneTan.webp'
import tylersong from '../assets/img/images/headshots/TylerSong.webp'
import vivianhowe from '../assets/img/images/headshots/VivianHowe.webp'

export default {
    name: 'RosterDesign',
    components: { RosterCard },
    data() {
        return {
            aisiriprasad,
            angelazhang,
            julielin,
            lesliekim,
            mykhafloresca,
            oliviaking,
            tracyannetan,
            tylersong,
            vivianhowe
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
