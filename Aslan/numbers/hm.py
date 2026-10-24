distance = 120
avg_speed = 79
fuel_consumption = 5.7
fuel_price = 119

travel_time = distance / avg_speed
travel_time_hour = round(travel_time, 1)
travel_time_min = round(travel_time * 60)
lost_fuel = round(distance / 100 * fuel_consumption, 2)
total_price = round(lost_fuel * fuel_price)

result_info = f"Время в пути составит {travel_time_hour} часа или {travel_time_min} мин. \
    \nВы потратите {lost_fuel} л бензина, что в деньгах: {total_price}р."

print(result_info)