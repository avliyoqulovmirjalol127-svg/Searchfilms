<template>
  <section class="wrap price" id="pricing"></section>
  <section class="wrap price">
    <div class="card row box">
      <div class="info">
        <p class="tag">{{ $t("pricing.tag") }}</p>
        <h3 class="gold">{{ $t("pricing.price") }}</h3>
        <p>{{ $t("pricing.text") }}</p>
      </div>
      <div class="card sub">
        <b style="color: #0f8a55">● {{ $t("pricing.open") }}</b>
        <p>{{ $t("pricing.spotsText") }}</p>
        <button class="btn blue">{{ $t("pricing.btn") }} →</button>
      </div>
    </div>
  </section>
</template>

<style scoped>
.price {
  margin-top: 80px;
}
.box {
  justify-content: space-between;
  gap: 32px;
}
.info {
  max-width: 800px;
}
.info h3 {
  font-size: 26px;
}
.sub {
  display: grid;
  gap: 14px;
  width: 490px;
  padding: 30px;
}

@media (max-width: 1024px) {
  .box {
    flex-direction: column;
    align-items: stretch;
  }
  .info {
    max-width: none;
  }
  .sub {
    width: 100%;
  }
}

@media (max-width: 640px) {
  .price {
    margin-top: 48px;
  }
  .info h3 {
    font-size: 22px;
  }
  .sub {
    padding: 22px;
  }
}
</style>
