<template>
  <div class="wrapper" ref="el">
    <div class="app-container">
      <div class="stars-container">
        <div
          v-for="star in stars"
          :key="star.id"
          class="star"
          :style="{
            left: star.x + '%',
            top: star.y + 'px',
            width: star.size + 'px',
            height: star.size + 'px',
            animationDelay: star.delay + 's',
            animationDuration: star.duration + 's',
          }"
        ></div>
      </div>
      <div class="red-planet"></div>
      <div class="blue-planet"></div>
      <div class="green-planet-bg"></div>
      <BitBot />
      <Navbar />
      <LandingPage />
      <div class="transition0"></div>
      <TracksPage />
      <CampGamesPage />
      <!-- <Schedule :styles="{ height: '80vh', minHeight: '60rem' }" /> -->
      <TeamPage />
      <div class="transition1"></div>
      <FAQSponsorPage />
      <FooterContent />
    </div>
  </div>
</template>

<script lang="ts" setup>
const pageHeight = 8000;
const stars = Array.from({ length: 500 }, (_, i) => ({
  id: i,
  x: Math.random() * 100,
  y: Math.random() * pageHeight,
  size: Math.random() * 2.5 + 1,
  delay: Math.random() * 5,
  duration: Math.random() * 3 + 2,
}));

useHead({
  title: "Bitcamp",
  bodyAttrs: {
    style: "background-color: #010218;",
  },
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

.stars-container {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 0;
  pointer-events: none;
}

.star {
  position: absolute;
  border-radius: 50%;
  background-color: #ffffff;
  animation: twinkle ease-in-out infinite alternate;
}

@keyframes twinkle {
  0% {
    opacity: 0.15;
    transform: scale(0.8);
    box-shadow: 0 0 2px rgba(255, 255, 255, 0.3);
  }
  100% {
    opacity: 1;
    transform: scale(1.2);
    box-shadow: 0 0 6px rgba(255, 255, 255, 0.8);
  }
}

@keyframes float {
  0% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(var(--float-distance));
  }
  100% {
    transform: translateY(0);
  }
}

.red-planet {
  --float-distance: -380px;
  will-change: transform;
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
  animation: float 25s infinite ease-in-out;
}

.blue-planet {
  --float-distance: -300px;
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
  animation: float 35s infinite ease-in-out;
}

.green-planet-bg {
  --float-distance: -120px;
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
  animation: float 60s infinite ease-in-out;
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
    /* background-color: #d3d3d3; */
    opacity: 40%;
    z-index: 10;
    margin-left: 10%;
    width: 80%;
  }
  .transition1 {
    /* background-color: #010b18; */
    height: 4vw;
  }
}

.transition1 {
  /* background-color: #010b18; */
  height: 4vw;
}
</style>
