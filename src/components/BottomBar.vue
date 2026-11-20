<script setup>
import { useI18n } from "vue-i18n";
import { flags } from "../flags";

const { locale } = useI18n();

const cols = [
  { icon: "grid", title: "footer.services", link: "footer.id" },
  { icon: "link", title: "footer.links", link: "footer.about" },
  {
    icon: "shield",
    title: "footer.legal",
    link: "footer.privacyPolicy",
    langs: true,
  },
];

const icons = {
  grid: "M5 5h4v4H5zM15 5h4v4h-4zM5 15h4v4H5zM15 15h4v4h-4z",
  link: "M10 14a4 4 0 005.7 0l3-3a4 4 0 00-5.7-5.7l-1 1M14 10a4 4 0 00-5.7 0l-3 3a4 4 0 005.7 5.7l1-1",
  shield: "M12 3l7 3v5c0 5-3 8-7 10-4-2-7-5-7-10V6zM9 12l2 2 4-4",
};

const langs = [
  { code: "uz", name: "O'zbek" },
  { code: "kaa", name: "Qaraqalpaq" },
  { code: "ru", name: "Русский" },
  { code: "en", name: "English" },
  { code: "zh", name: "中文" },
];

function pick(code) {
  locale.value = code;
  localStorage.setItem("lang", code);
  document.documentElement.lang = code;
}
</script>

<template>
  <footer class="wrap" style="margin: 110px auto 40px">
    <div class="card foot">
      <div>
        <div class="brand">
          <i class="dash"></i>
          <span class="logo2">yhuu</span>
        </div>
        <h3 class="slogan">{{ $t("footer.slogan") }}</h3>
        <p>{{ $t("footer.desc") }}</p>

        <div class="row soc">
          <a
            href="https://t.me/yhuu_uz"
            target="_blank"
            rel="noopener"
            class="dot tg"
            aria-label="Telegram"
          >
            <svg width="22" height="22" viewBox="0 0 24 24" fill="#fff">
              <path d="M21 4L3 11l5 2 2 6 3-4 5 4zM8 13l9-6" />
            </svg>
          </a>
          <a
            href="https://youtube.com/@yhuu_uz"
            target="_blank"
            rel="noopener"
            class="dot yt"
            aria-label="YouTube"
          >
            <svg width="22" height="22" viewBox="0 0 24 24" fill="#fff">
              <path d="M9 7v10l8-5z" />
            </svg>
          </a>
          <a
            href="https://instagram.com/yhuu.uz"
            target="_blank"
            rel="noopener"
            class="dot ig"
            aria-label="Instagram"
          >
            <svg
              width="22"
              height="22"
              viewBox="0 0 24 24"
              fill="none"
              stroke="#fff"
              stroke-width="2"
              stroke-linecap="round"
              stroke-linejoin="round"
            >
              <rect x="3" y="3" width="18" height="18" rx="5" />
              <circle cx="12" cy="12" r="4" />
              <circle cx="17.5" cy="6.5" r="1" fill="#fff" stroke="none" />
            </svg>
          </a>
        </div>
      </div>

      <div v-for="c in cols" :key="c.title">
        <h3 class="fh">
          <i class="ico">
            <svg
              width="22"
              height="22"
              viewBox="0 0 24 24"
              fill="none"
              stroke="#fff"
              stroke-width="2"
              stroke-linecap="round"
              stroke-linejoin="round"
            >
              <path :d="icons[c.icon]" />
            </svg>
          </i>
          {{ $t(c.title) }}
        </h3>

        <a href="#" class="fl">
          {{ $t(c.link) }}
          <svg width="8" height="14" viewBox="0 0 8 14" fill="none">
            <path
              d="M1 1l6 6-6 6"
              stroke="currentColor"
              stroke-width="2"
              stroke-linecap="round"
            />
          </svg>
        </a>

        <div v-if="c.langs" class="langs">
          <button
            v-for="l in langs"
            :key="l.code"
            :class="{ on: l.code === locale }"
            @click="pick(l.code)"
          >
            <i class="flag" v-html="flags[l.code]"></i>
            {{ l.name }}
          </button>
        </div>
      </div>

      <div class="support">
        <a href="tel:+998711234567" class="row call" style="gap: 18px">
          <i class="phone">
            <svg
              width="26"
              height="26"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="2"
              stroke-linecap="round"
              stroke-linejoin="round"
            >
              <path
                d="M5 4h4l2 5-2.5 1.5a11 11 0 005 5L15 13l5 2v4a2 2 0 01-2 2A16 16 0 013 6a2 2 0 012-2z"
              />
            </svg>
          </i>
          <div>
            <small>{{ $t("footer.support") }}</small>
            <h3 class="tel">+998 71 123 45 67</h3>
            <small>{{ $t("footer.hours") }}</small>
          </div>
        </a>
        <div class="row" style="gap: 14px">
          <small>{{ $t("footer.mobile") }}</small>

          <a href="#" class="store">
            <svg width="26" height="26" viewBox="0 0 24 24" fill="#14285f">
              <path
                d="M16.4 12.6c0-2.3 1.9-3.4 2-3.5-1.1-1.6-2.8-1.8-3.4-1.8-1.4-.1-2.8.9-3.5.9s-1.8-.8-3-.8c-1.5 0-3 .9-3.8 2.3-1.6 2.8-.4 7 1.2 9.3.8 1.1 1.7 2.4 2.9 2.3 1.2 0 1.6-.8 3-.8s1.8.8 3 .8 2-1.1 2.8-2.2c.9-1.3 1.2-2.5 1.3-2.6-.1 0-2.5-1-2.5-3.9zM14.1 5.8c.6-.8 1.1-1.8.9-2.8-.9 0-2 .6-2.6 1.4-.6.7-1.1 1.8-.9 2.7 1 .1 2-.5 2.6-1.3z"
              />
            </svg>
            <span
              ><small>{{ $t("footer.download") }}</small
              ><b>App Store</b></span
            >
          </a>

          <a href="#" class="store">
            <svg width="26" height="26" viewBox="0 0 24 24">
              <path d="M4 3l10 9-10 9z" fill="#1ea366" />
              <path d="M4 3l13 7-3 2z" fill="#4285f4" />
              <path d="M4 21l13-7-3-2z" fill="#ea4335" />
              <path d="M17 10l4 2-4 2-3-2z" fill="#fbbc04" />
            </svg>
            <span
              ><small>{{ $t("footer.download") }}</small
              ><b>Google Play</b></span
            >
          </a>
        </div>
      </div>

      <div class="copy">
        <small>{{ $t("footer.copy") }}</small>
        <small class="legal">
          <a href="#">{{ $t("footer.privacy") }}</a> •
          <a href="#">{{ $t("footer.terms") }}</a> •
          <a href="#">{{ $t("footer.cookies") }}</a>
        </small>
        <small class="status">
          <i class="pulse"></i> {{ $t("footer.status") }}
          <span class="ver">v1.0.0</span>
        </small>
      </div>
    </div>
  </footer>
