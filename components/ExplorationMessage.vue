<template>
  <div class="exploration-container" ref="containerRef">
    <div class="exploration-message">
      <h1 class="title"><i>Bitcamp is a place for exploration.</i></h1>
      <p class="description">
        You have 36 hours to explore, learn, and create with world-class mentors
        and over 1,000 participants. Whether you're a seasoned hacker or new to
        it all, there's something for everyone.
      </p>
    </div>
  </div>
</template>
<script lang="ts">
export default {
  name: "ExplorationMessage",
};
</script>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from "vue";
import { gsap } from "gsap";
import { SplitText } from "gsap/SplitText";
import { ScrollTrigger } from "gsap/ScrollTrigger";

gsap.registerPlugin(SplitText, ScrollTrigger);

const containerRef = ref<HTMLElement | null>(null);

let titleSplit: SplitText | null = null;
let descSplit: SplitText | null = null;
let titleAnim: gsap.core.Tween | null = null;
let descAnim: gsap.core.Tween | null = null;

function setup() {
  titleAnim && titleAnim.revert();
  descAnim && descAnim.revert();
  titleSplit && titleSplit.revert();
  descSplit && descSplit.revert();

  if (!containerRef.value) return;

  const scroller = document.querySelector(".wrapper") ?? window;
  ScrollTrigger.defaults({ scroller });

  const titleEl = containerRef.value.querySelector(".title")!;
  const descEl = containerRef.value.querySelector(".description")!;

  titleSplit = SplitText.create(titleEl, { type: "chars,words,lines" });
  descSplit = SplitText.create(descEl, { type: "chars,words,lines" });

  titleAnim = gsap.from(titleSplit.lines, {
    rotationX: -100,
    transformOrigin: "50% 50% -160px",
    opacity: 0,
    duration: 0.8,
    ease: "power3",
    stagger: 0.25,
    scrollTrigger: {
      trigger: titleEl,
      start: "top 85%",
    },
  });

  descAnim = gsap.from(descSplit.lines, {
    rotationX: -100,
    transformOrigin: "50% 50% -160px",
    opacity: 0,
    duration: 0.8,
    ease: "power3",
    stagger: 0.25,
    scrollTrigger: {
      trigger: descEl,
      start: "top 90%",
    },
  });
}

onMounted(() => {
  setup();
  window.addEventListener("resize", setup);
});

onUnmounted(() => {
  window.removeEventListener("resize", setup);
  titleAnim && titleAnim.revert();
  descAnim && descAnim.revert();
  titleSplit && titleSplit.revert();
  descSplit && descSplit.revert();
});
</script>

<style scoped>
.exploration-container {
  width: 100%;
  display: flex;
  justify-content: center;
  margin-bottom: -2rem;
}

.exploration-message {
  padding: 0 2rem;
  max-width: 753px;
  width: 100%;
  box-sizing: border-box;
}

.title {
  color: #fff7eb;
  text-align: center;
  font-family: "Aleo", serif;
  font-size: 46px;
  font-style: italic;
  font-weight: 800;
  line-height: 110%;
  /* letter-spacing: 0; */
  text-shadow: 0 0 20.82px rgba(255, 249, 240, 1);
  margin-bottom: 1rem;
}

.description {
  color: #fff7eb;
  text-align: center;
  font-family: "Avenir", sans-serif;
  font-size: 24px;
  font-style: normal;
  font-weight: 400;
  line-height: 140%;
  /* letter-spacing: 0; */
  opacity: 0.9;
}

@media (max-width: 1380px) {
  .exploration-container {
    margin-bottom: -3rem;
  }
  .title {
    font-size: 36px;
  }
  .description {
    font-size: 20px;
  }
}

@media (max-width: 1380px) {
  .exploration-container {
    margin-bottom: -3rem;
  }
  .title {
    font-size: 30px;
  }
  .description {
    font-size: 18px;
  }
}

@media (max-width: 796px) {
  .exploration-message {
    max-width: 550px;
  }

  .title {
    font-size: 38px;
    line-height: 120%;
  }

  .description {
    font-size: 18px;
    line-height: 150%;
  }
}

@media (max-width: 450px) {
  .exploration-message {
    max-width: 300px;
  }
}
</style>
