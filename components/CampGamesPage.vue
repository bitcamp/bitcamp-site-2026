<template>
  <div id="campfire-games" class="cfg-top">
    <div class="cfg-content">
      <picture>
        <source
          media="(max-width: 1024px)"
          srcset="assets/img/images/cfgTitleMobile.svg"
        />
        <img
          class="cfg-title"
          src="assets/img/images/cfgTitle.svg"
          alt="Campfire games title"
        />
      </picture>
      <div class="cfg-box">
        <p id="cfg-blurb-first">
          The Campfire Games are a way to learn, grow, and build with the
          Bitcamp Community. At the start of this year's event, you will join
          one of three teams based on your personality and interests—joining
          forces with hackers from around the world!
        </p>
        <p id="cfg-blurb-second">
          By winning unique challenges, attending workshops, and participating
          in mini-events, you'll rack up points for your team. At the end of
          Bitcamp, members of the winning team will receive limited edition
          Bitcamp swag.
        </p>
      </div>

      <div class="team-row-desktop">
        <img src="assets/img/images/teams.svg" alt="Teams" />
      </div>
      <div class="team-carousel">
        <div class="carousel-container">
          <button class="nav-button nav-button--left" @click="prevTeam">
            <img src="assets/img/icons/left-arrow.svg" alt="Left Arrow" />
          </button>
          <div class="carousel-track" :style="trackStyle">
            <div
              v-for="(team, index) in teams"
              :key="team.name"
              class="carousel-item"
            >
              <div class="team-stack">
                <img
                  :src="team.icon"
                  :alt="team.name + ' icon'"
                  class="team-icon"
                  :style="{ height: iconSize + 'px' }"
                />
                <img
                  :src="team.text"
                  :alt="team.name + ' text'"
                  class="team-text"
                />
              </div>
            </div>
          </div>
          <button class="nav-button nav-button--right" @click="nextTeam">
            <img src="assets/img/icons/right-arrow.svg" alt="Right Arrow" />
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import gsap from "gsap";

import redTeamIcon from "@/assets/img/images/red-marshie.svg";
import redTeamText from "@/assets/img/images/red-team-card.svg";
import greenTeamIcon from "@/assets/img/images/green-marshie.svg";
import greenTeamText from "@/assets/img/images/green-team-card.svg";
import blueTeamIcon from "@/assets/img/images/blue-marshie.svg";
import blueTeamText from "@/assets/img/images/blue-team-card.svg";

export default {
  name: "CampGamesPage",

  data() {
    return {
      currentTeamIndex: 1,
      teams: [
        { name: "Red Team", icon: redTeamIcon, text: redTeamText },
        { name: "Green Team", icon: greenTeamIcon, text: greenTeamText },
        { name: "Blue Team", icon: blueTeamIcon, text: blueTeamText },
      ],
      iconSize: 200,
    };
  },
  computed: {
    trackStyle() {
      const ITEM_WIDTH = 70; // %
      const GAP = 5; // %
      const ITEM_STEP = ITEM_WIDTH + GAP;
      const LEFT_OFFSET = (100 - ITEM_WIDTH) / 2; // 12.5

      const translateX = LEFT_OFFSET - this.currentTeamIndex * ITEM_STEP;
      return { transform: `translateX(${translateX}%)` };
    },
  },
  methods: {
    nextTeam() {
      this.currentTeamIndex = (this.currentTeamIndex + 1) % this.teams.length;
    },
    prevTeam() {
      this.currentTeamIndex =
        (this.currentTeamIndex - 1 + this.teams.length) % this.teams.length;
    },
  },
  mounted() {
    // Float animation on marshies
    const icons = this.$el.querySelectorAll(".team-icon");
    icons.forEach((icon: HTMLElement, i: number) => {
      gsap.to(icon, {
        yPercent: -8,
        duration: 1.2 + (i % 3) * 0.4,
        ease: "sine.inOut",
        repeat: -1,
        yoyo: true,
        delay: i * 0.3,
      });
    });

    // Scroll-triggered fade-in for sections
    const sections = [
      ".cfg-title",
      ".cfg-box",
      ".team-row-desktop",
      ".team-carousel",
    ];
    sections.forEach((sel) => {
      const el = this.$el.querySelector(sel);
      if (!el) return;
      gsap.fromTo(
        el,
        { y: 40, opacity: 0 },
        {
          y: 0,
          opacity: 1,
          duration: 1,
          ease: "power2.out",
          scrollTrigger: {
            trigger: el,
            start: "top 85%",
            once: true,
          },
        },
      );
    });
  },

  beforeUnmount() {
    gsap.killTweensOf(this.$el.querySelectorAll(".team-icon"));
  },
};
</script>

<style scoped>
.cfg-top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
}

.cfg-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 1rem;
  padding: 5rem 0;
}

.cfg-title {
  width: 100%;
  max-width: 60%;
}

.cfg-box {
  padding-left: 7%;
  padding-right: 50%;
}

#cfg-blurb-first,
#cfg-blurb-second {
  font-family: "Avenir";
  color: #fff7eb;
  font-size: 2.2rem;
  line-height: 150%;
  text-align: left;
  margin: 0;
}

#cfg-blurb-first {
  font-weight: 700;
}

#cfg-blurb-second {
  font-weight: 300;
  margin-top: 2rem;
}

.team-row-desktop {
  display: flex;
  justify-content: center;
  align-items: center;
}

.team-stack {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
  width: 100%;
}

.team-icon {
  width: auto;
  object-fit: contain;
}

.team-text {
  width: 100%;
  max-width: 350px;
  height: auto;
  object-fit: contain;
}

.team-carousel {
  display: none;
  justify-content: center;
  align-items: center;
}

.carousel-container {
  overflow: hidden;
  width: 100%;
  margin: 0 auto;
  position: relative;
}

.carousel-track {
  display: flex;
  gap: 5%;
  transition: transform 0.5s ease;
}

.carousel-item {
  flex: 0 0 70%;
  display: flex;
  align-items: center;
  justify-content: center;
  padding-top: 4vmax;
  padding-bottom: 4vmax;
}

.carousel-item img {
  width: 100%;
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

@media screen and (max-width: 1270px) {
  #cfg-blurb-first,
  #cfg-blurb-second {
    font-size: 16px;
  }

  .cfg-title {
    width: 125%;
  }

  .team-carousel {
    display: flex;
  }

  .team-row-desktop {
    display: none;
  }

  .team-icon {
    height: 200px !important;
  }
}

@media screen and (max-width: 1024px) {
  .cfg-top {
    display: block;
    padding: 0;
  }

  .cfg-content {
    padding-left: 0;
    align-items: flex-start;
  }

  .cfg-title {
    width: 150%;
    max-width: none;
  }

  .cfg-box {
    width: 80%;
    margin: 0 auto;
    align-items: center;
  }
}

@media screen and (max-width: 515px) {
  #cfg-blurb-first,
  #cfg-blurb-second {
    font-size: 14px;
  }

  .cfg-title {
    width: 110%;
  }
}
</style>