</template>
<style scoped>
.foot {
  display: grid;
  grid-template-columns: 1.2fr 1fr 1fr 1fr;
  gap: 40px;
  padding: 44px;
}

/* Brend */
.brand {
  position: relative;
  display: inline-block;
}
.dash {
  position: absolute;
  top: 14px;
  left: 6px;
  width: 36px;
  height: 5px;
  border-radius: 5px;
  background: linear-gradient(90deg, #ffc933, #ffb300);
  transform: rotate(-10deg);
  box-shadow: 0 3px 8px rgba(255, 179, 0, 0.45);
}
.logo2 {
  display: inline-block;
  font-size: 58px;
  font-style: italic;
  font-weight: 800;
  letter-spacing: -2px;
  background: linear-gradient(135deg, #2a6af0, #5b45e8);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}
.slogan {
  margin: 14px 0 8px;
  font-size: 22px;
}

/* Ijtimoiy tarmoqlar */
.soc {
  gap: 12px;
  margin-top: 20px;
}
.dot {
  display: grid;
  place-items: center;
  width: 46px;
  height: 46px;
  border-radius: 50%;
  box-shadow: 0 8px 18px rgba(30, 60, 130, 0.18);
  transition: transform 0.25s var(--ease);
}
.dot:hover {
  transform: translateY(-4px) scale(1.08);
}
.tg {
  background: #2aa3e0;
}
.yt {
  background: #ff3030;
}
.ig {
  background: linear-gradient(
    45deg,
    #feda75,
    #fa7e1e,
    #d62976,
    #962fbf,
    #4f5bd5
  );
}

/* Ustunlar */
.fh {
  display: flex;
  align-items: center;
  gap: 12px;
  font-size: 18px;
}
.ico {
  display: grid;
  place-items: center;
  width: 46px;
  height: 46px;
  border-radius: 14px;
  background: linear-gradient(135deg, #7a86f5, #5b45e8);
  box-shadow: 0 8px 18px rgba(91, 69, 232, 0.3);
}
.fl {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 18px;
  padding: 12px 0;
  border-bottom: 1px solid #e3eaf5;
  transition:
    color 0.2s,
    padding 0.25s var(--ease);
}
.fl:hover {
  color: var(--blue);
  padding-left: 8px;
}

/* Til chiplari */
.langs {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 18px;
}
.langs button {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 6px 14px 6px 8px;
  border-radius: 999px;
  font-size: 14px;
  background: #fff;
  color: var(--text);
  border: 1px solid #e3eaf5;
  transition:
    transform 0.25s var(--ease),
    border-color 0.2s,
    color 0.2s,
    box-shadow 0.2s;
}
.langs button:hover {
  transform: translateY(-2px);
  border-color: var(--blue);
  color: var(--blue);
  box-shadow: 0 8px 16px rgba(26, 86, 204, 0.15);
}
.langs button.on {
  background: var(--blue);
  border-color: var(--blue);
  color: #fff;
  box-shadow: 0 8px 18px rgba(26, 86, 204, 0.3);
}

/* Bayroq */
.flag {
  display: block;
  width: 26px;
  height: 18px;
  border-radius: 4px;
  overflow: hidden;
  flex: none;
  box-shadow:
    0 0 0 1px rgba(20, 40, 95, 0.12),
    0 2px 5px rgba(20, 40, 95, 0.2);
}
.flag :deep(svg) {
  display: block;
  width: 100%;
  height: 100%;
}

/* Telefon (bosiladigan) */
.call {
  color: inherit;
  transition: transform 0.25s var(--ease);
}
.call:hover {
  transform: translateX(4px);
}
.call .phone {
  transition:
    background 0.25s,
    color 0.25s,
    box-shadow 0.25s;
}
.call:hover .phone {
  background: var(--blue);
  color: #fff;
  box-shadow: 0 10px 22px rgba(26, 86, 204, 0.35);
}
.call:hover .tel {
  text-decoration: underline;
}

/* Aloqa */
.support,
.copy {
  grid-column: 1 / -1;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 20px;
}
.support {
  padding: 26px 32px;
  border-radius: 22px;
  background: linear-gradient(
    135deg,
    rgba(255, 255, 255, 0.95),
    rgba(238, 244, 255, 0.8)
  );
  border: 1px solid #fff;
  box-shadow: 0 10px 30px rgba(30, 60, 130, 0.07);
}
.phone {
  display: grid;
  place-items: center;
  width: 56px;
  height: 56px;
  border-radius: 18px;
  color: var(--blue);
  background: #e6efff;
}
.tel {
  font-size: 26px;
  color: var(--blue);
}
.store {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px 20px;
  border-radius: 16px;
  background: #fff;
  box-shadow: 0 6px 18px rgba(30, 60, 130, 0.1);
  transition:
    transform 0.25s var(--ease),
    box-shadow 0.25s var(--ease);
}
.store:hover {
  transform: translateY(-3px);
  box-shadow: 0 14px 28px rgba(30, 60, 130, 0.18);
}
.store span {
  display: grid;
  line-height: 1.15;
}
.store b {
  color: var(--navy);
  font-size: 17px;
}

/* Pastki qator */
.copy {
  padding-top: 8px;
}
.legal a:hover {
  color: var(--blue);
}
.status {
  display: flex;
  align-items: center;
  gap: 8px;
}
.pulse {
  width: 9px;
  height: 9px;
  border-radius: 50%;
  background: #22b573;
  box-shadow: 0 0 0 0 rgba(34, 181, 115, 0.6);
  animation: pulse 2s infinite;
}
.ver {
  padding: 3px 12px;
  border-radius: 999px;
  background: #fff;
  border: 1px solid #e3eaf5;
}
@keyframes pulse {
  70% {
    box-shadow: 0 0 0 9px rgba(34, 181, 115, 0);
  }
  100% {
    box-shadow: 0 0 0 0 rgba(34, 181, 115, 0);
  }
}
@media (max-width: 1024px) {
  .foot {
    grid-template-columns: 1fr 1fr;
    gap: 32px;
    padding: 32px;
  }
}

@media (max-width: 640px) {
  .foot {
    grid-template-columns: 1fr;
    padding: 24px;
  }
  .logo2 {
    font-size: 46px;
  }
  .slogan {
    font-size: 19px;
  }
  .tel {
    font-size: 22px;
  }
  .support {
    flex-direction: column;
    align-items: flex-start;
    padding: 20px;
  }
  .support .row {
    flex-wrap: wrap;
  }
  .copy {
    flex-direction: column;
    align-items: flex-start;
    gap: 12px;
  }
}
</style>
