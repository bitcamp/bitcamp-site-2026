<template>
  <div id="tracks" class="tracks-page">
    <div class="stars-overlay"></div>

    <div class="content-wrapper">
      <div class="center-header">
        <h1 class="main-title">Tracks</h1>
        <p class="main-subtitle">
          Discover more with tracks at Bitcamp! Dive deep into a topic or expand
          your horizons across many!
        </p>
      </div>

      <div class="tracks-container desktop-view">
        <div
          v-for="(track, index) in tracks"
          :key="track.title"
          class="track-cloud"
          :class="'pos-' + index"
          :style="positionMargin(index)"
        >
          <img :src="starBorder" class="star-border-overlay" alt="" />
          <div class="cloud-content">
            <div class="icon-area">
              <div class="circle-placeholder">
                <img :src="track.icon" v-if="track.icon" class="icon-img" />
                <span v-else class="placeholder-text">Image</span>
              </div>
            </div>
            <div class="text-area">
              <h2 class="cloud-title">{{ track.title }}</h2>
              <p class="cloud-desc">{{ track.description }}</p>
            </div>
          </div>
        </div>
      </div>

      <div class="track-carousel mobile-view">
        <div class="carousel-container">
          <button class="nav-button nav-button--left" @click="prevTrack">
            <img src="assets/img/icons/left-arrow.svg" alt="Left Arrow" />
          </button>

          <div class="carousel-track" :style="trackStyle">
            <div
              v-for="(track, index) in tracks"
              :key="track.title"
              class="carousel-item"
            >
              <div class="track-card">
                <img :src="starBorder" class="star-border-overlay" alt="" />
                <div class="card-inner">
                  <div class="card-text">
                    <h2 class="cloud-title">{{ track.title }}</h2>
                    <p class="cloud-desc">{{ track.description }}</p>
                  </div>
                  <div class="card-icon">
                    <div class="circle-placeholder">
                      <img
                        :src="track.icon"
                        v-if="track.icon"
                        class="icon-img"
                      />
                      <span v-else class="placeholder-text">Image</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <button class="nav-button nav-button--right" @click="nextTrack">
            <img src="assets/img/icons/right-arrow.svg" alt="Right Arrow" />
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import gsap from "gsap";
import starBorder from "@/assets/img/star-border.png";
import generalLogo from "@/assets/img/icons/general_logo.svg";
import gamedevLogo from "@/assets/img/icons/gamedev_logo.svg";
import appdevLogo from "@/assets/img/icons/appdev_logo.svg";
import mlLogo from "@/assets/img/icons/ml_logo.svg";
import datasciLogo from "@/assets/img/icons/datasci_logo.svg";
import quantumLogo from "@/assets/img/icons/quantum_logo.svg";

