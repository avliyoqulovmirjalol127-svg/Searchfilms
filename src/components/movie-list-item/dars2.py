# MUSTAQIL ISH: variantni so'rab hisoblash

# Jadval: variant: (uylar soni, 1 uy kVt, energiya kVt*s/yil, isrof %, narx $, foyda $/yil)
variantlar = {
    1:  (100, 2,   1000000, 5,  100000, 20000),
    2:  (150, 2,   1500000, 4,  120000, 30000),
    3:  (200, 1.5, 2000000, 3,  150000, 25000),
    4:  (120, 2.5, 1200000, 6,  90000,  15000),
    5:  (80,  3,   800000,  5,  80000,  16000),
    6:  (250, 1.2, 2500000, 2,  200000, 40000),
    7:  (300, 1,   3000000, 4,  240000, 60000),
    8:  (180, 2,   1800000, 5,  180000, 36000),
    9:  (60,  2.5, 600000,  10, 60000,  12000),
    10: (400, 1.5, 4000000, 3,  320000, 80000),
}

kt = 0.5  # talab koeffitsiyenti

v = int(input("Variant raqamini kiriting (1-10): "))

if v not in variantlar:
    print("Bunday variant yo'q! 1 dan 10 gacha kiriting.")
else:
    n, p, W, isrof, narx, foyda = variantlar[v]

    print()
    print("Variant:", v)
    print("Uylar soni:", n, "| 1 uy:", p, "kVt | Energiya:", W, "kVt*s/yil")
    print("Isrof:", isrof, "% | Narx:", narx, "$ | Foyda:", foyda, "$/yil")
    print()

    # 1-qadam: quvvat
    P = n * p * kt
    print("1-qadam: P =", P, "kVt")

    # 2-qadam: yillik isrof
    W_isrof = W * isrof / 100
    print("2-qadam: Isrof =", W_isrof, "kVt*s/yil")

    # 3-qadam: qaytish muddati
    T = narx / foyda
    print("3-qadam: Qaytish muddati =", round(T, 2), "yil")

    # 4-qadam: CO2
    co2_gaz = W * 0.5 / 1000
    co2_quyosh = W * 0.04 / 1000
    print("4-qadam: CO2 gaz =", co2_gaz, "tonna")
    print("4-qadam: CO2 quyosh =", co2_quyosh, "tonna")
    print("Farq:", co2_gaz - co2_quyosh, "tonna kam chiqadi")