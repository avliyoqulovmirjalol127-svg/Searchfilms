<script setup>
import { ref, computed } from "vue";

const code = ref("");
const ready = computed(() => code.value.length === 6);

function onInput(e) {
  code.value = e.target.value.replace(/\D/g, "").slice(0, 6);
  e.target.value = code.value;
}

function join() {
  if (!ready.value) return;
  alert("Kod: " + code.value);
}
</script>

<template>
  <section class="wrap" id="join">
    <div class="card row code">
      <div>
        <p class="tag gold">{{ $t("code.tag") }}</p>
        <h3>{{ $t("code.title") }}</h3>
        <small>{{ $t("code.text") }}</small>
      </div>

      <div class="row" style="gap: 12px">
        <input
          :value="code"
          inputmode="numeric"
          maxlength="6"
          placeholder="000000"
          :class="{ ok: ready }"
          @input="onInput"
          @keyup.enter="join"
        />
        <button class="btn gbtn" :class="{ ready }" @click="join">
          {{ $t("code.btn") }}
        </button>
      </div>
    </div>
  </section>
</template>

<style scoped>
.code {
  justify-content: space-between;
  gap: 40px;
}
.code h3 {
  font-size: 26px;
  margin: 6px 0;
}
.code input {
  width: 410px;
  height: 68px;
  padding: 0 24px;
  border-radius: 16px;
  text-align: center;
  font-size: 26px;
  letter-spacing: 0.4em;
  color: var(--navy);
  border: 1px solid #cfe0f5;
  transition:
    border-color 0.25s,
    box-shadow 0.25s;
}
.code input:focus {
  border-color: var(--blue);
  box-shadow: 0 0 0 4px rgba(26, 86, 204, 0.12);
}
.code input:focus-visible {
  outline: none;
}
.code input.ok {
  border-color: var(--gold);
  box-shadow: 0 0 0 4px rgba(217, 154, 11, 0.15);
}

.gbtn {
  height: 68px;
  padding: 0 28px;
  background: #f0c875;
  color: #7a6a4a;
  box-shadow: none;
  transition:
    background 0.3s,
    color 0.3s,
    box-shadow 0.3s,
    transform 0.25s var(--ease);
}
.gbtn.ready {
  background: linear-gradient(135deg, #e8a50f, #c27f00);
  color: #fff;
  box-shadow: 0 12px 26px rgba(194, 127, 0, 0.4);
}

@media (max-width: 900px) {
  .code {
    flex-direction: column;
    align-items: stretch;
    gap: 24px;
  }
  .code input {
    width: auto;
    flex: 1;
    min-width: 0;
  }
}

@media (max-width: 640px) {
  .code h3 {
    font-size: 22px;
  }
  .code > .row {
    flex-direction: column;
    align-items: stretch;
  }
  .code input,
  .gbtn {
    width: 100%;
  }
  .code input {
    font-size: 24px;
  }
}
</style>
