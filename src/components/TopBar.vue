<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useI18n } from 'vue-i18n'
import { flags } from '../flags'

const { locale } = useI18n()

const langs = [
  { code: 'uz', name: "O'zbekcha", domain: '.uz' },
  { code: 'kaa', name: 'Qaraqalpaqsha', domain: '.kaa' },
  { code: 'ru', name: 'Русский', domain: '.ru' },
  { code: 'en', name: 'English', domain: '.en' },
  { code: 'zh', name: '中文', domain: '.zh' },
]

const open = ref(false)
const box = ref(null)

const current = computed(() => locale.value)
const active = computed(() => langs.find((l) => l.code === current.value))

function pick(code) {
  locale.value = code
  localStorage.setItem('lang', code)
  document.documentElement.lang = code
  open.value = false
}

function outside(e) {
  if (box.value && !box.value.contains(e.target)) open.value = false
}

onMounted(() => document.addEventListener('click', outside))
onUnmounted(() => document.removeEventListener('click', outside))
</script>

<template>
  <header class="head">
    <div class="wrap row between">
      <div class="row" style="gap: 12px">
        <a href="/" class="logo">
          <i class="dash"></i>
          yhuu
        </a>

        <div ref="box" class="lang">
          <button class="uz" @click="open = !open">
            {{ active.domain }}
            <i class="flag" v-html="flags[current]"></i>
            <svg
              class="chev"
              :class="{ up: open }"
              width="12"
              height="8"
              viewBox="0 0 12 8"
              fill="none"
            >
              <path
                d="M1 1.5l5 5 5-5"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
              />
            </svg>
          </button>

          <Transition name="pop">
            <ul v-if="open" class="menu">
              <li
                v-for="l in langs"
                :key="l.code"
                :class="{ on: l.code === current }"
                @click="pick(l.code)"
              >
                <i class="flag sm" v-html="flags[l.code]"></i>
                <span class="name">{{ l.name }}</span>
                <span class="dom">{{ l.domain }}</span>
              </li>
            </ul>
          </Transition>
        </div>
      </div>

      <div class="actions">
        <a href="#pricing" class="btn plans">{{ $t('nav.pricing') }}</a>
        <button class="btn violet">{{ $t('nav.login') }}</button>
      </div>
    </div>
  </header>
</template>

<style scoped>
.between {
  justify-content: space-between;
}
.head {
  position: sticky;
  top: 0;
  z-index: 50;
  height: 110px;
  display: flex;
  align-items: center;
  background: rgba(255, 255, 255, 0.82);
  backdrop-filter: blur(16px);
  border-bottom: 1px solid rgba(20, 40, 95, 0.06);
}
.head .wrap {
  width: 100%;
}

/* Logo */
.logo {
  position: relative;
  color: #fff;
  font-size: 32px;
  font-weight: 800;
  letter-spacing: -1px;
  padding: 18px 32px 14px;
  border-radius: 16px;
  background: linear-gradient(135deg, #2a6af0, #1445a8);
  box-shadow: 0 10px 24px rgba(26, 86, 204, 0.4);
  transition: transform 0.3s var(--ease);
}
.logo:hover {
  transform: rotate(-2deg) scale(1.04);
}
.dash {
  position: absolute;
  top: 9px;
  left: 34px;
  width: 26px;
  height: 4px;
  border-radius: 4px;
  background: #ffc933;
  transform: rotate(-10deg);
}

/* Til tugmasi */
.lang {
  position: relative;
}
.uz {
  display: flex;
  align-items: center;
  gap: 6px;
  background: none;
  color: var(--blue);
  font-size: 22px;
  font-weight: 800;
  padding: 6px 4px;
  border-bottom: 2px solid var(--blue);
}
.chev {
  transition: transform 0.25s var(--ease);
}
.chev.up {
  transform: rotate(180deg);
}

/* Bayroq */
.flag {
  position: relative;
  display: block;
  width: 34px;
  height: 22px;
  border-radius: 5px;
  overflow: hidden;
  flex: none;
  box-shadow:
    0 0 0 1px rgba(20, 40, 95, 0.12),
    0 4px 10px rgba(20, 40, 95, 0.22);
  transition: transform 0.25s var(--ease);
}
.flag :deep(svg) {
  display: block;
  width: 100%;
  height: 100%;
}
.flag::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.3), rgba(255, 255, 255, 0) 55%);
  pointer-events: none;
}
.uz:hover .flag {
  transform: scale(1.1) rotate(-3deg);
}
.flag.sm {
  width: 36px;
  height: 24px;
}

/* Til menyusi */
.menu {
  position: absolute;
  top: calc(100% + 14px);
  left: 0;
  width: 250px;
  list-style: none;
  padding: 8px;
  border-radius: 20px;
  background: #fff;
  border: 1px solid #eef2fa;
  box-shadow: 0 24px 50px rgba(30, 60, 130, 0.2);
}
.menu li {
  display: grid;
  grid-template-columns: 36px 1fr auto;
  align-items: center;
  gap: 12px;
  padding: 11px 12px;
  border-radius: 14px;
  font-size: 15px;
  font-weight: 600;
  color: var(--navy);
  cursor: pointer;
  transition:
    background 0.2s,
    color 0.2s;
}
.menu li:hover {
  background: #f1f6ff;
}
.menu li.on {
  background: #e8f0ff;
  color: var(--blue);
}
.dom {
  font-weight: 500;
  color: var(--text);
}
.menu li.on .dom {
  color: var(--blue);
}

.pop-enter-active,
.pop-leave-active {
  transition:
    opacity 0.2s,
    transform 0.25s var(--ease);
}
.pop-enter-from,
.pop-leave-to {
  opacity: 0;
  transform: translateY(-8px) scale(0.97);
}

/* O'ng tugmalar */
.actions {
  display: flex;
  align-items: center;
  gap: 16px;
}
.plans {
  background: #fff;
  color: var(--blue);
  border: 1px solid #e3eaf5;
}
.violet {
  color: #fff;
  background: linear-gradient(135deg, #7059f0, #5b45e8);
  box-shadow: 0 10px 24px rgba(91, 69, 232, 0.38);
}

/* Telefon: avvalgi holat, "Tariflar" ko'rinmaydi */
@media (max-width: 640px) {
  .plans {
    display: none;
  }
  .head {
    height: 76px;
  }
  .logo {
    font-size: 22px;
    padding: 12px 20px 8px;
    border-radius: 12px;
  }
  .dash {
    top: 6px;
    left: 22px;
    width: 18px;
    height: 3px;
  }
  .uz {
    font-size: 18px;
  }
  .violet {
    padding: 10px 14px;
    font-size: 13px;
    line-height: 1.25;
  }
  .menu {
    width: 220px;
  }
}
</style>