<template>
  <div class="wrapper" ref="el">
    <div class="app-container">
      <div class="red-planet"></div>
      <div class="blue-planet"></div>
      <div class="green-planet-bg"></div>
      <!-- <BitBot /> -->
      <Navbar />
      <LandingPage />
      <div class="transition0"></div>
      <TracksPage />
      <CampGamesPage />
      <Schedule :styles="{ height: '80vh', minHeight: '60rem' }" />
      <TeamPage />
      <div class="transition1"></div>
      <FAQSponsorPage />
      <FooterContent />
    </div>
  </div>
</template>

<script lang="ts" setup>
useHead({
  title: "Bitcamp",
  meta: [
    {
      name: "description",
      content:
        "Bitcamp is a place for exploration. You will have 36 hours to delve into your curiosities, learn something new, and make something awesome. With world-class mentors and hundreds of fellow campers, you're in for an amazing time. If you're ready for an adventure, see you by the fire!",
    },
    {
      property: "og:title",
      content: "Bitcamp 2025",
    },
    {
      property: "og:site_name",
      content: "Bitcamp 2025",
    },
    {
      property: "og:url",
      content: "https://bit.camp/",
    },
    {
      property: "og:description",
      content:
        "Bitcamp is a place for exploration. You will have 36 hours to delve into your curiosities, learn something new, and make something awesome. With world-class mentors and hundreds of fellow campers, you're in for an amazing time. If you're ready for an adventure, see you by the fire!",
    },
    {
      property: "og:type",
      content: "website",
    },
    {
      property: "twitter:card",
      content: "summary",
    },
    {
      property: "twitter:url",
      content: "https://bit.camp/",
    },
    {
      property: "twitter:title",
      content: "Bitcamp 2025",
    },
    {
      property: "twitter:description",
      content:
        "Bitcamp is a place for exploration. You will have 36 hours to delve into your curiosities, learn something new, and make something awesome. With world-class mentors and hundreds of fellow campers, you're in for an amazing time. If you're ready for an adventure, see you by the fire!",
    },
    {
      name: "msapplication-TileColor",
      content: "#ff6f3f",
    },
    {
      name: "msapplication-config",
      content: "/bitcamp-brand/favicons/browserconfig.xml",
    },
    {
      name: "theme-color",
      content: "#ffffff",
    },
  ],
  link: [
    {
      rel: "icon",
      type: "image/png",
      sizes: "32x32",
      href: "/bitcamp-brand/favicons/favicon-32x32.png",
    },
    {
      rel: "icon",
      type: "image/png",
      sizes: "16x16",
      href: "/bitcamp-brand/favicons/favicon-16x16.png",
    },
    {
      rel: "manifest",
      href: "/bitcamp-brand/favicons/site.webmanifest",
    },
    {
      rel: "mask-icon",
      href: "/bitcamp-brand/favicons/safari-pinned-tab.svg",
      color: "#ff6f3f",
    },
    {
      rel: "shortcut icon",
      href: "/bitcamp-brand/favicons/favicon.ico",
    },
  ],
});
</script>
<script lang="ts">
import BitBot from "~/components/BitBot.vue";

// import { Break } from '#build/components';
import Navbar from "~/components/Navbar.vue";
import Schedule from "~/components/Schedule.vue";
// import Break from '../components/Break.vue';
// import CampGamesPage from '../components/CampGamesPage.vue';
// import FAQSponsorPage from '../components/FAQSponsorPage.vue';
// import FooterContent from "../components/FooterContent.vue"
// import LandingPage from '../components/LandingPage.vue';
// import TeamPage from '../components/TeamPage.vue';
// import TracksPage from '../components/TracksPage.vue';

export default {
  name: "HomePage",
  // components: { Navbar, FooterContent, LandingPage, Break, TracksPage, CampGamesPage, TeamPage, FAQSponsorPage },
  components: { BitBot, Navbar, Schedule },
};
</script>

<style scoped>
.wrapper {
  overflow-y: scroll;
  overflow-x: hidden;
  height: 100dvh;
}

.app-container {
  overflow: hidden;
  /* overflow-y: scroll; */
  display: flex;
  flex-direction: column;
  width: 100vw;
  min-height: 100vh;
  background-size: 100% auto;
  background-repeat: no-repeat;
  background-color: #010b18;
  position: relative;
  z-index: 1;
}

.red-planet {
  position: absolute;
  right: -800px;
  top: 2000px;
  width: 80%;
  height: 80%;
  background-image: url("../assets/img/images/red-planet.webp");
  background-size: contain;
  background-repeat: no-repeat;
  z-index: -1;
  pointer-events: none;
}

.blue-planet {
  position: absolute;
  left: -1550px;
  top: 3010px;
  width: 150%;
  height: 150%;
  background-image: url("../assets/img/images/blue-planet.webp");
  background-size: contain;
  background-repeat: no-repeat;
  z-index: -1;
  pointer-events: none;
}

.green-planet-bg {
  position: absolute;
  right: -50px;
  bottom: 25%;
  width: 500px;
  height: 500px;
  background-image: url("../assets/img/images/green-planet.webp");
  background-size: contain;
  background-repeat: no-repeat;
  z-index: 0;
  pointer-events: none;
}

.LandingPage,
.TracksPage,
.CampGamesPage {
  position: absolute;
  width: 100%;
}

.LandingPage {
  top: 0;
  height: 33%;
  /* Adjust height as needed */
  background-color: lightblue;
  z-index: 1;
  display: flex;
  justify-content: center;
  align-items: center;
}

.TracksPage {
  top: 25%;
  /* Controls overlap with Landing Page */
  height: 50%;
  /* Adjust height as needed */
  /* background-color: lightgreen; */
  z-index: 2;
  display: flex;
  justify-content: center;
  align-items: center;
}

.CampGamesPage {
  bottom: 0;
  height: 33%;
  /* Adjust height as needed */
  /* background-color: lightcoral; */
  z-index: 1;
  display: flex;
  justify-content: center;
  align-items: center;
}

/* .Schedule {
  background: linear-gradient(to bottom, #31055a 0%, #2b0542 8%, #580000 100%);
} */
/* .transition0 {
  width: 100%;
  height: 2px;
  background-color: #000000;
  z-index: 10;
} */

@media (max-width: 1300px) {
  .blue-planet {
    left: -1250px;
    top: 2410px;
  }
  .red-planet {
    right: -700px;
    top: 1700px;
  }
}

@media (max-width: 1150px) {
  .green-planet-bg {
    right: -50px;
    bottom: 24%;
  }
}

@media (max-width: 1100px) {
  .blue-planet {
    display: none;
  }
  .red-planet {
    display: none;
  }
  .green-planet-bg {
    display: none;
  }
}
@media (max-width: 796px) {
  .transition0 {
    width: 100%;
    height: 2px;
    background-color: #d3d3d3;
    opacity: 40%;
    z-index: 10;
    margin-left: 10%;
    width: 80%;
  }
  .transition1 {
    background-color: #010b18;
    height: 4vw;
  }
}

.transition1 {
  background-color: #010b18;
  height: 4vw;
}
</style>
