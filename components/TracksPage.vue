<template>
  <div id="tracks" class="tracks-page">
    <div class="stars-overlay"></div>

    <div class="content-wrapper">
      <div class="center-header">
        <h1 class="main-title">Tracks</h1>
        <p class="main-subtitle">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit.
          In mollis facilisis urna, in pellentesque nisi ultrices non.
          Duis vestibulum felis quis magna laoreet pretium.
          Aliquam ut pretium massa, a eleifend ligula. Quisque
          elementum arcu finibus vestibulum efficitur.
        </p>
      </div>

      <div class="tracks-container desktop-view">
        <div
          v-for="(track, index) in tracks"
          :key="index"
          :class="['track-cloud', `pos-${index}`]"
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

      <div class="mobile-carousel mobile-view">
        <button class="nav-btn prev" @click="prevTrack" aria-label="Previous Track">
          <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path
              d="M19 12H5M5 12L12 19M5 12L12 5"
              stroke="#e76f51"
              stroke-width="3"
              stroke-linecap="round"
              stroke-linejoin="round"
            />
          </svg>
        </button>

        <div class="track-cloud mobile-card">
          <img :src="starBorder" class="star-border-overlay" alt="" />
          <div class="cloud-content">
            <div class="text-area">
              <h2 class="cloud-title">{{ tracks[currentTrack].title }}</h2>
              <p class="cloud-desc">{{ tracks[currentTrack].description }}</p>
            </div>
            <div class="image-area">
              <div class="circle-placeholder">
                <img
                  :src="tracks[currentTrack].icon"
                  v-if="tracks[currentTrack].icon"
                  class="icon-img"
                />
                <span v-else class="placeholder-text">Image</span>
              </div>
            </div>
          </div>
        </div>

        <button class="nav-btn next" @click="nextTrack" aria-label="Next Track">
          <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path
              d="M5 12H19M19 12L12 5M19 12L12 19"
              stroke="#e76f51"
              stroke-width="3"
              stroke-linecap="round"
              stroke-linejoin="round"
            />
          </svg>
        </button>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import starBorder from "@/assets/img/star-border.png";

export default {
  name: "TracksPage",
  data() {
    return {
      currentTrack: 0,
      starBorder,
      tracks: [
        {
          title: "General Track",
          description:
            "For any and all hackers! Build the perfect hack using hardware, software, and collaboration with other tech-lovers, design thinkers, and students - all skill and experience levels are welcome!",
          icon: null,
        },
        {
          title: "Game Development",
          description:
            "Aliens—at least as we imagine them—are a mirror for our own hopes, fears, and curiosity...",
          icon: null,
        },
        {
          title: "App Development",
          description:
            "Ever wondered how to turn your innovative app idea into a reality? Ready to turn your concepts into cutting-edge applications? Join the App Dev track - we'll introduce you to different aspects of development including the software development life cycle, development tools such as Flutter, and full-stack development through access to exclusive workshops and mentors as you work on your hack!",
          icon: null,
        },
        {
          title: "Machine Learning",
          description:
            "If you are amazed by AI breakthroughs like ChatGPT and driven to create something just as impactful, then this is your track! Dive into hands-on workshops where you'll learn to build and deploy machine learning models, gain proficiency in essential ML techniques, and discuss innovations reshaping the AI landscape. By the end of this track, you’ll have a portfolio-ready project to showcase!",
          icon: null,
        },
        {
          title: "Data Science",
          description:
            "The Data Science track introduces beginners to working with data through workshops and guided mini-projects. Hackers will explore data cleaning, analysis, and visualization to discover meaning and patterns from data!",
          icon: null,
        },
        {
          title: "Quantum",
          description:
            "Hackers will delve into the field of quantum computing with exclusive mentors, sponsors, and workshops! Hackers will use their knowledge of Python and other computing skills on educational and interactive Quantum Track activities. If you've been a previous participant of the Quantum track, there will be new, challenging prompts for you to tackle!",
          icon: null,
        },
      ],
    };
  },
  methods: {
    nextTrack() {
      this.currentTrack = (this.currentTrack + 1) % this.tracks.length;
    },
    prevTrack() {
      this.currentTrack = (this.currentTrack - 1 + this.tracks.length) % this.tracks.length;
    },
  },
};
</script>

<style scoped>
/* ================= GLOBAL STYLES ================= */
.tracks-page {
  background-color: #050a14;
  min-height: 100vh;
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
  width: 98vw;
  max-width: 1600px;
  height: 90vh;
  min-height: 800px;
  z-index: 10;
  margin-top: 40px;
  margin-bottom: 40px;
}

