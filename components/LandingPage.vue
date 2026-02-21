<template>
  <div class="gradient">
    <img
      src="../assets/img/images/hero_space.svg"
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
  background: transparent;
  width: 100%;
  aspect-ratio: 16 / 9;
}


.background {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: auto;
  z-index: 0;
  mask-image: linear-gradient(to bottom, black 55%, transparent 100%);
  -webkit-mask-image: linear-gradient(to bottom, black 55%, transparent 100%);
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
  font-size: 1.7vw;
  padding: 0.3em 0.9em;
  border-width: 3px;
  animation: button-enter 0.7s cubic-bezier(0.34, 1.56, 0.64, 1) 0.4s both;
}

@keyframes button-enter {
  from {
    opacity: 0;
    transform: scale(0.75) translateY(0.5em);
  }
  to {
    opacity: 1;
    transform: scale(1) translateY(0);
  }
}

.register-button:hover {
  transform: scale(1.07);
  box-shadow: 0 0 20px rgba(255, 111, 63, 0.5);
  background-color: #ff8a5c;
}

@media (max-width: 796px) {
  .background {
    content: url("../assets/img/images/hero_space_mobile.svg");
  }

  .register-button {
    border-radius: 5rem;
    padding: 0.1em 0.9em;
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
