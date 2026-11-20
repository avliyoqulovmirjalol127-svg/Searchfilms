<script setup>
import Heading from "./Heading.vue";
</script>

<template>
  <Heading
    :tag="$t('catalog.tag')"
    :title="$t('catalog.title')"
    :text="$t('catalog.text')"
  />
  <section class="wrap" id="catalog">
    <div class="empty">
      <div class="icon">
        <svg
          width="34"
          height="34"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          stroke-width="1.8"
          stroke-linecap="round"
          stroke-linejoin="round"
        >
          <path d="M4 5h16v11H4z" />
          <path d="M8 20h8M12 16v4" />
          <path d="M10 9l4 2-4 2z" />
        </svg>
      </div>
      <h3>{{ $t("catalog.emptyTitle") }}</h3>
      <small>{{ $t("catalog.emptyText") }}</small>
    </div>
  </section>
</template>

<style scoped>
.empty {
  display: grid;
  justify-items: center;
  gap: 10px;
  padding: 80px 20px;
  text-align: center;
  border: 2px dashed #b8cde8;
  border-radius: 28px;
  background: rgba(255, 255, 255, 0.45);
}
.icon {
  display: grid;
  place-items: center;
  width: 78px;
  height: 78px;
  margin-bottom: 8px;
  border-radius: 24px;
  color: var(--blue);
  background: linear-gradient(135deg, #e3edff, #fff);
  box-shadow: 0 10px 26px rgba(26, 86, 204, 0.16);
}
@media (max-width: 640px) {
  .empty {
    padding: 48px 16px;
  }
}
</style>