.center-header {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  text-align: center;
  width: clamp(400px, 50vw, 800px);
  z-index: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.main-title {
  font-family: "serif";
  font-size: clamp(4rem, 8vw, 7.5rem);
  margin: 0;
  line-height: 1;
  text-shadow: 0 0 30px rgba(255, 255, 255, 0.4);
  white-space: nowrap;
}

.main-subtitle {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  font-size: clamp(1.2rem, 1.8vw, 1.6rem);
  line-height: 1.6;
  margin-top: 20px;
  max-width: 600px;
  opacity: 0.9;
}

/* ================= SHARED CARD STYLES ================= */
.track-cloud {
  background: transparent;
  padding: 30px;
  z-index: 5;
  display: flex;
  align-items: center;
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
  gap: 15px;
  z-index: 2;
  width: 100%;
}

.cloud-title {
  font-family: "serif";
  font-size: 2.2rem;
  font-weight: bold;
}
.cloud-desc {
  font-family: "Avenir", Helvetica, sans-serif;
  font-size: 1.15rem;
  line-height: 1.25;
}

.circle-placeholder {
  width: 100px;
  height: 100px;
  background: rgba(255, 255, 255, 0.05);
  border-radius: 50%;
  border: 3px solid rgba(255, 255, 255, 0.6);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  overflow: hidden;
}

/* ================= DESKTOP VIEW POSITIONS ================= */
.desktop-view {
  display: block;
}
.mobile-view {
  display: none;
}

.track-cloud {
  position: absolute;
  width: clamp(300px, 22vw, 380px);
  min-height: 150px;
}

.pos-0 {
  top: 15%;
  left: 10%;
}
.pos-1 {
  top: 1%;
  left: 50%;
  transform: translateX(-50%);
}
.pos-2 {
  top: 15%;
  right: 10%;
}

.pos-3 {
  bottom: 15%;
  left: 10%;
}
.pos-4 {
  bottom: 1%;
  left: 50%;
  transform: translateX(-50%);
}
.pos-5 {
  bottom: 15%;
  right: 10%;
}

@media screen and (max-width: 1400px) and (min-width: 1201px) {
  .track-cloud {
    width: 280px;
  }
  .pos-0,
  .pos-3 {
    left: 4%;
  }
  .pos-2,
  .pos-5 {
    right: 4%;
  }
  .main-title {
    font-size: 7rem;
  }
  .main-subtitle {
    font-size: 1.7rem;
    max-width: 450px;
  }
}

/* ================= MOBILE VIEW (<= 1200px) ================= */
@media (max-width: 1200px) {
  .desktop-view { display: none; }
  .mobile-view { display: flex; }

  
  .tracks-page {
    min-height: unset;      
    height: auto;
    padding: 24px 0 16px;   
    align-items: flex-start;
    justify-content: flex-start;
  }

  .content-wrapper {
    width: 100%;
    max-width: 100%;
    height: auto;
    min-height: unset;      
    padding: 0;

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
    margin: 0 auto 20px;
  }

  
  .main-title {
    font-size: clamp(4.2rem, 9vw, 6.8rem);
    line-height: 1.05;
    white-space: normal;
  }

  .main-subtitle {
    font-size: clamp(1.35rem, 3.2vw, 2.1rem);
    line-height: 1.45;
    max-width: 62ch;
    margin: 12px auto 0;
  }

  
  .mobile-carousel {
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: clamp(14px, 3vw, 26px);
    padding: 0 14px;
  }

  
  .mobile-card {
    position: relative;
    width: min(84vw, 560px);
    aspect-ratio: 1.9 / 1;
    max-width: 560px;
    padding: clamp(28px, 3.6vw, 48px) clamp(18px, 2.8vw, 34px);
    background: rgba(30, 40, 60, 0.8);
    border-radius: 40px;
  }

  .mobile-card .cloud-title {
    font-size: clamp(2rem, 4vw, 3rem);
  }

  .mobile-card .cloud-desc {
    font-size: clamp(1.05rem, 2.4vw, 1.55rem);
    line-height: 1.35;
  }

  .mobile-card .circle-placeholder {
    width: clamp(110px, 22vw, 170px);
    height: clamp(110px, 22vw, 170px);
  }

  .nav-btn {
    background: #e3e2e0;
    border: none;
    border-radius: 50%;
    width: clamp(50px, 9vw, 70px);
    height: clamp(50px, 9vw, 70px);
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    box-shadow: 0 4px 10px rgba(0,0,0,0.3);
    flex-shrink: 0;
  }

  .nav-btn svg {
    width: clamp(26px, 4.5vw, 46px);
    height: clamp(26px, 4.5vw, 46px);
  }
}
</style>