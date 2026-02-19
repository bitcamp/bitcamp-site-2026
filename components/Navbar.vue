<template>
  <header>
    <nav>
      <div class="non-pages">
        <div class="hamburgerContainer">
          <button
            class="hamburger hamburger--spin"
            type="button"
            style="color: #ffffff"
            :class="{ 'is-active': showDropdown }"
            @click="toggleDropdown"
          >
            <span class="hamburger-box">
              <span class="hamburger-inner"></span>
            </span>
          </button>
        </div>
      </div>

      <ul v-if="showDropdown || bigScreen" class="nav-pages">
        <li class="page">
          <a
            href="#tracks"
            class="page-type"
            @click.prevent="scrollTo('tracks')"
            >Tracks</a
          >
        </li>

        <li class="page">
          <a
            href="#campfire-games"
            class="page-type"
            @click.prevent="scrollTo('campfire-games')"
            >Campfire Games</a
          >
        </li>
        <li class="page">
          <a
            href="#roster"
            class="page-type"
            @click.prevent="scrollTo('roster')"
            >Our Team</a
          >
        </li>

        <li v-if="bigScreen" class="page page-logo">
          <a href="/">
            <img
              id="logo-with-text"
              src="~/public/bitcamp-brand/logos/logotype.png"
            />
            <!-- <img id="logo-image" src="~/public/bitcamp-brand/logos/bitcamp.png" /> -->
          </a>
        </li>

        <li class="page">
          <a
            href="#schedule"
            class="page-type"
            @click.prevent="scrollTo('schedule')"
            >Schedule</a
          >
        </li>
        <li class="page">
          <a href="#faq" class="page-type" @click.prevent="scrollTo('faq')"
            >FAQ</a
          >
        </li>
        <li class="page">
          <a
            href="#sponsors"
            class="page-type"
            @click.prevent="scrollTo('sponsors')"
            >Sponsors</a
          >
        </li>

        <li v-if="!bigScreen" class="page mobile-socials">
          <div class="socials-row">
            <a
              href="https://instagram.com/bitcamp"
              target="_blank"
              aria-label="Instagram"
            >
              <img
                src="../assets/img/icons/tabler-icon-brand-instagram.svg"
                alt=""
              />
            </a>

            <a
              href="https://www.tiktok.com/@bitcamp_umd"
              target="_blank"
              aria-label="TikTok"
            >
              <img
                src="../assets/img/icons/tabler-icon-brand-tiktok.svg"
                alt=""
              />
            </a>

            <a href="https://x.com/bitcmp" target="_blank" aria-label="X">
              <img src="../assets/img/icons/tabler-icon-brand-x.svg" alt="" />
            </a>

            <a
              href="https://www.facebook.com/bitcmp"
              target="_blank"
              aria-label="Facebook"
            >
              <img
                src="../assets/img/icons/tabler-icon-brand-facebook.svg"
                alt=""
              />
            </a>
          </div>
        </li>

        <template v-if="bigScreen">
          <a
            id="mlh-trust-badge"
            style="
              display: block;
              height: 32px;
              width: 32px;
              max-width: 100px;
              min-width: 60px;
              width: 10%;
              top: -8px;
              margin-top: -1.5rem;
              position: absolute;
              right: -5vw;
            "
            href="https://mlh.io/na?utm_source=na-hackathon&utm_medium=TrustBadge&utm_campaign=2026-season&utm_content=white"
            target="_blank"
          >
            <img
              src="https://s3.amazonaws.com/logged-assets/trust-badge/2026/mlh-trust-badge-2026-white.svg"
              alt="Major League Hacking 2025 Hackathon Season"
              style="width: 100%"
            />
          </a>
        </template>
      </ul>
    </nav>
  </header>

  <div
    v-if="showDropdown && !bigScreen"
    class="mobile-nav-bg"
    aria-hidden="true"
  ></div>
  <div
    v-if="showDropdown && !bigScreen"
    class="mobile-nav-mountains"
    aria-hidden="true"
  ></div>

  <div>
    <slot />
  </div>
</template>

<script lang="ts">
export default {
  name: "NavbarComponent",
};
</script>

<script setup lang="ts">
import { ref, onMounted } from "vue";

const showDropdown = ref(false);
const bigScreen = ref(false);

