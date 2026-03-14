<template>
    <div id="sponsfin" class="container">
        <div class="team-name">Sponsorship & Finance</div>
        <div class="section">
            <RosterCard name="Abhinav Manda" position="Sponsorship & Finance Organizer" pronouns="he/him" :imageSrc="abhinavmanda" linkedinUrl="https://www.linkedin.com/in/abhinav-manda/" />
            <RosterCard name="Aditri Gadigi" position="Sponsorship & Finance Organizer" pronouns="she/her" linkedinUrl="http://www.linkedin.com/in/aditrig" :imageSrc="aditrigadigi" />
            <RosterCard name="Christopher Huang" position="Sponsorship & Finance Organizer" pronouns="he/him" :imageSrc="christopherhuang" linkedinUrl="https://www.linkedin.com/in/chrishuang47/" />
            <RosterCard name="Manit Mishra" position="Sponsorship & Finance Organizer" pronouns="he/him" :imageSrc="manitmishra" linkedinUrl="https://www.linkedin.com/in/manitmishra/" />
            <RosterCard name="Melanie Chen" position="Sponsorship & Finance Organizer" pronouns="she/her" linkedinUrl="https://www.linkedin.com/in/melaniechenn" :imageSrc="melaniechen" />
            <RosterCard name="Sania Manyem" position="Sponsorship & Finance Organizer" pronouns="she/her" :imageSrc="saniamanyem" linkedinUrl="https://www.linkedin.com/in/sania-manyem-9ab7652b6/" />
        </div>
    </div>
</template>

<script lang="ts">
import RosterCard from './RosterCard.vue'
import abhinavmanda from '../assets/img/images/headshots/AbhinavManda.webp'
import aditrigadigi from '../assets/img/images/headshots/AditriGadigi.webp'
import christopherhuang from '../assets/img/images/headshots/ChristopherHuang.webp'
import manitmishra from '../assets/img/images/headshots/ManitMishra.webp'
import melaniechen from '../assets/img/images/headshots/MelanieChen.webp'
import saniamanyem from '../assets/img/images/headshots/SaniaManyem.webp'

export default {
    name: 'RosterSponsFin',
    components: { RosterCard },
    data() {
        return {
            abhinavmanda,
            aditrigadigi,
            christopherhuang,
            manitmishra,
            melaniechen,
            saniamanyem
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
