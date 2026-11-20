<script setup>
import { ref } from "vue";
import Heading from "./Heading.vue";

const list = [
  { k: "a1", color: "#e8a825", emoji: "😄" },
  { k: "a2", color: "#e07a8c", emoji: "😊" },
  { k: "a3", color: "#3aa8a8", emoji: "🤓" },
  { k: "a4", color: "#5c78c0", emoji: "👓" },
  { k: "a5", color: "#7aa84a", emoji: "😆" },
  { k: "a6", color: "#ee9a55", emoji: "😁" },
  { k: "a7", color: "#8f86c0", emoji: "😴" },
  { k: "a8", color: "#a85a95", emoji: "😒" },
  { k: "a9", color: "#c4574a", emoji: "😠" },
  { k: "a10", color: "#3f9a7a", emoji: "🙂" },
];

const picked = ref(null);
</script>

<template>
  <Heading
    :tag="$t('avatars.tag')"
    :title="$t('avatars.title')"
    :text="$t('avatars.text')"
  />

  <section class="wrap avatars">
    <button
      v-for="(a, i) in list"
      :key="a.k"
      class="av"
      :class="{ on: picked === a.k }"
      :style="{ '--i': i, '--c': a.color }"
      @click="picked = a.k"
    >
      <span v-if="picked === a.k" class="check">
        <svg
          width="14"
          height="14"
          viewBox="0 0 24 24"
          fill="none"
          stroke="#fff"
          stroke-width="3.5"
          stroke-linecap="round"
          stroke-linejoin="round"
        >
          <path d="M5 12l5 5 9-10" />
        </svg>
      </span>
      <i class="face">{{ a.emoji }}</i>
      <b>{{ $t(`avatars.list.${a.k}.name`) }}</b>
      <small>{{ $t(`avatars.list.${a.k}.trait`) }}</small>
    </button>
  </section>

  <p class="hint">{{ $t("avatars.hint") }}</p>
</template>

<style scoped>
.avatars {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 16px;
}

.av {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
  width: 132px;
  padding: 18px 8px 16px;
  border-radius: 24px;
  background: rgba(255, 255, 255, 0.92);
  box-shadow: 0 6px 18px rgba(30, 60, 130, 0.08);
  transition:
    transform 0.3s var(--ease),
    box-shadow 0.3s var(--ease);
}
.av:hover {
  transform: translateY(-8px) rotate(-1.5deg);
  box-shadow: 0 22px 40px rgba(30, 60, 130, 0.2);
}
.av.on {
  box-shadow:
    0 0 0 3px var(--c),
    0 22px 40px rgba(30, 60, 130, 0.22);
}

.face {
  display: grid;
  place-items: center;
  width: 98px;
  height: 98px;
  margin-bottom: 8px;
  border-radius: 50%;
  font-size: 46px;
  font-style: normal;
  background: var(--c);
  box-shadow: 0 12px 22px rgba(20, 40, 95, 0.2);
  animation: float 4.5s ease-in-out infinite;
  animation-delay: calc(var(--i) * -0.45s);
}

.av b {
  color: var(--blue);
  font-size: 14px;
}
.av small {
  font-size: 12px;
  line-height: 1.3;
  color: var(--text);
}

.check {
  position: absolute;
  top: 10px;
  right: 10px;
  display: grid;
  place-items: center;
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background: #22b573;
  box-shadow: 0 4px 10px rgba(34, 181, 115, 0.45);
  animation: pop 0.35s var(--ease);
}

.hint {
  margin-top: 22px;
  text-align: center;
  font-size: 14px;
  color: var(--text);
}

@keyframes float {
  0%,
  100% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-6px);
  }
}
@keyframes pop {
  from {
    transform: scale(0);
  }
  to {
    transform: scale(1);
  }
}

@media (prefers-reduced-motion: reduce) {
  .face {
    animation: none;
  }
}

@media (max-width: 640px) {
  .avatars {
    gap: 10px;
  }
  .av {
    width: calc(33.333% - 7px);
    padding: 14px 4px 12px;
  }
  .face {
    width: 70px;
    height: 70px;
    font-size: 32px;
  }
  .av b {
    font-size: 12px;
  }
  .av small {
    font-size: 11px;
  }
}
</style>
