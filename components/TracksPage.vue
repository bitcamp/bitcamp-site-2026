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
          <img 
            :src="starBorder" 
            class="star-border-overlay" 
            alt="" 
          />
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
            <path d="M19 12H5M5 12L12 19M5 12L12 5" stroke="#e76f51" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </button>

        <div class="track-cloud mobile-card">
          <img 
            :src="starBorder" 
            class="star-border-overlay" 
            alt="" 
          />
          <div class="cloud-content">
            <div class="text-area">
              <h2 class="cloud-title">{{ tracks[currentTrack].title }}</h2>
              <p class="cloud-desc">{{ tracks[currentTrack].description }}</p>
            </div>
            <div class="image-area">
              <div class="circle-placeholder">
                <img :src="tracks[currentTrack].icon" v-if="tracks[currentTrack].icon" class="icon-img" />
                <span v-else class="placeholder-text">Image</span>
              </div>
            </div>
          </div>
        </div>

        <button class="nav-btn next" @click="nextTrack" aria-label="Next Track">
          <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M5 12H19M19 12L12 5M19 12L12 19" stroke="#e76f51" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </button>

      </div>

    </div>
  </div>
</template>

<script lang="ts">
import quantumLogo from "@/assets/img/icons/quantum-logo.svg";
import appDevLogo from "@/assets/img/icons/appdev-logo.svg";
import cyberLogo from "@/assets/img/icons/cyber-logo.svg";
import generalLogo from "@/assets/img/icons/general-logo.svg";
import mlLogo from "@/assets/img/icons/ml-logo.svg";

import starBorder from "@/assets/img/star-border.png";

export default {
  name: "TracksPage",
  data() {
    return {
      currentTrack: 0, 
      starBorder,
      tracks: [
        {title: "Placeholder1", description: "Aliens—at least as we imagine them—are a mirror for our own hopes, fears, and curiosity...", icon: null  },
        { title: "Placeholder2", description: "Aliens—at least as we imagine them—are a mirror for our own hopes, fears, and curiosity...", icon: null  },
        { title: "Placeholder3", description: "Aliens—at least as we imagine them—are a mirror for our own hopes, fears, and curiosity...", icon: null },
        { title: "Placeholder4", description: "Aliens—at least as we imagine them—are a mirror for our own hopes, fears, and curiosity...", icon: null  },
        { title: "Placeholder5", description: "Aliens—at least as we imagine them—are a mirror for our own hopes, fears, and curiosity...", icon: null  },
        { title: "Placeholder6", description: "Aliens—at least as we imagine them—are a mirror for our own hopes, fears, and curiosity...", icon: null },
      ],
    };
  },
  methods: {
    nextTrack() {
      this.currentTrack = (this.currentTrack + 1) % this.tracks.length;
    },
    prevTrack() {
      this.currentTrack = (this.currentTrack - 1 + this.tracks.length) % this.tracks.length;
    }
  }
};
</script>

<style scoped>
/* ================= GLOBAL STYLES ================= */
.tracks-page {
  background-color: #050a14;
  min-height: 90vh;
  position: relative;
  overflow: hidden;
  color: white;
  font-family: 'serif';
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 0;
}

.content-wrapper {
  position: relative;
  width: 98vw;
  max-width: 100%; 
  height: 75vh; 
  min-height: 700px;
  z-index: 10;
}

.center-header {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  text-align: center;
  width: 600px; 
  z-index: 20;
}

.main-title {
  font-size: 6rem;
  margin: 0;
  text-shadow: 0 0 30px rgba(255, 255, 255, 0.5);
  font-weight: bold;
}

/* BIGGER PARAGRAPH BELOW TRACKS */
.main-subtitle {
  font-size: 1.4rem; 
  line-height: 1.6;
  opacity: 1;
  margin-top: 15px;
  text-shadow: 0 0 10px rgba(0,0,0,0.5);
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
  pointer-events: none;
  object-fit: fill; 
  z-index: -1;
}

