<template>
  <div class="gradient">
    <div class="stars-container">
      <div
        v-for="star in stars"
        :key="star.id"
        class="star"
        :style="{
          left: star.x + '%',
          top: star.y + '%',
          width: star.size + 'px',
          height: star.size + 'px',
          animationDelay: star.delay + 's',
          animationDuration: star.duration + 's',
        }"
      ></div>
    </div>
    <img
      src="../assets/img/images/better_landing.webp"
      class="background"
      alt="landing image"
    />
    <div class="content-wrapper">
      <div class="button-wrapper">
        <a
          target="_blank"
          href="https://register.bit.camp"
          class="register-button"
          >REGISTER</a
        >
      </div>
    </div>
    <div class="message-wrapper">
      <ExplorationMessage />
    </div>
  </div>
</template>
<script lang="ts">
export default {
  name: "LandingPage",
  components: {},
};
</script>

<script setup lang="ts">
const stars = Array.from({ length: 80 }, (_, i) => ({
  id: i,
  x: Math.random() * 100,
  y: Math.random() * 60,
  size: Math.random() * 2.5 + 1,
  delay: Math.random() * 5,
  duration: Math.random() * 3 + 2,
}));
</script>

<style scoped>
.gradient {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 80vw;
  height: auto;
  overflow: hidden;
  background: linear-gradient(180deg, #201f3a 70%, #010b18 100%);
  width: 100%;
  aspect-ratio: 16 / 9;
}

.stars-container {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 1;
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

.background {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: auto;
  z-index: 0;
  object-fit: cover;
}

.message-wrapper {
  position: absolute;
  bottom: 6%;
  left: 50%;
  transform: translateX(-50%);
  width: 100%;
  z-index: 1;
}

.button-wrapper {
  position: absolute;
  top: 48%;
  right: 38%;
  transform: translateY(-50%);
  width: auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  z-index: 1;
}

.register-button {
  background-color: #ff6f3f;
  border-radius: 5rem;
  border-style: solid;
  border-color: #e54d1a;
  color: white;
  font-family: Avenir;
  font-weight: bold;
  letter-spacing: 0.2rem;
  margin-bottom: 40%;
  cursor: pointer;
  transition: transform 0.25s ease, box-shadow 0.25s ease,
    background-color 0.25s ease;
  font-size: 2vw;
  padding: 0.03em 0.65em;
  border-width: 3px;
}

.register-button:hover {
  transform: scale(1.07);
  box-shadow: 0 0 20px rgba(255, 111, 63, 0.5);
  background-color: #ff8a5c;
}

@media (max-width: 796px) {
  .background {
    content: url("../assets/img/images/better_mobile.webp");
  }

  .register-button {
    border-radius: 5rem;
    letter-spacing: 0.25rem;
    font-size: 4vw;
    border-width: 4px;
    margin-top: 43vw;
    margin-right: 40vw;
  }

  .gradient {
    aspect-ratio: 9 / 16;
    min-height: auto;
    overflow: visible;
    display: block;
    background: linear-gradient(180deg, #201f3a 70%, #010b18 100%);
  }

  .button-wrapper {
    top: 30vw;
    left: 50%;
    right: auto;
    transform: translateX(-50%);
  }

  .message-wrapper {
    position: relative;
    height: auto;
    z-index: 1;
    margin-top: 250vw;
  }
}

@media (max-width: 500px) {
  .button-wrapper {
    width: 90%;
    max-width: 350px;
  }
}
</style>
