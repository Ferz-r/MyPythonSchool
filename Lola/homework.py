#zadanie1
distance = 300
speed = 100
rashod_topliva = 8 #8 litros za kazhdyi 100 km
cena_topliva = 60 #60 rublei za litr

vremya_v_puti = distance/speed
print (f"vremya v puti: {vremya_v_puti}")
#rezultat = 3.0

vremya_v_minutah = vremya_v_puti * 60
print (f"vremya_v_minutah: {vremya_v_minutah}")
#rezultat = 180.0

nuzhno_litrov_topliva = distance * rashod_topliva / 100
print (f"nuzhno_litrov_topliva: {nuzhno_litrov_topliva}")
#rezultat = 24.0

cena_topliva = nuzhno_litrov_topliva * cena_topliva
print (cena_topliva)
rezultat = 1440

#zadanie 2
print("===zadanie 2===")
rubli = 20000
exchange = 75

result = rubli//exchange
ostatok = rubli%exchange

print ("obichniy obmennik")
print (f"poluchilos v celyh dollarah:{result}")
print (f"sdacha v rublyah:{ostatok}")

result = round (rubli/exchange,2)
print ("obmennik s centami")
print (f"poluchilos v dollarah {result}")

#zadanie 3 
konfety = 20
deti = 6

na_rebenka = konfety // deti
print (na_rebenka)
#rezultat = 3

ostatok = konfety % deti
print (ostatok)
#resultat = 2

dokupit = deti - ostatok
print (dokupit)
#resultat = 4

#zadanie 4
number = 16
kvadrat = number ** 2
print (round(kvadrat, 2))

kub = number ** 3
print (round (kub))

koren = number ** 0.5
print (round(koren))

#zadanie 5
schet = 50
procent = 10

chaevye = schet * (procent / 100)
print (chaevye)

itog = schet + chaevye
print (round(itog,2))

na_troih = itog / 3
print (round(na_troih, 2))