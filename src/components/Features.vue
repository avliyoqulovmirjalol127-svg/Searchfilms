<script setup>
import Heading from "./Heading.vue";

const items = [
  { n: 1, icon: "🎬", color: "#3b82f6" },
  { n: 2, icon: "🖼", color: "#e8a825" },
  { n: 3, icon: "🧠", color: "#3b82f6" },
  { n: 4, icon: "🏫", color: "#e8a825" },
];
</script>

<template>
  <Heading
    :tag="$t('features.tag')"
    :title="$t('features.title')"
    :text="$t('features.text')"
  />
  <section class="wrap grid4" id="features">
    <div v-for="f in items" :key="f.n" class="card feat lift">
      <i class="ico" :style="{ background: f.color }">{{ f.icon }}</i>
      <h3>{{ $t(`features.f${f.n}.title`) }}</h3>
      <p>{{ $t(`features.f${f.n}.text`) }}</p>
      <b>{{ $t(`features.f${f.n}.note`) }}</b>
    </div>
  </section>
</template>

<style scoped>
.grid4 {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 20px;
}
.feat {
  display: flex;
  flex-direction: column;
  gap: 12px;
  padding: 28px;
}
.feat b {
  margin-top: auto;
  font-size: 14px;
  color: #8a5a00;
}
.ico {
  display: grid;
  place-items: center;
  width: 60px;
  height: 60px;
  border-radius: 16px;
  font-size: 28px;
  font-style: normal;
}
@media (max-width: 1024px) {
  .grid4 {
    grid-template-columns: repeat(2, 1fr);
  }
}
@media (max-width: 640px) {
  .grid4 {
    grid-template-columns: 1fr;
  }
  .feat {
    padding: 22px;
  }
}
</style>
