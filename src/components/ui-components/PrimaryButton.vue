<template>
  <button class="btn">
    <slot></slot>
  </button>
</template>

<script >
import { defineComponent } from 'vue';

export default {
  name: 'PrimaryButton',
  data() {
    return {};
  },
  methods: {},
};
</script>