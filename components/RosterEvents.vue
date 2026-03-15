<template>
  <div id="events" class="container">
    <div class="team-name">Events</div>
    <div class="section">
      <RosterCard
        name="Adrian Alphons"
        position="Events Organizer"
        pronouns="he/him"
        :imageSrc="adrianalphons"
        linkedinUrl="https://www.linkedin.com/in/adrian-alphons"
      />
      <RosterCard
        name="Alisha Rajadhyksha"
        position="Events Organizer"
        pronouns="she/her"
        :imageSrc="alisharajadhyksha"
        linkedinUrl="https://www.linkedin.com/in/alisha-rajadhyksha"
      />
      <RosterCard
        name="Anunithaa Rajakumaresan"
        position="Events Organizer"
        pronouns="she/her"
        :imageSrc="anunithaarajakumaresan"
        linkedinUrl="https://www.linkedin.com/in/anunithaa-rajakumaresan-180261238/"
      />
      <RosterCard
        name="Ethan Zhu"
        position="Events Organizer"
        pronouns="he/him"
        :imageSrc="ethanzhu"
        linkedinUrl="https://www.linkedin.com/in/etzhu/"
      />
      <RosterCard
        name="Hannah Chen"
        position="Events Organizer"
        pronouns="she/her"
        linkedinUrl="https://www.linkedin.com/in/hannah-chen-30099b27b"
        :imageSrc="hannahchen"
      />
      <RosterCard
        name="Saanvi Kataria"
        position="Events Organizer"
        pronouns="she/her"
        linkedinUrl="https://www.linkedin.com/in/-saanvikataria"
        :imageSrc="saanvikataria"
      />
      <RosterCard
        name="Sofie Douglass"
        position="Events Organizer"
        pronouns="she/her"
        :imageSrc="sofiedouglass"
        linkedinUrl="https://www.linkedin.com/in/sofia-douglass-6952b0395"
      />
    </div>
  </div>
</template>

<script lang="ts">
import RosterCard from "./RosterCard.vue";
import adrianalphons from "../assets/img/images/headshots/AdrianAlphons.webp";
import alisharajadhyksha from "../assets/img/images/headshots/AlishaRajadhyksha.webp";
import anunithaarajakumaresan from "../assets/img/images/headshots/AnunithaaRajakumaresan.webp";
import ethanzhu from "../assets/img/images/headshots/EthanZhu.webp";
import hannahchen from "../assets/img/images/headshots/HannahChen.webp";
import saanvikataria from "../assets/img/images/headshots/SaavniKataria.webp";
import sofiedouglass from "../assets/img/images/headshots/SofieDouglass.webp";

export default {
  name: "RosterEvents",
  components: { RosterCard },
  data() {
    return {
      adrianalphons,
      alisharajadhyksha,
      anunithaarajakumaresan,
      ethanzhu,
      hannahchen,
      saanvikataria,
      sofiedouglass,
    };
  },
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
  color: #ffffff;
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
