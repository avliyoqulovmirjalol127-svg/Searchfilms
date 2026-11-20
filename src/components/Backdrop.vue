<template>
  <div class="bg" aria-hidden="true">
    <i class="blob b1"></i>
    <i class="blob b2"></i>
    <i class="blob b3"></i>
    <i class="blob b4"></i>
    <i class="dots"></i>
  </div>
</template>

<style scoped>
.bg {
  position: fixed;
  inset: 0;
  z-index: -1;
  overflow: hidden;
  pointer-events: none;
}

/* Yorug' dog'lar */
.blob {
  position: absolute;
  border-radius: 50%;
  filter: blur(90px);
  opacity: 0.55;
  animation: float 22s ease-in-out infinite;
}
.b1 {
  width: 620px;
  height: 620px;
  top: -180px;
  left: -140px;
  background: #5b8cff;
}
.b2 {
  width: 520px;
  height: 520px;
  top: 18%;
  right: -160px;
  background: #ffc857;
  opacity: 0.45;
  animation-delay: -6s;
  animation-duration: 26s;
}
.b3 {
  width: 560px;
  height: 560px;
  bottom: -220px;
  left: 12%;
  background: #8b7bff;
  opacity: 0.38;
  animation-delay: -12s;
  animation-duration: 30s;
}
.b4 {
  width: 420px;
  height: 420px;
  bottom: 8%;
  right: 8%;
  background: #4fd1c5;
  opacity: 0.25;
  animation-delay: -3s;
  animation-duration: 24s;
}

/* Nuqtali to'r (tepada ko'rinadi, pastga so'nadi) */
.dots {
  position: absolute;
  inset: 0;
  background-image: radial-gradient(
    rgba(20, 40, 95, 0.16) 1px,
    transparent 1.4px
  );
  background-size: 28px 28px;
  -webkit-mask-image: linear-gradient(to bottom, #000 0%, transparent 70%);
  mask-image: linear-gradient(to bottom, #000 0%, transparent 70%);
}

@keyframes float {
  0%,
  100% {
    transform: translate(0, 0) scale(1);
  }
  33% {
    transform: translate(60px, 40px) scale(1.08);
  }
  66% {
    transform: translate(-40px, 70px) scale(0.95);
  }
}

/* Animatsiyani yoqtirmaydiganlar uchun */
@media (prefers-reduced-motion: reduce) {
  .blob {
    animation: none;
  }
}
</style>