export default {
  name: "TracksPage",

  data() {
    return {
      currentTrackIndex: 0,
      starBorder,
      cloudX: [] as ReturnType<typeof gsap.quickTo>[],
      cloudY: [] as ReturnType<typeof gsap.quickTo>[],
      onPointerMove: null as ((e: PointerEvent) => void) | null,
      onPointerLeave: null as (() => void) | null,
      tracks: [
        {
          title: "General Track",
          description:
            "For any and all hackers! Build the perfect hack using hardware, software, and collaboration with other tech-lovers, design thinkers, and students - all skill and experience levels are welcome!",
          icon: generalLogo,
        },
        {
          title: "Game Development",
          description:
            "Ever wanted to make a game in a weekend? Join the Game Dev track! Build a game around a surprise theme using any tools or engines you like, attend optional beginner-friendly workshops, collaborate with others, and showcase your creativity by the end of the hackathon!",
          icon: gamedevLogo,
        },
        {
          title: "App Development",
          description:
            "Ever wondered how to turn your innovative app idea into a reality? Ready to turn your concepts into cutting-edge applications? Join the App Dev track - we'll introduce you to different aspects of development including the software development life cycle, development tools such as Flutter, and full-stack development through access to exclusive workshops and mentors as you work on your hack!",
          icon: appdevLogo,
        },
        {
          title: "Machine Learning",
          description:
            "If you are amazed by AI breakthroughs like ChatGPT and driven to create something just as impactful, then this is your track! Dive into hands-on workshops where you'll learn to build and deploy machine learning models, gain proficiency in essential ML techniques, and discuss innovations reshaping the AI landscape. By the end of this track, you'll have a portfolio-ready project to showcase!",
          icon: mlLogo,
        },
        {
          title: "Data Science",
          description:
            "The Data Science track introduces beginners to working with data through workshops and guided mini-projects. Hackers will explore data cleaning, analysis, and visualization to discover meaning and patterns from data!",
          icon: datasciLogo,
        },
        {
          title: "Quantum",
          description:
            "Hackers will delve into the field of quantum computing with exclusive mentors, sponsors, and workshops! Hackers will use their knowledge of Python and other computing skills on educational and interactive Quantum Track activities. If you've been a previous participant of the Quantum track, there will be new, challenging prompts for you to tackle!",
          icon: quantumLogo,
        },
      ],
    };
  },

  mounted() {
    this.initMouseFollow();
    gsap.fromTo(
      this.$el.querySelector(".main-title"),
      { rotation: -75, y: -80, opacity: 0 },
      {
        scrollTrigger: {
          trigger: this.$el.querySelector(".center-header"),
          start: "top 85%",
          once: true,
        },
        rotation: 0,
        y: 0,
        opacity: 1,
        ease: "bounce.out",
        duration: 1.5,
      },
    );
  },

  beforeUnmount() {
    this.destroyMouseFollow();
  },

  computed: {
    trackStyle() {
      const ITEM_WIDTH = 80;
      const GAP = 4;
      const ITEM_STEP = ITEM_WIDTH + GAP;
      const LEFT_OFFSET = (100 - ITEM_WIDTH) / 2;
      const translateX = LEFT_OFFSET - this.currentTrackIndex * ITEM_STEP;
      return { transform: `translateX(${translateX}%)` };
    },
  },

  methods: {
    initMouseFollow() {
      const clouds = this.$el.querySelectorAll(".desktop-view .track-cloud");
      if (!clouds.length) return;

      clouds.forEach((cloud: HTMLElement, i: number) => {
        const qx = gsap.quickTo(cloud, "x", { duration: 0.6, ease: "power3" });
        const qy = gsap.quickTo(cloud, "y", { duration: 0.6, ease: "power3" });

        gsap.to(cloud, {
          yPercent: -5,
          duration: 1 + (i % 3) * 0.5,
          ease: "sine.inOut",
          repeat: -1,
          yoyo: true,
          delay: i * 0.3,
        });

        cloud.addEventListener("pointermove", (e: PointerEvent) => {
          const rect = cloud.getBoundingClientRect();
          const nx = (e.clientX - rect.left) / rect.width;
          const ny = (e.clientY - rect.top) / rect.height;

          qx(gsap.utils.interpolate(-20, 20, nx));
          qy(gsap.utils.interpolate(-20, 20, ny));
        });

        cloud.addEventListener("pointerleave", () => {
          qx(0);
          qy(0);
        });
      });
    },

    destroyMouseFollow() {
      const wrapper = this.$el?.querySelector(".content-wrapper");
      if (!wrapper) return;
      if (this.onPointerMove)
        wrapper.removeEventListener("pointermove", this.onPointerMove);
      if (this.onPointerLeave)
        wrapper.removeEventListener("pointerleave", this.onPointerLeave);
    },

    nextTrack() {
      this.currentTrackIndex =
        (this.currentTrackIndex + 1) % this.tracks.length;
    },
    prevTrack() {
      this.currentTrackIndex =
        (this.currentTrackIndex - 1 + this.tracks.length) % this.tracks.length;
    },
    positionMargin(index: number) {
      if (index === 0 || index === 3) return { marginLeft: "50px" };
      if (index === 2 || index === 5) return { marginRight: "50px" };
      return {};
    },
  },
};
</script>

<style scoped>
.tracks-page {
  position: relative;
  overflow-x: clip;
  color: white;
  display: flex;
  justify-content: center;
  align-items: center;
}

.content-wrapper {
  position: relative;
  width: 100%;
  max-width: 1800px;
  height: 100vh;
  z-index: 10;
  padding-inline: clamp(48px, 6vw, 120px);
}

