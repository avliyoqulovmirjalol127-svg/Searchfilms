<script setup>
defineProps({ tag: String, title: String, text: String })
</script>

<template>
  <div class="sec">
    <p class="tag">{{ tag }}</p>
    <h2>{{ title }}</h2>
    <p>{{ text }}</p>
  </div>
</template>