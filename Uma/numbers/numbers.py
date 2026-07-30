#zadanie1
print("===zadanie1===")
rasstoinie = 268
speed = 80
rashod = 17
price = 70

time_hour = rasstoinie / speed
rashod_za_km = rashod/100
total_oil=rashod_za_km*rasstoinie


print(f"время в часах: {time_hour}")
print(f"время в минутах: {round(time_hour * 60)}")
print(f"топливо потребуется: {total_oil}")
print(f"стоимость топлива за всю поездку: {round(total_oil*price,2)}")



#zadanie2
print("===zadanie2===")
rubli = 25000
exchange = 75


dollar =  rubli//exchange
dollar_with_cent = rubli/exchange
cent = int(round(dollar_with_cent-dollar,2)*100)

print(f"poluchilos v dollarah:{dollar}")
print(f"ostalos centov:{cent}")





#zadanie3
print("===zadanie3===")
konfeti = 63
deti = 6

result = konfeti//deti
ostatok = konfeti%deti
dokupit = deti-ostatok


print(f"poluchilos kazhdomu rebenku:{result}")
print(f"konfet ostalos:{ostatok}")
print(f"dokupit detyam porovnu:{dokupit}")



#zadanie4
print("===zadanie4===")
number = 34
kvadrat = number**2
kub = number**3
koren = round(number**0.5,2)

print(f"number v kvadrate:{kvadrat}")
print(f"number v kube:{kub}")
print(f"number v koren:{koren}")



#zadanie5
print("===zadanie5===")
schet = 1335
chaevie = 2.5
razmer_chaevih = round(schet*chaevie/100,2)
total_summ = schet + razmer_chaevih
razdelit = round(total_summ / 3,2)

print(f"razmer chaevih:{razmer_chaevih}")
print(f"itogovaya summa:{total_summ}")
print(f"na 3 cheloveck:{razdelit}")



print("=======")


