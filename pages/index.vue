<template>
  <div class="wrapper" ref="el">
    <div class="app-container" :style="pageHeightStyle">
      <div class="stars-container">
        <div class="space-stars-bg"></div>
        <div class="space-clouds-bg"></div>
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

      <div class="marker-layer">
        <div class="marker-container initial">
          <div
            class="moving-box"
            :style="{ backgroundImage: `url(${floatingMarshie})` }"
          ></div>
        </div>

        <div class="marker-container second"><div class="marker"></div></div>
        <div class="marker-container third"><div class="marker"></div></div>
        <div class="marker-container fourth"><div class="marker"></div></div>
        <div class="marker-container fifth"><div class="marker"></div></div>
        <div class="marker-container sixth"><div class="marker"></div></div>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import floatingMarshie from "@/assets/img/images/floating_marshie.svg";
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { MotionPathPlugin } from "gsap/MotionPathPlugin";
import { onMounted, onUnmounted, nextTick, computed } from "vue";

gsap.registerPlugin(ScrollTrigger, MotionPathPlugin);
ScrollTrigger.defaults({
  scroller: ".wrapper",
});

const pageHeightStyle = computed(() => ({
  "--page-height": `${pageHeight}px`,
}));

let ctx: gsap.Context | null = null;

function createTimeline() {
  ctx?.revert();

  ctx = gsap.context(() => {
    const box = document.querySelector(".moving-box") as HTMLElement;
    const layer = document.querySelector(".marker-layer") as HTMLElement;
    if (!box || !layer) return;

    gsap.set(box, { x: 0, y: 0 });

    const layerRect = layer.getBoundingClientRect();

    const startRect = box.getBoundingClientRect();
    const start = {
      x: startRect.left + startRect.width / 2 - layerRect.left,
      y: startRect.top + startRect.height / 2 - layerRect.top,
    };

    const containers = gsap.utils.toArray<HTMLElement>(
      ".marker-container:not(.initial)",
    );

    const points = containers.map((container) => {
      const r = container.getBoundingClientRect();
      const target = {
        x: r.left + r.width / 2 - layerRect.left,
        y: r.top + r.height / 2 - layerRect.top,
      };

      return {
        x: target.x - start.x,
        y: target.y - start.y,
      };
    });

    gsap
      .timeline({
        scrollTrigger: {
          trigger: ".marker-layer",
          start: "top top",
          end: "bottom bottom",
          scrub: 1,
          invalidateOnRefresh: true,
        },
      })
      .to(
        box,
        {
          ease: "none",
          motionPath: { path: points, curviness: 1.5 },
        },
        0,
      )
      .to(
        box,
        {
          ease: "none",
          rotation: 1080,
          transformOrigin: "50% 50%",
        },
        0,
      );
  });

  ScrollTrigger.refresh();
}
const pageHeight = 8000;

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

onMounted(async () => {
  await nextTick();
  createTimeline();

  window.addEventListener("resize", createTimeline);
});

onUnmounted(() => {
  window.removeEventListener("resize", createTimeline);
  ctx?.revert();
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
  background: linear-gradient(180deg, #201f3a 0%, #010b18 12%, #010b18 100%);
  position: relative;
  z-index: 2;
}

.stars-container {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 0;
  pointer-events: none;
  contain: layout style paint;
}

.space-stars-bg,
.space-clouds-bg {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  background-repeat: repeat-y;
  background-size: 100% auto;
  z-index: 0;
}

.space-stars-bg {
  background-image: url("../assets/img/images/space_stars.svg");
  z-index: 1;
}

.space-clouds-bg {
  background-image: url("../assets/img/images/space_clouds.svg");
  z-index: 1;
}

@media (max-width: 1100px) {
  .space-stars-bg,
  .space-clouds-bg {
    display: none;
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
  will-change: transform;
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
  will-change: transform;
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

  background-color: lightblue;
  z-index: 1;
  display: flex;
  justify-content: center;
  align-items: center;
}

.TracksPage {
  top: 25%;
  height: 50%;
  z-index: 2;
  display: flex;
  justify-content: center;
  align-items: center;
}

.CampGamesPage {
  bottom: 0;
  height: 33%;
  z-index: 1;
  display: flex;
  justify-content: center;
  align-items: center;
}

.marker-layer {
  position: absolute;
  inset: 0;
  height: var(--page-height);
  pointer-events: none;
  z-index: 0;
  pointer-events: none;
  contain: layout;
}

.marker-container {
  position: absolute;
  width: 140px;
  height: 140px;
  /* border: 2px dashed rgba(255, 255, 255, 0.25); */
  border-radius: 10px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.marker {
  width: 100px;
  height: 100px;
  border-radius: 10px;
  /* outline: 2px solid rgba(255, 255, 255, 0.25); */
}

.moving-box {
  width: 300px;
  height: 300px;
  border-radius: 10px;
  z-index: 10;
  will-change: transform;
  background-size: contain;
  background-repeat: no-repeat;
  background-position: center;
  background-color: transparent;
}

.initial {
  left: 85%;
  top: 3%;
}

.second {
  left: 10%;
  top: 25%;
}

.third {
  right: 10%;
  top: 45%;
}

.fourth {
  left: 20%;
  top: 65%;
}

.fifth {
  left: 60%;
  top: 80%;
}

.sixth {
  left: 15%;
  top: 95%;
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
  .marker-layer {
    visibility: hidden;
    pointer-events: none;
  }
  .transition0 {
    width: 100%;
    height: 2px;
    opacity: 40%;
    z-index: 10;
    margin-left: 10%;
    width: 80%;
  }
  .transition1 {
    height: 4vw;
  }
}

.transition1 {
  height: 4vw;
}
</style>
