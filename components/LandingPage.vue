<template>
  <div class="gradient">
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

<style scoped>
.gradient {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 80vw;
  height: auto;
  overflow: hidden;
  background: linear-gradient(
  180deg,
  #201F3A 70%,
  #060118 100%
);
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
  top: 51%;
  right: 38%;
  transform: translateY(-60%);
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
  font-family: Aleo, sans-serif;
  font-weight: bold;
  letter-spacing: 0.2rem;
  margin-bottom: 40%;
  cursor: pointer;
  transition: transform 0.2s, box-shadow 0.2s;
  font-size: 1.8vw;
  padding: 0.8vw 2.5vw;
  border-width: 0.25vw;
}

@media (max-width: 796px) {
  .background {
    content: url("../assets/img/images/better_mobile.webp");
  }

  .register-button {
    border-radius: 5rem;
    letter-spacing: 0.25rem;
    font-size: 4vw;
    border-width: 0.7vw;
    margin-top: 43vw;
    margin-right: 40vw;
  }

  .gradient {
    aspect-ratio: 9 / 16;
    background: transparent;
    min-height: auto;
    position: relative;
    overflow: visible;
    display: block;
    background: linear-gradient(180deg,#201F3A 70%,#060118 100%);
  }

  .button-wrapper {
    top: 30vw;
    left: 50%;
    right: auto;
    transform: translateX(-50%);
  }

  .message-wrapper {
    position: relative;
    /* top: auto; */
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
