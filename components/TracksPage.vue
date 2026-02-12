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
            <div class="text-area">
              <h2 class="cloud-title">{{ track.title }}</h2>
              <p class="cloud-desc">{{ track.description }}</p>
            </div>
            <div class="image-area">
              <div class="circle-placeholder">
                <img :src="track.icon" v-if="track.icon" class="icon-img" />
                <span v-else class="placeholder-text">Image</span>
              </div>
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
  min-height: auto;
  position: relative;
  overflow: hidden;
  color: white;
  display: flex;
  justify-content: center;
  align-items: center;
  padding-top: 1px;
  padding-bottom: 1px;
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

.track-cloud {
  z-index: 5;
  display: flex;
  align-items: center;
  margin-top: 6rem;
  margin-bottom: 6rem;
}

.star-border-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  object-fit: fill;
  z-index: -1;
  transform: scale(1.1);
}

.cloud-content {
  position: relative;
  display: flex;
  align-items: center;
  z-index: 2;
  width: 100%;
}

.cloud-title {
  font-family: "Aleo";
  font-size: clamp(1.4rem, 1.8vw, 2.2rem);
  margin-left: 1rem;
  margin-top: 1rem;
  font-weight: bold;
}

.cloud-desc {
  font-family: "Avenir", Helvetica, sans-serif;
  font-size: clamp(0.85rem, 1vw, 1.15rem);
  line-height: 1.25;
  margin-left: 1rem;
}

.circle-placeholder {
  width: 115px;
  height: 115px;
  background: none;
  border-radius: 50%;
  border: none;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  overflow: visible;
}

.icon-img {
  width: 160px;
  height: 160px;
  object-fit: contain;
}

.desktop-view .circle-placeholder {
  margin-top: 100px;
}

.desktop-view {
  display: block;
}

.mobile-view {
  display: none;
}

.track-cloud {
  position: absolute;
  width: 26vw;
  aspect-ratio: 2 / 1;
  height: auto;
  max-width: 450px;
  max-height: 220px;
}

.pos-0 {
  top: 12%;
  left: max(3%, 40px);
  padding: 10px;
}
.pos-1 {
  top: 2%;
  left: 50%;
  transform: translateX(-50%);
  padding: 10px;
}
.pos-2 {
  top: 12%;
  right: max(3%, 40px);
  padding: 10px;
}
.pos-3 {
  bottom: 12%;
  left: max(3%, 40px);
  padding: 10px;
}
.pos-4 {
  bottom: 2%;
  left: 50%;
  transform: translateX(-50%);
  padding: 10px;
}
.pos-5 {
  bottom: 12%;
  right: max(3%, 40px);
  padding: 10px;
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
  min-width: 0;
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
  box-sizing: border-box;
  overflow: hidden;
}

.card-inner {
  position: relative;
  z-index: 2;
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 16px;
  min-width: 0;
}

.card-text {
  flex: 1 1 0%;
  min-width: 0;
  text-align: left;
}

.card-text .cloud-title {
  font-size: 1.8rem;
  margin: 0 0 8px 0;
  margin-left: 0;
}

.card-text .cloud-desc {
  font-size: 1.1rem;
  line-height: 1.4;
  margin: 0;
  margin-left: 0;
  overflow-wrap: break-word;
  word-wrap: break-word;
}

.card-icon {
  flex: 0 0 auto;
  display: flex;
  align-items: center;
  justify-content: center;
}

.card-inner .circle-placeholder {
  width: 140px;
  height: 140px;
  border: none;
  background: transparent;
}

.card-inner .icon-img {
  width: 100%;
  height: 100%;
  object-fit: contain;
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
    min-height: auto;
    height: auto;
    padding: 40px 0 0;
    overflow: hidden;
  }

  .content-wrapper {
    width: 100%;
    max-width: 100%;
    height: auto;
    min-height: unset;
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
