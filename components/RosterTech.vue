<template>
  <div id="tech" class="container">
    <div class="team-name">Tech</div>
    <div class="section">
      <RosterCard
        name="Ananya Srinivasan"
        position="Tech Organizer"
        pronouns="she/her"
        :imageSrc="ananyasrinivasan"
        linkedinUrl=""
      />
      <RosterCard
        name="Anika Thakur"
        position="Tech Organizer"
        pronouns="she/her"
        :imageSrc="anikathakur"
        linkedinUrl="https://www.linkedin.com/in/anika-thakur"
      />
      <RosterCard
        name="Daniel Yi"
        position="Tech Organizer"
        pronouns="he/him"
        :imageSrc="danielyi"
        linkedinUrl="https://github.com/eggoil166"
      />
      <!-- <RosterCard
        name="Harini Thirukonda"
        position="Tech Organizer"
        pronouns="she/her"
        linkedinUrl="https://www.linkedin.com/in/harini-thirukonda-190036238/"
        :imageSrc="harinithirukonda"
      /> -->
      <RosterCard
        name="Harrison Padgett"
        position="Tech Organizer"
        pronouns="he/him"
        linkedinUrl="https://www.linkedin.com/in/harrison-padgett"
        :imageSrc="harrisonpadgett"
      />
      <RosterCard
        name="Jadon Chu"
        position="Tech Organizer"
        pronouns="he/him"
        :imageSrc="jadonchu"
        linkedinUrl="https://www.linkedin.com/in/jadon-g-chu"
      />
      <!-- <RosterCard
        name="Joseph Cho"
        position="Tech Organizer"
        pronouns="he/him"
        :imageSrc="josephcho"
        linkedinUrl="https://www.linkedin.com/in/jcho1114"
      /> -->
      <RosterCard
        name="Lusenie Turay"
        position="Tech Organizer"
        pronouns="he/him"
        :imageSrc="lusenieturay"
        linkedinUrl="https://www.linkedin.com/in/lusenie-turay"
      />
      <RosterCard
        name="Sanya Gupta"
        position="Tech Organizer"
        pronouns="she/her"
        linkedinUrl="https://www.linkedin.com/in/sanya-gupta7"
        :imageSrc="sanyagupta"
      />
      <!-- <RosterCard
        name="Srujana Theerthala"
        position="Tech Organizer"
        pronouns="she/her"
        linkedinUrl="https://www.linkedin.com/in/srujana-theerthala-165671262"
        :imageSrc="srujanatheerthala"
      /> -->
      <RosterCard
        name="Swathi Pulipati"
        position="Tech Organizer"
        pronouns="she/her"
        linkedinUrl="https://linkedin.com/in/swathi-pulipati-1b450b232"
        :imageSrc="swathipulipati"
      />
      <RosterCard
        name="Thiru Sethuraman"
        position="Tech Organizer"
        pronouns="he/him"
        :imageSrc="thirusethuraman"
        linkedinUrl="https://www.linkedin.com/in/thirus27"
      />
      <RosterCard
        name="Tyson Cheung"
        position="Tech Organizer"
        pronouns="he/him"
        linkedinUrl="https://www.linkedin.com/in/tyson-cheung"
        :imageSrc="tysoncheung"
      />
    </div>
  </div>
</template>

<script lang="ts">
import RosterCard from "./RosterCard.vue";
import ananyasrinivasan from "../assets/img/images/headshots/AnanyaSrinivasan.webp";
import anikathakur from "../assets/img/images/headshots/AnikaThakur.webp";
import danielyi from "../assets/img/images/headshots/DanielYi.webp";
import harinithirukonda from "../assets/img/images/headshots/harinithirukonda.webp";
import harrisonpadgett from "../assets/img/images/headshots/harrisonpadgett.webp";
import jadonchu from "../assets/img/images/headshots/JadonChu.webp";
import josephcho from "../assets/img/images/headshots/JosephCho.webp";
import lusenieturay from "../assets/img/images/headshots/LusenieTuray.webp";
import sanyagupta from "../assets/img/images/headshots/sanyagupta.webp";
import srujanatheerthala from "../assets/img/images/headshots/srujanatheerthala.webp";
import swathipulipati from "../assets/img/images/headshots/swathipulipati.webp";
import thirusethuraman from "../assets/img/images/headshots/thirusethuraman.webp";
import tysoncheung from "../assets/img/images/headshots/tysoncheung.webp";

export default {
  name: "RosterTech",
  components: { RosterCard },
  data() {
    return {
      ananyasrinivasan,
      anikathakur,
      danielyi,
      harinithirukonda,
      harrisonpadgett,
      jadonchu,
      josephcho,
      lusenieturay,
      sanyagupta,
      srujanatheerthala,
      swathipulipati,
      thirusethuraman,
      tysoncheung,
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