onMounted(() => {
  const startSize = window.innerWidth;
  if (startSize > 1200) {
    bigScreen.value = true;
  } else {
    bigScreen.value = false;
  }
  window.addEventListener("resize", onresize);
  window.addEventListener("scroll", setColorAndOpacity);
});

onUnmounted(() => {
  window.removeEventListener("resize", onresize);
  window.removeEventListener("scroll", setColorAndOpacity);
});

function onresize() {
  const screenSize = window.innerWidth;

  if (screenSize <= 1200) {
    bigScreen.value = false;
  } else {
    bigScreen.value = true;
    showDropdown.value = false;
  }

  setColorAndOpacity();
}

function setColorAndOpacity() {
  var header = document.getElementsByTagName("header")[0];
}

function scrollTo(id: string) {
  const target = document.getElementById(id);
  if (!target) return;

  const wrapper = document.querySelector(".wrapper") as HTMLElement | null;
  if (wrapper) {
    const targetTop = target.getBoundingClientRect().top + wrapper.scrollTop;
    wrapper.scrollTo({ top: targetTop, behavior: "smooth" });
  } else {
    target.scrollIntoView({ behavior: "smooth" });
  }

  showDropdown.value = false;
}

function toggleDropdown() {
  showDropdown.value = !showDropdown.value;
  setColorAndOpacity();
}
</script>

<style scoped lang="scss">
header {
  z-index: 100000;
  position: fixed;
  border: 0;
  width: 90%;
  left: 45%;
  transform: translateX(-50%);
  background-color: transparent;
  border-radius: 50px;
  margin-top: 30px;
  padding: 0 2vw;

  &::before {
    content: "";
    position: absolute;
    top: -30px;
    left: -50vw;
    width: 200vw;
    height: calc(100% + 30px);
    background-color: #010b18;
    z-index: -1;
  }
}

nav {
  position: relative;
  margin-top: -1em;
  font-family: Aleo;
}

#logo-with-text {
  height: 42px;
  object-fit: cover;
  margin-left: 0;
}

.page-type {
  color: #ffffffb2;
  font-family: Aleo;
  font-size: 1.4vw;
  font-style: normal;
  font-weight: 700;
  line-height: normal;
  white-space: nowrap;
}

.page-type:hover {
  color: darkorange;
}

.nav-pages {
  display: flex;
  margin-left: 0;
  flex-direction: row;
  justify-content: space-evenly;
  align-items: center;
  width: 100%;
}

.nav-pages li {
  display: flex;
  align-items: center;
  text-decoration: none !important;
  z-index: 3;

  &.page {
    margin-top: 4px;
  }
}

.nav-pages li a {
  text-decoration: none;
  font-size: 1.4vw;
  color: #d3d3d3;
}

.hamburgerContainer {
  display: none;
}

