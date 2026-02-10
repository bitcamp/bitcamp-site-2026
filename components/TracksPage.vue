<template>
  <div id="tracks" class="tracks-page">
    <div class="stars-overlay"></div>

    <div class="content-wrapper">
      <div class="center-header">
        <h1 class="main-title">Tracks</h1>
        <p class="main-subtitle">
          Discover more with tracks at Bitcamp! Dive deep into a topic or expand your horizons across many!
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
            
            <div class="text-area">
              <h2 class="cloud-title">{{ tracks[currentTrack].title }}</h2>
              <p class="cloud-desc">{{ tracks[currentTrack].description }}</p>
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
          description: "For any and all hackers! Build the perfect hack using hardware, software, and collaboration with other tech-lovers, design thinkers, and students - all skill and experience levels are welcome!",
          icon: "/_nuxt/assets/img/icons/general_logo.svg",
        },
        {
          title: "Game Development",
          description:
            "Ever wanted to make a game in a weekend? Join the Game Dev track! Build a game around a surprise theme using any tools or engines you like, attend optional beginner-friendly workshops, collaborate with others, and showcase your creativity by the end of the hackathon!",
          icon: "/_nuxt/assets/img/icons/gamedev_logo.svg",
        },
        {
          title: "App Development",
          description: "Ever wondered how to turn your innovative app idea into a reality? Ready to turn your concepts into cutting-edge applications? Join the App Dev track - we'll introduce you to different aspects of development including the software development life cycle, development tools such as Flutter, and full-stack development through access to exclusive workshops and mentors as you work on your hack!",
          icon: "/_nuxt/assets/img/icons/appdev_logo.svg",
        },
        {
          title: "Machine Learning",
          description: "If you are amazed by AI breakthroughs like ChatGPT and driven to create something just as impactful, then this is your track! Dive into hands-on workshops where you'll learn to build and deploy machine learning models, gain proficiency in essential ML techniques, and discuss innovations reshaping the AI landscape. By the end of this track, you’ll have a portfolio-ready project to showcase!",
          icon: "/_nuxt/assets/img/icons/ml_logo.svg",
        },
        {
          title: "Data Science",
          description: "The Data Science track introduces beginners to working with data through workshops and guided mini-projects. Hackers will explore data cleaning, analysis, and visualization to discover meaning and patterns from data!",
          icon: "/_nuxt/assets/img/icons/datasci_logo.svg",
        },
        {
          title: "Quantum",
          description: "Hackers will delve into the field of quantum computing with exclusive mentors, sponsors, and workshops! Hackers will use their knowledge of Python and other computing skills on educational and interactive Quantum Track activities. If you've been a previous participant of the Quantum track, there will be new, challenging prompts for you to tackle!",
          icon: "/_nuxt/assets/img/icons/quantum_logo.svg",
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

/* ================= SHARED CARD STYLES ================= */
.track-cloud {
  background: transparent;
  padding: 2vw;
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

/* Default Desktop flex behavior */
.cloud-content {
  position: relative;
  display: flex;
  align-items: center;
  gap: 1.5vw;
  z-index: 2;
  width: 100%;
}

.cloud-title {
  font-family: "Aleo";
  font-size: clamp(1.1rem, 1.4vw, 1.8rem);
  font-weight: bold;
}
.cloud-desc {
  font-family: "Avenir", Helvetica, sans-serif;
  font-size: clamp(.75rem, .85vw, 1.2rem);
  line-height: 1.25;
}

.circle-placeholder {
  width: clamp(100px, 4.5vw, 100px);
  height: clamp(100px, 4.5vw, 100px);
  background: rgba(255, 255, 255, 0.05);
  border-radius: 50%;
  border: 4px solid rgb(255, 255, 255);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  overflow: hidden;
  
}

.desktop-view .circle-placeholder{
 margin-top: 100px; 
}

/* ================= DESKTOP VIEW POSITIONS ================= */
.desktop-view { display: block; }
.mobile-view { display: none; }

.track-cloud {
  position: absolute;
  width: 22vw;
  aspect-ratio: 2 / 1;
  height: auto;
  max-width: 380px;
  max-height: 180px;
}

.pos-0 { top: 12%; left: max(3%, 40px); }
.pos-1 { top: 2%; left: 50%; transform: translateX(-50%); }
.pos-2 { top: 12%; right: max(3%, 40px); }

.pos-3 { bottom: 12%; left: max(3%, 40px); }
.pos-4 { bottom: 2%; left: 50%; transform: translateX(-50%); }
.pos-5 { bottom: 12%; right: max(3%, 40px); }

/* ================= MOBILE VIEW (<= 1200px) ================= */
@media (max-width: 1200px) {
  .desktop-view { display: none; }
  .mobile-view { display: flex; }

  .tracks-page {
    min-height: auto;
    height: auto;
    padding: 40px 0 60px;
    align-items: center;
    justify-content: center;
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
    font-size: clamp(1rem, 3vw, 1.7rem);
    margin-top: 12px;
  }

  .mobile-carousel {
    --pad: 12px;
    --gap: clamp(10px, 3vw, 16px);
    --btn: clamp(42px, 12vw, 58px);

    width: 100%;
    display: grid;
    grid-template-columns: var(--btn) auto var(--btn);
    column-gap: var(--gap);
    align-items: center;
    padding: 0 var(--pad);
    box-sizing: border-box;
    margin: 0 auto;
    justify-content: center;
  }

  .nav-btn {
    background: #e3e2e0;
    border: none;
    border-radius: 50%;
    width: var(--btn);
    height: var(--btn);
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    box-shadow: 0 4px 10px rgba(0,0,0,0.3);
    z-index: 10;
  }

  .nav-btn.prev { justify-self: start; margin-left: 7px; }
  .nav-btn.next { justify-self: end; margin-right: 7px; }
  .nav-btn svg { width: 60%; height: 60%; }

  /* ================= MOBILE CARD FIXES ================= */

  .mobile-card {
    position: relative;
    justify-self: center;
    width: min(420px, calc(100vw - (2 * var(--pad) + 2 * var(--btn) + 2 * var(--gap))));
    padding: clamp(16px, 3.6vw, 24px);
    background: rgba(30, 40, 60, 0.8);
    border-radius: 32px;
    overflow: hidden;

    
    display: block !important;
    height: auto !important;
    aspect-ratio: unset !important;
    max-height: none !important;
  }

  .mobile-card .cloud-content {
   
    display: flex !important;
    flex-direction: row;
    align-items: flex-start;
    gap: 12px;
    position: static;
    padding: 0;
  }

  .mobile-card .image-area {
    
    position: absolute;
    right: clamp(8px, 3.5vw, 18px);
    bottom: clamp(5px, 3vw, 12px);
    margin: 0;
    width: clamp(75px, 22vw, 250px);
    height: clamp(75, 22vw, 250px);
    display: block;
    z-index: 5;
    order: 2;
    
  }

  
  .mobile-card .circle-placeholder {
    width: 100%;
    height: 100%;
    border: none;
    background: transparent;
  }

  .mobile-card .icon-img {
    width: 100%;
    height: 100%;
    object-fit: contain;
  }

  
  .mobile-card .text-area {
    display: block; 
    flex: 1 1 70%;
    width: 70%;
    padding: 0;
    order: 1;
    
    padding-right: clamp(90px, 28vw, 150px);
  }

  .mobile-card .cloud-title {
    font-size: clamp(1.2rem, 5vw, 1.8rem);
    line-height: 1.1;
    margin: 0 0 8px 0;
  }

  .mobile-card .cloud-desc {
    font-size: clamp(0.85rem, 3.5vw, 1.1rem);
    line-height: 1.35;
    margin: 0;
    hyphens: auto;
    
    overflow-wrap: anywhere; 
  }
  
  
  .mobile-card .cloud-content::after {
    content: "";
    display: block;
    clear: both;
  }
}


@media (max-width: 1200px) {
  
  .mobile-card .text-area {
    width: 70% !important;
    flex: 1 1 70% !important;
    box-sizing: border-box;
  }

  .mobile-card .image-area {
    width: 30% !important;
    flex: 0 0 30% !important;
    box-sizing: border-box;
    margin: 0 0 0 8px;
  }
}
</style>