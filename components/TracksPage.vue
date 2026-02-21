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

      <div class="desktop-view">
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

      <div class="mobile-view">
        <div class="mobile-grid">
          <div
            v-for="(track, index) in tracks"
            :key="track.title"
            class="mobile-card"
            :class="'mobile-card--' + index"
          >
            <img :src="starBorder" class="star-border-overlay" alt="" />
            <div class="mobile-card-content">
              <div class="mobile-card-header">
                <div class="icon-area">
                  <div class="circle-placeholder">
                    <img :src="track.icon" v-if="track.icon" class="icon-img" />
                    <span v-else class="placeholder-text">Image</span>
                  </div>
                </div>
                <div class="mobile-card-title-group">
                  <h2 class="cloud-title">{{ track.title }}</h2>
                </div>
              </div>
              <div class="mobile-card-body">
                <p class="cloud-desc">{{ track.description }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import starBorder from "@/assets/img/star-border.png";
import generalLogo from "@/assets/img/icons/general_logo.svg";
import gamedevLogo from "@/assets/img/icons/gamedev_logo.svg";
import appdevLogo from "@/assets/img/icons/appdev_logo.svg";
import mlLogo from "@/assets/img/icons/ml_logo.svg";
import datasciLogo from "@/assets/img/icons/datasci_logo.svg";
import quantumLogo from "@/assets/img/icons/quantum_logo.svg";

gsap.registerPlugin(ScrollTrigger);

export default {
  name: "TracksPage",

  data() {
    return {
      onResize: null as (() => void) | null,
      mobileCardTriggers: [] as ScrollTrigger[],
      desktopCloudTriggers: [] as ScrollTrigger[],
      desktopPopTweens: [] as gsap.core.Tween[],
      desktopPlayed: false,
      mobilePlayed: false,
      currentTrackIndex: 0,
      openTrackIndex: -1,
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

  mounted() {
    gsap.fromTo(
      this.$el.querySelector(".main-title"),
      { y: 60, opacity: 0 },
      {
        scrollTrigger: {
          trigger: this.$el.querySelector(".center-header"),
          start: "top 85%",
          once: true,
        },
        y: 0,
        opacity: 1,
        ease: "power3.out",
        duration: 1,
      },
    );

    gsap.fromTo(
      this.$el.querySelector(".main-subtitle"),
      { y: 40, opacity: 0 },
      {
        scrollTrigger: {
          trigger: this.$el.querySelector(".center-header"),
          start: "top 85%",
          once: true,
        },
        y: 0,
        opacity: 0.9,
        ease: "power3.out",
        duration: 1,
        delay: 0.2,
      },
    );

    this.setupDesktopClouds();
    this.setupMobileCards();

    this.onResize = () => {
      this.setupMobileCards();
      this.setupDesktopClouds();
    };

    window.addEventListener("resize", this.onResize);
  },

  beforeUnmount() {
    if (this.onResize) window.removeEventListener("resize", this.onResize);
    this.killMobileCards();
    this.killDesktopClouds();
  },

  methods: {
    setupDesktopClouds() {
      const isDesktop = window.matchMedia("(min-width: 797px)").matches;
      if (!isDesktop) {
        this.killDesktopClouds();
        return;
      }

      this.killDesktopClouds();

      const clouds = Array.from(
        this.$el.querySelectorAll(".desktop-view .track-cloud"),
      ) as HTMLElement[];

      if (!clouds.length) return;

      clouds.forEach((cloud, i) => {
        if (this.desktopPlayed) {
          gsap.set(cloud, { scale: 1, opacity: 1 });
          return;
        }

        gsap.set(cloud, { scale: 0, opacity: 0 });

        const tween = gsap.to(cloud, {
          scale: 1,
          opacity: 1,
          duration: 0.6,
          ease: "back.out(1.7)",
          delay: i * 0.1,
          paused: true,
          onComplete: () => {
            if (i === clouds.length - 1) this.desktopPlayed = true;
          },
        });

        const st = ScrollTrigger.create({
          trigger: this.$el.querySelector(".content-wrapper"),
          start: "top 70%",
          once: true,
          onEnter: () => tween.play(),
        });

        this.desktopPopTweens.push(tween);
        this.desktopCloudTriggers.push(st);
      });

      ScrollTrigger.refresh();
    },

    killDesktopClouds() {
      this.desktopCloudTriggers.forEach((t) => t.kill());
      this.desktopCloudTriggers = [];

      this.desktopPopTweens.forEach((t) => t.kill());
      this.desktopPopTweens = [];
    },

    setupMobileCards() {
      const isMobile = !window.matchMedia("(min-width: 797px)").matches;
      if (!isMobile) {
        this.killMobileCards();
        return;
      }

      this.killMobileCards();

      const scroller =
        (document.querySelector(".wrapper") as Element) ?? window;

      const cards = Array.from(
        this.$el.querySelectorAll(".mobile-card"),
      ) as HTMLElement[];

      if (!cards.length) return;

      cards.forEach((card) => {
        if (this.mobilePlayed) {
          gsap.set(card, { opacity: 1, y: 0 });
          return;
        }

        gsap.set(card, { opacity: 0, y: 24 });

        const tween = gsap.to(card, {
          opacity: 1,
          y: 0,
          duration: 0.55,
          ease: "power3.out",
          paused: true,
          onComplete: () => {
            this.mobilePlayed = true;
          },
        });

        const st = ScrollTrigger.create({
          trigger: card,
          scroller,
          start: "top 90%",
          once: true,
          onEnter: () => tween.play(),
        });

        this.mobileCardTriggers.push(st);
      });

      ScrollTrigger.refresh();
    },

    killMobileCards() {
      this.mobileCardTriggers.forEach((t) => t.kill());
      this.mobileCardTriggers = [];
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

.star-border-overlay {
  opacity: 0.8;
}

.content-wrapper {
  position: relative;
  width: 100%;
  max-width: 1800px;
  height: 100vh;
  z-index: 10;
  padding-inline: 5vw;
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
  font-size: 5vw;
  margin: 0;
  line-height: 1;
  text-shadow: 0 0 30px rgba(255, 255, 255, 0.4);
  white-space: nowrap;
}

.main-subtitle {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  font-size: 1.1vw;
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
  z-index: 2;
  transform: scale(1.1);
}

.desktop-view {
  display: block;
}

.track-cloud {
  background: linear-gradient(
    135deg,
    rgba(15, 20, 55, 0.7) 0%,
    rgba(8, 10, 30, 0.85) 100%
  );
  border: 1px solid rgba(100, 130, 220, 0.1);
  border-radius: 120px;
  position: absolute;
  width: 24vw;
  max-width: 380px;
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
  font-size: 1.8vw;
  font-weight: bold;
  margin: 0.5rem 0 0.4rem;
}

.cloud-desc {
  font-family: "Avenir", Helvetica, sans-serif;
  font-size: 1vw;
  line-height: 1.35;
  margin: 0;
}

.pos-0 {
  top: 15%;
  left: max(5%, 40px);
  box-shadow: 0 0 100px rgba(227, 78, 37, 0.5);
}
.pos-1 {
  top: 5%;
  left: 50%;
  transform: translateX(-50%);
  box-shadow: 0 0 100px rgba(228, 147, 47, 0.5);
}
.pos-2 {
  top: 15%;
  right: max(5%, 40px);
  box-shadow: 0 0 100px rgba(201, 51, 139, 0.5);
}
.pos-3 {
  bottom: 15%;
  left: max(5%, 40px);
  box-shadow: 0 0 100px rgba(175, 48, 186, 0.5);
}
.pos-4 {
  bottom: 5%;
  left: 50%;
  transform: translateX(-50%);
  box-shadow: 0 0 100px rgba(46, 129, 170, 0.5);
}
.pos-5 {
  bottom: 15%;
  right: max(5%, 40px);
  box-shadow: 0 0 100px rgba(50, 156, 61, 0.5);
}

.mobile-view {
  display: none;
}

.mobile-grid {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 14px;
  padding: 0 14px;
  width: 100%;
}

.mobile-card {
  background: linear-gradient(
    135deg,
    rgba(15, 20, 55, 0.7) 0%,
    rgba(8, 10, 30, 0.85) 100%
  );
  border: 1px solid rgba(100, 130, 220, 0.1);
  position: relative;
  width: 100%;
  padding: 4px;
  -webkit-tap-highlight-color: transparent;
  border-radius: 16px;
  backdrop-filter: blur(10px);
  transition: border-color 0.3s ease, box-shadow 0.3s ease, transform 0.15s ease;
}

.mobile-card:active {
  transform: scale(0.98);
}

.mobile-card .star-border-overlay {
  transform: scale(1.04);
  opacity: 0.6;
  border-radius: 16px;
}

.mobile-card-content {
  position: relative;
  z-index: 2;
  width: 100%;
}

.mobile-card-header {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 14px 12px;
}

.mobile-card .icon-area {
  margin-top: 0;
  flex-shrink: 0;
}

.mobile-card .circle-placeholder {
  width: 48px;
  height: 48px;
  background: radial-gradient(
    circle,
    rgba(255, 255, 255, 0.05) 0%,
    transparent 70%
  );
}

.mobile-card .icon-img {
  width: 58px;
  height: 58px;
  filter: drop-shadow(0 0 8px var(--card-accent));
  transition: filter 0.3s ease;
}

.mobile-card-title-group {
  flex: 1;
  min-width: 0;
}

.mobile-card .cloud-title {
  font-family: "Aleo";
  font-size: 17px;
  font-weight: bold;
  margin: 0;
  text-align: left;
  letter-spacing: 0.02em;
  text-shadow: 0 0 24px rgba(180, 200, 255, 0.12);
}

.mobile-card-orbit {
  display: flex;
  gap: 5px;
  margin-top: 6px;
  align-items: center;
}

.orbit-dot {
  width: 4px;
  height: 4px;
  border-radius: 50%;
  background: var(--card-accent);
  opacity: 0.6;
  animation: orbit-pulse 2.5s ease-in-out infinite;
}

.orbit-dot:nth-child(2) {
  opacity: 0.4;
  width: 3px;
  height: 3px;
  animation-delay: 0.4s;
}

.orbit-dot:nth-child(3) {
  opacity: 0.2;
  width: 2px;
  height: 2px;
  animation-delay: 0.8s;
}

.mobile-card-body {
  padding: 0 14px 18px;
}

.mobile-card .cloud-desc {
  font-family: "Avenir", Helvetica, sans-serif;
  font-size: 13.5px;
  line-height: 1.65;
  margin: 0;
  border-top: 1px solid rgba(100, 130, 220, 0.1);
  padding-top: 12px;
}

@media (max-width: 1400px) {
  .pos-0 {
    top: 23%;
    left: max(5%, 40px);
  }
  .pos-2 {
    top: 20%;
    right: max(5%, 40px);
  }
}

@media (max-width: 1200px) {
  .content-wrapper {
    position: relative;
    width: 100%;
    max-width: 1800px;
    height: 85vh;
    z-index: 10;
    padding-inline: 5vw;
  }

  .pos-0 {
    top: 25%;
    left: max(5%, 40px);
  }
  .pos-2 {
    top: 25%;
    right: max(5%, 40px);
  }
}

@media (max-width: 796px) {
  .desktop-view {
    display: none;
  }

  .mobile-view {
    display: flex;
    justify-content: center;
    width: 100%;
  }

  .tracks-page {
    padding: 40px 0 0;
  }

  .content-wrapper {
    height: auto;
    padding: 0;
    margin-top: 10px;
    margin-bottom: 48px;
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .center-header {
    position: relative;
    top: auto;
    left: auto;
    transform: none;
    width: 88vw;
    max-width: 760px;
    margin: 20px auto 32px;
  }

  .main-title {
    font-size: 11vw;
    white-space: normal;
    text-shadow: 0 0 40px rgba(140, 170, 255, 0.35),
      0 0 80px rgba(80, 110, 220, 0.15);
  }

  .main-subtitle {
    font-size: 14px;
    line-height: 1.55;
    margin-top: 14px;
    max-width: 300px;
    color: rgba(170, 190, 235, 0.7);
  }
}
</style>
