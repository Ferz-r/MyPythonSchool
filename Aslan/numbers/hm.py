# One exercise
print("ПЕРВОЕ ЗАДАНИЕ")
distance = 120
avg_speed = 79
fuel_consumption = 5.7
fuel_price = 119

travel_time = distance / avg_speed
travel_time_hour = round(travel_time, 1)
travel_time_min = round(travel_time * 60)
lost_fuel = round(distance / 100 * fuel_consumption, 2)
total_price = round(lost_fuel * fuel_price)

result_info = (
    f"Время в пути составит {travel_time_hour} часа или {travel_time_min} мин. \
    \nВы потратите {lost_fuel} л бензина, что в деньгах: {total_price}р."
)

print(result_info)


# Two exercise
print("ВТОРОЕ ЗАДАНИЕ")
rubles = 1000
exchange = 80.33

dollars = rubles // exchange
dollars_with_cents = rubles / exchange
cents = int(round(dollars_with_cents - dollars, 2) * 100)

print(f"Вы получите ${dollars} и ¢{cents}")

# Three exercise
print("ТРЕТЬЕ ЗАДАНИЕ")
candies = 43
childrens = 15

each_children = candies // childrens
ostatok = candies % childrens
dokupit = childrens - ostatok
print(
    f"Каждому ребенку достанутся конфеты - {each_children} шт. \
    \nКонфет останется - {ostatok} шт.\
    \nДокупить конфет - {dokupit} шт."
)

# Four exercise
print("ЧЕТВЕРТОЕ ЗАДАНИЕ")
num = 12

square = num**2
cube = num**3
square_root = round(num**0.5, 2)

print(square)
print(cube)
print(square_root)

# Five exercise
print("ПЯТОЕ ЗАДАНИЕ")
summ = 3400
tips = 0.25
guests = 3

tips_result = summ * tips
total_summ =summ + tips_result
total_sum_divided_by_guest = round(total_summ / guests, 2)

print(
    f"Сумма чека без чаевых {summ} р.\
    \nИтоговая сумма чека {total_summ}р, включая чаевые {tips_result}р.\
    \nСумма к оплате, с учетом {guests} гостей составляет {total_sum_divided_by_guest}р с каждого"
)
