<script setup>
import { ref, onMounted, onUnmounted } from "vue";

const items = [
  {
    id: "top",
    key: "nav.home",
    icon: "M3 11l9-8 9 8v9a1 1 0 01-1 1h-5v-6H9v6H4a1 1 0 01-1-1z",
  },
  {
    id: "features",
    key: "nav.features",
    icon: "M12 3l2.2 5.3L20 9l-4.3 3.9L17 19l-5-3-5 3 1.3-6.1L4 9l5.8-.7z",
  },
  { id: "join", key: "nav.code", icon: "M5 9h14M5 15h14M10 4L8 20M16 4l-2 16" },
  {
    id: "catalog",
    key: "nav.catalog",
    icon: "M12 21a9 9 0 100-18 9 9 0 000 18zM10 8.5l5 3.5-5 3.5z",
  },
  {
    id: "login",
    key: "nav.signin",
    icon: "M12 12a4 4 0 100-8 4 4 0 000 8zM4 21a8 8 0 0116 0",
  },
];

const active = ref("top");

// Tabni bosganda aylanish tugaguncha avtomatik aniqlashni to'xtatib turadi
let locked = false;
let timer = null;

function release() {
  locked = false;
  update();
}

function go(id) {
  active.value = id;
  locked = true;
  clearTimeout(timer);
  timer = setTimeout(release, 700); // aylanish bo'lmasa ham qulf ochiladi

  if (id === "top") {
    window.scrollTo({ top: 0, behavior: "smooth" });
    return;
  }
  document
    .getElementById(id)
    ?.scrollIntoView({ behavior: "smooth", block: "start" });
}

// Aylantirganda qaysi bo'lim ekranda ekanini aniqlaydi
function update() {
  if (window.scrollY < 120) {
    active.value = "top";
    return;
  }
  const line = window.innerHeight * 0.4;
  let best = "top";
  let bestTop = -Infinity;
  for (const it of items) {
    if (it.id === "top") continue;
    const el = document.getElementById(it.id);
    if (!el) continue;
    const t = el.getBoundingClientRect().top;
    if (t <= line && t > bestTop) {
      best = it.id;
      bestTop = t;
    }
  }
  active.value = best;
}

function onScroll() {
  if (locked) {
    // Aylanish davom etyapti: tugagach (150ms to'xtasa) qulfni ochamiz
    clearTimeout(timer);
    timer = setTimeout(release, 150);
    return;
  }
  update();
}

onMounted(() => {
  window.addEventListener("scroll", onScroll, { passive: true });
  update();
});
onUnmounted(() => {
  window.removeEventListener("scroll", onScroll);
  clearTimeout(timer);
});
</script>

<template>
  <nav class="nav" aria-label="Menu">
    <div class="bar">
      <button
        v-for="it in items"
        :key="it.id"
        class="tab"
        :class="{ on: active === it.id }"
        :aria-current="active === it.id ? 'true' : undefined"
        @click="go(it.id)"
      >
        <svg
          width="24"
          height="24"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          stroke-width="2"
          stroke-linecap="round"
          stroke-linejoin="round"
        >
          <path :d="it.icon" />
        </svg>
        <small>{{ $t(it.key) }}</small>
      </button>
    </div>
  </nav>
</template>

<style scoped>
/* Faqat telefonda ko'rinadi */
.nav {
  display: none;
}

@media (max-width: 640px) {
  .nav {
    display: block;
    position: fixed;
    left: 50%;
    bottom: calc(12px + env(safe-area-inset-bottom, 0px));
    z-index: 60;
    width: min(340px, calc(100% - 24px));
    transform: translateX(-50%);
  }
}

/* Shisha panel */
.bar {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  height: 62px;
  border-radius: 31px;
  background: linear-gradient(
    180deg,
    rgba(255, 255, 255, 0.74),
    rgba(255, 255, 255, 0.52)
  );
  backdrop-filter: blur(16px) saturate(1.6);
  -webkit-backdrop-filter: blur(16px) saturate(1.6);
  border: 1px solid rgba(255, 255, 255, 0.95);
  box-shadow:
    0 16px 34px rgba(30, 60, 130, 0.25),
    inset 0 1px 0 #fff;
}

/* Tab */
.tab {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 2px;
  height: 100%;
  background: none;
  color: var(--text);
  transition: color 0.25s;
}
.tab svg {
  transition: transform 0.35s var(--ease);
}
.tab:active svg {
  transform: scale(0.85);
}

/* Yorliq faqat faol tabda ochiladi */
.tab small {
  max-height: 0;
  opacity: 0;
  overflow: hidden;
  font-size: 10.5px;
  font-weight: 700;
  line-height: 1.2;
  transition:
    max-height 0.3s var(--ease),
    opacity 0.25s;
}

/* Faol tab: ko'k, yorliq chiqadi, tagida nuqta */
.tab.on {
  color: var(--blue);
}
.tab.on svg {
  transform: translateY(-1px) scale(1.08);
}
.tab.on small {
  max-height: 14px;
  opacity: 1;
}
.tab.on::after {
  content: "";
  position: absolute;
  bottom: 6px;
  width: 5px;
  height: 5px;
  border-radius: 50%;
  background: var(--blue);
  box-shadow: 0 0 8px rgba(26, 86, 204, 0.9);
  animation: dot 0.35s var(--ease);
}

@keyframes dot {
  from {
    transform: scale(0);
  }
  to {
    transform: scale(1);
  }
}

@media (prefers-reduced-motion: reduce) {
  .tab svg,
  .tab small,
  .tab.on::after {
    transition: none;
    animation: none;
  }
}
</style>
