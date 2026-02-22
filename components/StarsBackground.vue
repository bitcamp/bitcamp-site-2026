<template>
  <canvas ref="canvas" class="stars-canvas"></canvas>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from "vue";

const canvas = ref<HTMLCanvasElement | null>(null);
let animationId = 0;
let ctx: CanvasRenderingContext2D | null = null;
let width = 0;
let height = 0;

interface Star {
  x: number;
  y: number;
  radius: number;
  twinkleSpeed: number;
  twinkleOffset: number;
}

interface Meteor {
  x: number;
  y: number;
  vx: number;
  vy: number;
  length: number;
  opacity: number;
}

const stars: Star[] = [];
const meteors: Meteor[] = [];
let lastMeteorTime = 0;
let nextMeteorDelay = 2500;

function initStars() {
  stars.length = 0;
  const count = Math.floor((width * height) / 2800);
  for (let i = 0; i < count; i++) {
    stars.push({
      x: Math.random() * width,
      y: Math.random() * height,
      radius: Math.random() * 1.6 + 0.3,
      twinkleSpeed: Math.random() * 0.8 + 0.3,
      twinkleOffset: Math.random() * Math.PI * 2,
    });
  }
}

function spawnMeteor() {
  const speed = Math.random() * 6 + 5;
  const angle = (Math.random() * 20 + 25) * (Math.PI / 180);
  meteors.push({
    x: Math.random() * width * 1.2,
    y: Math.random() * height * 0.4 - height * 0.1,
    vx: -Math.cos(angle) * speed,
    vy: Math.sin(angle) * speed,
    length: Math.random() * 280 + 180,
    opacity: 1,
  });
}

function draw(t: number) {
  if (!ctx) return;
  ctx.clearRect(0, 0, width, height);

  for (const s of stars) {
    const alpha =
      (Math.sin(t * s.twinkleSpeed + s.twinkleOffset) * 0.5 + 0.5) * 0.75 +
      0.15;
    ctx.beginPath();
    ctx.arc(s.x, s.y, s.radius, 0, Math.PI * 2);
    ctx.fillStyle = `rgba(255,255,255,${alpha.toFixed(3)})`;
    ctx.fill();
  }

  for (let i = meteors.length - 1; i >= 0; i--) {
    const m = meteors[i];
    const tailX = m.x - (m.vx / Math.hypot(m.vx, m.vy)) * m.length;
    const tailY = m.y - (m.vy / Math.hypot(m.vx, m.vy)) * m.length;

    const grad = ctx.createLinearGradient(m.x, m.y, tailX, tailY);
    grad.addColorStop(0, `rgba(255,255,255,${m.opacity.toFixed(3)})`);
    grad.addColorStop(0.3, `rgba(200,220,255,${(m.opacity * 0.5).toFixed(3)})`);
    grad.addColorStop(1, `rgba(180,200,255,0)`);

    ctx.beginPath();
    ctx.moveTo(m.x, m.y);
    ctx.lineTo(tailX, tailY);
    ctx.strokeStyle = grad;
    ctx.lineWidth = 3;
    ctx.stroke();

    m.x += m.vx;
    m.y += m.vy;
    m.opacity -= 0.012;

    if (m.opacity <= 0 || m.x < -m.length || m.y > height + m.length) {
      meteors.splice(i, 1);
    }
  }
}

function animate(t: number) {
  draw(t / 1000);

  if (t - lastMeteorTime > nextMeteorDelay) {
    spawnMeteor();
    lastMeteorTime = t;
    nextMeteorDelay = Math.random() * 3000 + 1500;
  }

  animationId = requestAnimationFrame(animate);
}

function resize() {
  if (!canvas.value) return;
  width = window.innerWidth;
  height = window.innerHeight;
  canvas.value.width = width;
  canvas.value.height = height;
  initStars();
}

onMounted(() => {
  if (!canvas.value) return;
  ctx = canvas.value.getContext("2d");
  resize();
  window.addEventListener("resize", resize);
  animationId = requestAnimationFrame(animate);
});

onUnmounted(() => {
  cancelAnimationFrame(animationId);
  window.removeEventListener("resize", resize);
});
</script>

<style scoped>
.stars-canvas {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  pointer-events: none;
  z-index: 1;
}
</style>