@media screen and (max-width: 1200px) {
  header {
    padding: 1.5%;
    width: 95%;
    left: 50%;

    &::before {
      display: none;
    }
  }

  nav {
    display: flex;
    flex-direction: column;
    align-self: flex-start;
    margin: 0;
  }

  #logo-with-text {
    display: none;
    position: relative;
  }

  .nav-pages {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    padding: 6vh 5vw 5vw 6vw;
    background: transparent;
    z-index: 100001;
    row-gap: 2.2rem;
  }

  .nav-pages li {
    margin: 0;
    width: auto;
  }

  .nav-pages li a {
    font-size: 3rem;
    font-weight: 600;
    display: block;
    width: 100%;
    text-align: left;
  }

  .hamburgerContainer {
    position: relative;
    display: flex;
    margin-right: 1vw;
    align-items: flex-end;
    flex-direction: column;
  }

  .mobile-nav-bg {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background-image: url("../assets/img/images/navbar_mv_bg.webp");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
    z-index: 99999;
  }

  .mobile-nav-mountains {
    position: fixed;
    bottom: -260px;
    left: 0;
    width: 100vw;
    height: 100vh;
    background-image: url("../assets/img/images/mountains_navbar.svg");
    background-size: contain;
    background-position: bottom center;
    background-repeat: no-repeat;
    z-index: 100000;
    pointer-events: none;
  }

  .hamburger {
    padding: 25px 15px;
    display: inline-block;
    cursor: pointer;
    transition-property: opacity, filter;
    transition-duration: 0.15s;
    transition-timing-function: linear;
    font: inherit;
    color: inherit;
    text-transform: none;
    background-color: transparent;
    border: 0;
    margin: 0;
    overflow: visible;
    position: relative;
    z-index: 100002;
  }

  .hamburger:hover {
    opacity: 0.7;
  }

  .hamburger.is-active:hover {
    opacity: 0.7;
  }

  .hamburger.is-active .hamburger-inner,
  .hamburger.is-active .hamburger-inner::before,
  .hamburger.is-active .hamburger-inner::after {
    background-color: #d3d3d3;
  }

  .hamburger-box {
    width: 40px;
    height: 24px;
    display: inline-block;
    position: relative;
  }

  .hamburger-inner {
    display: block;
    top: 50%;
    margin-top: -2px;
  }

  .hamburger-inner,
  .hamburger-inner::before,
  .hamburger-inner::after {
    width: 40px;
    height: 4px;
    background-color: #ffffff;
    border-radius: 4px;
    position: absolute;
    transition-property: transform;
    transition-duration: 0.15s;
    transition-timing-function: ease;
    box-shadow: 0 0 0 1.5px #000000;
  }

  .hamburger-inner::before,
  .hamburger-inner::after {
    content: "";
    display: block;
  }

  .hamburger-inner::before {
    top: -10px;
  }

  .hamburger-inner::after {
    bottom: -10px;
  }

  .hamburger--spin .hamburger-inner {
    transition-duration: 0.22s;
    transition-timing-function: cubic-bezier(0.55, 0.055, 0.675, 0.19);
  }

  .hamburger--spin .hamburger-inner::before {
    transition: top 0.1s 0.25s ease-in, opacity 0.1s ease-in;
  }

  .hamburger--spin .hamburger-inner::after {
    transition: bottom 0.1s 0.25s ease-in,
      transform 0.22s cubic-bezier(0.55, 0.055, 0.675, 0.19);
  }

  .hamburger--spin.is-active .hamburger-inner {
    transform: rotate(225deg);
    transition-delay: 0.12s;
    transition-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
  }

  .hamburger--spin.is-active .hamburger-inner::before {
    top: 0;
    opacity: 0;
    transition: top 0.1s ease-out, opacity 0.1s 0.12s ease-out;
  }

  .hamburger--spin.is-active .hamburger-inner::after {
    bottom: 0;
    transform: rotate(-90deg);
    transition: bottom 0.1s ease-out,
      transform 0.22s 0.12s cubic-bezier(0.215, 0.61, 0.355, 1);
  }
  .mobile-socials {
    padding-top: 0;
  }

  .socials-row {
    display: flex;
    gap: 2.4rem;
    align-items: center;
    justify-content: flex-start;
  }

  .socials-row img {
    width: 42px;
    height: 42px;
    opacity: 0.85;
    transition: transform 0.2s ease, opacity 0.2s ease;
  }

  .socials-row a:hover img {
    transform: translateY(-2px);
  }
}

@media screen and (max-width: 1050px) {
  .mobile-nav-mountains {
    bottom: 0;
  }
  .nav-pages li a {
    font-size: 4rem;
  }
  .mobile-socials {
    padding-top: 6px;
  }
  .socials-row img {
    width: 60px;
    height: 60px;
  }
}

@media screen and (max-width: 900px) {
  .mobile-nav-mountains {
    bottom: 0;
  }
}

@media screen and (max-width: 840px) {
  .mobile-nav-mountains {
    bottom: -90px;
  }
  .mobile-socials {
    padding-top: 0;
  }
  .socials-row img {
    width: 50px;
    height: 50px;
  }
}

@media screen and (max-width: 740px) {
  .mobile-nav-mountains {
    bottom: -70px;
  }
}

@media screen and (max-width: 600px) {
  .mobile-nav-mountains {
    bottom: -50px;
  }
  .nav-pages li a {
    font-size: 3.5rem;
  }
  .mobile-socials {
    padding-top: 1rem;
  }
}

@media screen and (max-width: 450px) {
  .mobile-nav-mountains {
    bottom: 0;
  }
  .nav-pages li a {
    font-size: 4rem;
  }
  .mobile-socials {
    padding-top: 2rem;
  }
  .socials-row img {
    width: 35px;
    height: 35px;
  }
}
</style>
