<script setup>
import { computed } from "vue";
import { useI18n } from "vue-i18n";

const { t } = useI18n();

const badges = computed(() => [
  "🛡 " + t("hero.b1"),
  "📱 " + t("hero.b2"),
  "⚡ " + t("hero.b3"),
]);
</script>

<template>
  <section class="wrap hero">
    <div>
      <p class="tag kicker"><i class="live"></i>{{ $t('hero.tag') }}</p>
      <h1>
        {{ $t("hero.title1") }}<br />
        <span class="gold">{{ $t("hero.title2") }}</span>
      </h1>
      <p class="lead">{{ $t("hero.lead") }}</p>
      <div class="row cta">
        <button class="btn blue">✦ {{ $t("hero.start") }}</button>
        <button class="btn">{{ $t("hero.open") }}</button>
      </div>
      <div class="row badges">
        <span v-for="b in badges" :key="b">{{ b }}</span>
      </div>
    </div>

    <div class="card login" id="login">
      <i class="ico">🎓</i>
      <p class="tag">{{ $t("login.tag") }}</p>
      <h3>{{ $t("login.title") }}</h3>
      <p>{{ $t("login.text") }}</p>
      <button class="btn blue row between">
        🔐 {{ $t("login.btn") }} <span>→</span>
      </button>
      <small>{{ $t("login.note") }}</small>
    </div>
  </section>
</template>

<style scoped>
.between {
  justify-content: space-between;
}
.hero {
  display: grid;
  grid-template-columns: 1.3fr 1fr;
  gap: 80px;
  align-items: center;
  padding-top: 90px;
  padding-bottom: 70px;
}
.hero h1 {
  font-size: clamp(44px, 5.4vw, 84px);
  line-height: 1.05;
  letter-spacing: -0.03em;
  margin: 14px 0 28px;
}
.lead {
  font-size: 20px;
  margin-bottom: 30px;
}
.cta {
  gap: 16px;
  flex-wrap: wrap;
}
.badges {
  gap: 12px 26px;
  flex-wrap: wrap;
  margin-top: 30px;
  font-size: 14px;
  font-weight: 700;
}
.login {
  display: grid;
  gap: 14px;
  background: linear-gradient(135deg, #fff, #fbf5e8);
}
.login .btn {
  padding: 22px 26px;
}
.login small {
  text-align: center;
}
.ico {
  display: grid;
  place-items: center;
  width: 88px;
  height: 88px;
  border-radius: 24px;
  font-size: 38px;
  font-style: normal;
  background: linear-gradient(135deg, #4a9ad4, #d9a21b);
}
.kicker {
  display: flex;
  align-items: center;
  gap: 10px;
}
.live {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: #f5a623;
  box-shadow: 0 0 0 6px rgba(245, 166, 35, 0.2);
}

.login h3 {
  font-size: 34px;
}
.login p:not(.tag) {
  font-size: 17px;
}

/* Planshet */
@media (max-width: 1024px) {
  .hero {
    grid-template-columns: 1fr;
    gap: 40px;
    padding-top: 50px;
    padding-bottom: 40px;
  }
  .hero h1 {
    font-size: 52px;
  }
}

/* Telefon */
@media (max-width: 640px) {
  .hero {
    gap: 28px;
    padding-top: 32px;
  }
  .hero h1 {
    font-size: 30px;
  }
  .login h3 {
    font-size: 1.17em;
  }
  .login p:not(.tag) {
    font-size: 1em;
  }
  .lead {
    font-size: 17px;
  }
  .cta .btn {
    flex: 1 1 100%;
  }
  .badges {
    gap: 10px 18px;
    font-size: 13px;
  }
  .login .btn {
    padding: 18px 20px;
  }
  .ico {
    width: 72px;
    height: 72px;
    font-size: 32px;
  }
}
</style>
