<script setup lang="ts">
import { ref, computed, onUnmounted } from 'vue';

const SRC = './Teenage.mp3';

const isPlaying = ref(false);
const currentTime = ref(0);
const duration = ref(0);

const audio = new Audio(SRC);

audio.addEventListener('timeupdate', () => {
  currentTime.value = audio.currentTime;
});

audio.addEventListener('loadedmetadata', () => {
  duration.value = audio.duration;
});

audio.addEventListener('ended', () => {
  isPlaying.value = false;
  audio.currentTime = 0;
});

const pct = computed(() =>
  duration.value ? (currentTime.value / duration.value) * 100 : 0
);

function toggle() {
  if (isPlaying.value) {
    audio.pause();
    isPlaying.value = false;
  } else {
    audio.play().catch(() => { });
    isPlaying.value = true;
  }
}

function seek(e: MouseEvent) {
  if (!duration.value) return;
  const target = e.currentTarget as HTMLElement;
  const r = target.getBoundingClientRect();
  audio.currentTime = ((e.clientX - r.left) / r.width) * duration.value;
}

function fmt(s: number) {
  if (!s || isNaN(s)) return '0:00';
  return Math.floor(s / 60) + ':' + String(Math.floor(s % 60)).padStart(2, '0');
}

onUnmounted(() => audio.pause());
</script>

<template>
  <div class="player-wrapper">
    <div class="orb orb-1"></div>
    <div class="orb orb-2"></div>

    <div class="card">
      <div class="cover" :class="{ playing: isPlaying }">
        <img src="/williem.jpg" alt="The Golden Spin" class="Lesgoooo" />
      </div>

      <div class="meta">
        <h1 class="title">Tamatlah Sudah Latihan Kita</h1>
        <p class="artist">Teenage Dirtbag</p>
      </div>

      <div class="progress-wrap">
        <div class="time-row">
          <span>{{ fmt(currentTime) }}</span>
          <span>{{ fmt(duration) }}</span>
        </div>
        <div class="bar-track" @click="seek">
          <div class="bar-fill" :style="{ width: pct + '%' }"></div>
        </div>
      </div>

      <button class="play-btn" @click="toggle" aria-label="Toggle Playback">
        <svg v-if="!isPlaying" viewBox="0 0 24 24" fill="currentColor">
          <polygon points="5,3 19,12 5,21" />
        </svg>
        <svg v-else viewBox="0 0 24 24" fill="currentColor">
          <rect x="6" y="4" width="4" height="16" />
          <rect x="14" y="4" width="4" height="16" />
        </svg>
      </button>
    </div>
  </div>
</template>

<style>
html, body {
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
  background-color: #0d0d0d;
  overflow: hidden;
}

#app {
  width: 100%;
  height: 100%;
}
</style>

<style scoped>
.player-wrapper {
  min-height: 100vh;
  width: 100vw;
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: 'Nunito', sans-serif;
  /* Background uses the Purple as a subtle base */
  background: radial-gradient(circle at center, #1a1024 0%, #000000 100%);
  overflow: hidden;
  position: relative;
}

/* Gyro Themed Orbs */
.orb {
  position: fixed;
  border-radius: 50%;
  pointer-events: none;
  z-index: 0;
  filter: blur(80px);
  opacity: 0.4;
}
.orb-1 {
  width: 400px;
  height: 400px;
  background: #684583; /* Purple */
  top: -100px;
  left: -100px;
}
.orb-2 {
  width: 350px;
  height: 350px;
  background: #C5E55D; /* Lime */
  bottom: -50px;
  right: -50px;
}

.card {
  /* Dark Glassmorphism */
  background: rgba(28, 20, 36, 0.7);
  border: 1px solid rgba(197, 229, 93, 0.2);
  border-radius: 32px;
  backdrop-filter: blur(25px);
  padding: 40px;
  width: 320px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 24px;
  z-index: 1;
  box-shadow: 0 30px 60px rgba(0, 0, 0, 0.6);
}

.cover {
  width: 220px;
  height: 220px;
  border-radius: 24px;
  /* Cover gradient using Lime and Purple */
  background: linear-gradient(135deg, #684583, #C5E55D);
  padding: 4px; /* Border effect */
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 15px 35px rgba(0, 0, 0, 0.5);
  overflow: hidden;
}

.Lesgoooo {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 20px;
}

.cover.playing {
  animation: spin-vibe 4s ease-in-out infinite;
}

@keyframes spin-vibe {
  0%, 100% { transform: scale(1) rotate(0deg); }
  50% { transform: scale(1.05) rotate(2deg); }
}

.meta {
  text-align: center;
}

.title {
  font-family: 'Press Start 2P', monospace;
  font-size: 11px;
  color: #C5E55D; /* Lime Title */
  margin: 0 0 10px 0;
  text-shadow: 0 0 10px rgba(197, 229, 93, 0.3);
}

.artist {
  font-size: 14px;
  font-weight: 800;
  color: #B8C2CC; /* Steel Silver contrast */
  text-transform: uppercase;
  letter-spacing: 2px;
}

.progress-wrap {
  width: 100%;
}

.time-row {
  display: flex;
  justify-content: space-between;
  font-size: 11px;
  font-weight: 800;
  color: #684583; /* Purple Time */
  margin-bottom: 8px;
}

.bar-track {
  width: 100%;
  height: 8px;
  background: #120d1a;
  border-radius: 20px;
  cursor: pointer;
  position: relative;
  border: 1px solid rgba(197, 229, 93, 0.1);
}

.bar-fill {
  height: 100%;
  /* Gradient from Lime to a Gold contrast */
  background: linear-gradient(90deg, #C5E55D, #FACC15);
  border-radius: 20px;
  position: relative;
  pointer-events: none;
}

.bar-fill::after {
  content: '';
  position: absolute;
  right: -4px;
  top: 50%;
  transform: translateY(-50%);
  width: 14px;
  height: 14px;
  border-radius: 50%;
  background: #ffffff;
  box-shadow: 0 0 15px #C5E55D;
}

.play-btn {
  width: 68px;
  height: 68px;
  border-radius: 50%;
  border: none;
  background: #C5E55D; /* High contrast Lime */
  color: #1a1024;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  box-shadow: 0 8px 20px rgba(197, 229, 93, 0.4);
}

.play-btn:hover {
  transform: scale(1.1) rotate(15deg);
  background: #d9f27d;
}

.play-btn svg {
  width: 30px;
  height: 30px;
}
</style>