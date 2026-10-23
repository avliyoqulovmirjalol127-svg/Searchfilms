
#  VARIANTNI SO'RASH 
variantlar = {
    1:  [200, 6, 30],
    2:  [250, 8, 40],
    3:  [350, 12, 50],
    4:  [400, 5, 20],
    5:  [450, 7, 30],
    6:  [500, 9, 40],
    7:  [550, 4, 50],
    8:  [600, 6, 20],
    9:  [650, 8, 30],
    10: [700, 5, 40],
}

jurnal_raqam = int(input("Jurnaldagi tartib raqamingizni kiriting: "))
variant = jurnal_raqam % 10
if variant == 0:
    variant = 10

uylar_soni = variantlar[variant][0]
L = variantlar[variant][1]
quyosh_ulushi = variantlar[variant][2]

print("Variant:", variant)
print("Uylar soni:", uylar_soni, "| L:", L, "km | Quyosh ulushi:", quyosh_ulushi, "%")
print()

# O'zgarmas berilganlar
P1 = 2          # bitta uy quvvati, kVt
k = 0.5         # talab koeffitsiyenti
U = 10          # kuchlanish, kV
r0 = 0.5        # 1 km sim qarshiligi, Om/km

#  FUNKSIYALAR
def isrof(tok, qarshilik):
    return 3 * tok * tok * qarshilik

def kuchlanish_tushuvi(tok, qarshilik):
    return 1.73 * tok * qarshilik

#  P va I 
P_uylar = uylar_soni * P1 * k
P_maktab = 1 * 52 * k
P_dokon = 10 * 4 * k
P = P_uylar + P_maktab + P_dokon
I = P / (1.73 * U)
print("P =", P, "kVt")
print("I =", round(I, 2), "A")

# Energiya (yaxlitlamang!)
W_aniq = 1000000 * P / 346
W = W_aniq
print("W =", W, "kVt*soat")
print()

# A VARIANT: R, dP, dU 
R_A = r0 * L
dP_A = isrof(I, R_A) / 1000                                # kVt
dU_A = kuchlanish_tushuvi(I, R_A) / (U * 1000) * 100       # %
print("A: R =", round(R_A, 2), "Om")
print("A: dP =", round(dP_A, 2), "kVt")
print("A: dU =", round(dU_A, 2), "%")
print("A uchun dU < 5 % ?", dU_A < 5)
print()

#  C VARIANT: tok va dP 
I_C = I * (100 - quyosh_ulushi) / 100
R_C = r0 * L
dP_C = isrof(I_C, R_C) / 1000
dU_C = kuchlanish_tushuvi(I_C, R_C) / (U * 1000) * 100
print("C: I =", round(I_C, 2), "A")
print("C: dP =", round(dP_C, 2), "kVt")
print()

#   CO2 (A va C), tonna/yil 
tarmoqdan_C = W * (100 - quyosh_ulushi) / 100
quyoshdan_C = W - tarmoqdan_C
co2_A = W * 0.5 / 1000
co2_C = (tarmoqdan_C * 0.5 + quyoshdan_C * 0.04) / 1000
print("A: CO2 =", round(co2_A, 1), "tonna")
print("C: CO2 =", round(co2_C, 1), "tonna")
print()

#  LABORATORIYA JADVALI 

print("Variant", "U,kV", "R,Om", "P,kVt", "I,A", "dP,kVt", "dU,%", sep="\t")
print("A", U, round(R_A, 2), round(P, 1), round(I, 2), round(dP_A, 2), round(dU_A, 2), sep="\t")
print("C", U, round(R_C, 2), round(P, 1), round(I_C, 2), round(dP_C, 2), round(dU_C, 2), sep="\t")