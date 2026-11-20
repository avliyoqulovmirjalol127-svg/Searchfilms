import { createI18n } from 'vue-i18n'
import uz from './locales/uz.json'
import kaa from './locales/kaa.json'
import ru from './locales/ru.json'
import en from './locales/en.json'
import zh from './locales/zh.json'

const saved = localStorage.getItem('lang') || 'uz'
document.documentElement.lang = saved

export const i18n = createI18n({
  legacy: false,
  locale: saved,
  fallbackLocale: 'uz',
  messages: { uz, kaa, ru, en, zh },
})