.center-header {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  text-align: center;
  width: 30vw;
  z-index: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.main-title {
  font-family: "Aleo";
  font-size: clamp(3rem, 5vw, 6.5rem);
  margin: 0;
  line-height: 1;
  text-shadow: 0 0 30px rgba(255, 255, 255, 0.4);
  white-space: nowrap;
}

.main-subtitle {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  font-size: clamp(0.9rem, 1vw, 2rem);
  line-height: 1.5;
  margin-top: 20px;
  max-width: 500px;
  opacity: 0.9;
}

.star-border-overlay {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  object-fit: fill;
  z-index: -1;
  transform: scale(1.1);
}

.desktop-view {
  display: block;
}

.track-cloud {
  position: absolute;
  width: 26vw;
  max-width: 400px;
  z-index: 5;
  padding: 10px;
}

.cloud-content {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  z-index: 2;
  width: 100%;
}

.icon-area {
  margin-top: -50px;
}

.circle-placeholder {
  width: 90px;
  height: 90px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.icon-img {
  width: 120px;
  height: 120px;
  object-fit: contain;
}

.text-area {
  text-align: center;
  padding: 0 1rem 0.5rem;
}

.cloud-title {
  font-family: "Aleo";
  font-size: clamp(1.6rem, 2vw, 2.5rem);
  font-weight: bold;
  margin: 0.5rem 0 0.4rem;
}

.cloud-desc {
  font-family: "Avenir", Helvetica, sans-serif;
  font-size: clamp(0.9rem, 1.1vw, 1.25rem);
  line-height: 1.35;
  margin: 0;
}

.pos-0 {
  top: 12%;
  left: max(3%, 40px);
}
.pos-1 {
  top: 2%;
  left: 50%;
  transform: translateX(-50%);
}
.pos-2 {
  top: 12%;
  right: max(3%, 40px);
}
.pos-3 {
  bottom: 12%;
  left: max(3%, 40px);
}
.pos-4 {
  bottom: 2%;
  left: 50%;
  transform: translateX(-50%);
}
.pos-5 {
  bottom: 12%;
  right: max(3%, 40px);
}

.mobile-view {
  display: none;
}

.track-carousel {
  display: none;
  justify-content: center;
  align-items: center;
  width: 100%;
  overflow: hidden;
}

.carousel-container {
  overflow: hidden;
  width: 100%;
  max-width: 750px;
  margin: 0 auto;
  position: relative;
}

.carousel-track {
  display: flex;
  gap: 4%;
  transition: transform 0.5s ease;
}

.carousel-item {
  flex: 0 0 80%;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 3vmax 0;
}

.track-card {
  position: relative;
  width: 100%;
  background: rgba(30, 40, 60, 0.8);
  border-radius: 24px;
  padding: 28px;
  overflow: hidden;
}

.card-inner {
  position: relative;
  z-index: 2;
  display: flex;
  align-items: center;
  gap: 16px;
}

.card-text {
  flex: 1;
  min-width: 0;
}

.card-text .cloud-title {
  font-size: 1.8rem;
  margin: 0 0 8px;
}

.card-text .cloud-desc {
  font-size: 1.1rem;
  line-height: 1.4;
  margin: 0;
  overflow-wrap: break-word;
}

.card-icon {
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
}

.card-inner .circle-placeholder {
  width: 140px;
  height: 140px;
}

.card-inner .icon-img {
  width: 100%;
  height: 100%;
}

.nav-button {
  position: absolute;
  top: 35%;
  z-index: 2;
  border: none;
  border-radius: 50%;
  width: 8vmax;
  height: 8vmax;
  min-width: 40px;
  min-height: 40px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  background: none;
}

.nav-button img {
  width: 100%;
  height: 100%;
  transition: filter 0.15s ease, transform 0.15s ease;
}

.nav-button:active img {
  filter: drop-shadow(0 0 6px #f98f37) drop-shadow(0 0 14px #f98f37);
  transform: scale(0.85);
}

.nav-button--left {
  left: 1%;
}
.nav-button--right {
  right: 1%;
}

@media (max-width: 1400px) {
  .desktop-view {
    display: none;
  }
  .mobile-view {
    display: flex;
  }

  .tracks-page {
    padding: 40px 0 0;
  }

  .content-wrapper {
    height: auto;
    padding: 0;
    margin-top: 10px;
    margin-bottom: 20px;
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .center-header {
    position: relative;
    top: auto;
    left: auto;
    transform: none;
    width: min(92vw, 760px);
    margin: 20px auto 34px;
  }

  .main-title {
    font-size: clamp(2.6rem, 10vw, 5.5rem);
    white-space: normal;
  }

  .main-subtitle {
    font-size: clamp(1rem, 3vw, 2rem);
    margin-top: 20px;
  }
}
</style>