.cloud-content {
  position: relative;
  display: flex;
  align-items: center;
  gap: 15px;
  z-index: 2;
  width: 100%;
}

.text-area { flex: 1; }

.cloud-title { 
  font-size: 2.4rem; 
  margin-bottom: 8px; 
  font-weight: bold; 
  line-height: 1.1;
  text-shadow: 0 0 10px rgba(255, 255, 255, 0.3);
}

/* BIGGER PARAGRAPH INSIDE TRACKS */
.cloud-desc { 
  font-size: 1.5rem; 
  line-height: 1.2; 
  opacity: 1; 
  font-weight: 500;
}

.circle-placeholder {
  width: 110px; 
  height: 110px;
  background: rgba(255, 255, 255, 0.05);
  border-radius: 50%;
  border: 3px solid rgba(255, 255, 255, 0.6);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  box-shadow: 0 0 15px rgba(255, 255, 255, 0.1);
  overflow: hidden;
}

.icon-img { width: 85%; height: 85%; object-fit: contain; }

/* ================= DESKTOP SPECIFIC ================= */
.desktop-view { display: block; }
.mobile-view { display: none; }

.track-cloud {
  position: absolute; 
  width: 380px; 
  min-height: 150px;
}

/* CHANGED: Specifically targeting desktop view borders to make them smaller 
   and fit tighter around the content.
*/
.desktop-view .star-border-overlay {
  top: -20px;       /* Reduced from -50px */
  left: -15px;      /* Reduced from -20px */
  width: calc(100% + 30px);   /* Reduced from +40px */
  height: calc(100% + 40px);  /* Reduced from +100px */
}

/* Screen Fill Positioning */
.pos-1 { top: 2%; left: 50%; transform: translateX(-50%); }
.pos-4 { bottom: 2%; left: 50%; transform: translateX(-50%); }
.pos-0 { top: 15%; left: 2%; }
.pos-2 { top: 15%; right: 2%; }
.pos-3 { bottom: 15%; left: 2%; }
.pos-5 { bottom: 15%; right: 2%; }


/* ================= MOBILE RESPONSIVE ================= */
@media (max-width: 1200px) {
  .desktop-view { display: none; }
  .mobile-view { display: flex; }

  .tracks-page {
    height: auto;
    min-height: auto;
    padding: 0;
    align-items: flex-start;
    overflow-y: visible;
  }

  .content-wrapper {
    height: auto;
    min-height: auto;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 30px 0;
  }

  .center-header {
    position: relative;
    top: auto;
    left: auto;
    transform: none;
    width: 90%;
    margin-bottom: 15px;
  }

  .main-title { font-size: 3.5rem; }
  
  .main-subtitle { 
    font-size: 1.5rem; 
    text-decoration: underline; 
    text-decoration-color: rgba(255,255,255,0.3);
  }

  .mobile-carousel {
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 10px;
    margin-top: 0; 
    position: relative;
  }

  .nav-btn {
    background: #FFE4B5;
    border: none;
    border-radius: 50%;
    width: 45px;
    height: 45px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    box-shadow: 0 4px 10px rgba(0,0,0,0.3);
    z-index: 20;
    flex-shrink: 0;
  }
  
  .nav-btn svg {
    width: 20px;
    height: 20px;
  }

  .mobile-card {
    position: relative;
    width: 70%;
    max-width: 380px; 
    margin: 0 10px;
    min-height: 180px; 
    padding: 30px 20px; 
    background: rgba(30, 40, 60, 0.95); 
    border-radius: 40px;
  }

  /* Keep mobile border size as originally designed */
  .mobile-card .star-border-overlay {
    top: -20px;
    left: -20px;
    width: calc(100% + 40px);
    height: calc(100% + 40px);
  }

  .cloud-title { font-size: 1.9rem; }
  .cloud-desc { font-size: 1.3rem; }
  
  .cloud-content {
    flex-direction: row; 
    text-align: left;
  }

  .circle-placeholder {
    width: 90px;
    height: 90px;
  }
}
</style>