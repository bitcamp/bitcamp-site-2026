<template>
  <canvas ref="canvas" class="stars-canvas"></canvas>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from "vue";

const canvas = ref<HTMLCanvasElement | null>(null);
let ctx: CanvasRenderingContext2D | null = null;
let width = 0;
let height = 0;

interface Cloud {
  x: number;
  y: number;
  radiusX: number;
  radiusY: number;
  opacity: number;
}

function drawStars() {
  if (!ctx) return;
  const count = Math.floor((width * height) / 2800);
  for (let i = 0; i < count; i++) {
    const alpha = Math.random() * 0.6 + 0.3;
    const radius = Math.random() * 1.6 + 0.3;
    ctx.beginPath();
    ctx.arc(Math.random() * width, Math.random() * height, radius, 0, Math.PI * 2);
    ctx.fillStyle = `rgba(255,255,255,${alpha.toFixed(3)})`;
    ctx.fill();
  }
}

function drawCloud(cloud: Cloud) {
  if (!ctx) return;
  ctx.save();
  ctx.translate(cloud.x, cloud.y);
  ctx.scale(1, cloud.radiusY / cloud.radiusX);
  const grad = ctx.createRadialGradient(0, 0, 0, 0, 0, cloud.radiusX);
  grad.addColorStop(0, `rgba(210, 225, 255, ${cloud.opacity})`);
  grad.addColorStop(0.35, `rgba(190, 210, 255, ${cloud.opacity * 0.6})`);
  grad.addColorStop(1, `rgba(170, 200, 255, 0)`);
  ctx.beginPath();
  ctx.arc(0, 0, cloud.radiusX, 0, Math.PI * 2);
  ctx.fillStyle = grad;
  ctx.fill();
  ctx.restore();
}

function drawClouds() {
  for (let i = 0; i < 8; i++) {
    drawCloud({
      x: Math.random() * (width + 800) - 400,
      y: Math.random() * height * 0.8,
      radiusX: Math.random() * 400 + 300,
      radiusY: Math.random() * 100 + 60,
      opacity: Math.random() * 0.12 + 0.1,
    });
  }
}

function render() {
  if (!ctx) return;
  ctx.clearRect(0, 0, width, height);
  drawStars();
  drawClouds();
}

function resize() {
  if (!canvas.value) return;
  width = window.innerWidth;
  height = window.innerHeight;
  canvas.value.width = width;
  canvas.value.height = height;
  render();
}

onMounted(() => {
  if (!canvas.value) return;
  ctx = canvas.value.getContext("2d");
  resize();
  window.addEventListener("resize", resize);
});

onUnmounted(() => {
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
