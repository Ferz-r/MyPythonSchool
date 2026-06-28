print("===Задание 1. Чистое имя===")

input_name = "\t    ГаДжиМурад     \n"

print(input_name.strip())
print(input_name.strip().lower())
print(input_name.strip().upper())

print("===Задание 2. Цензура===")

censor_text = """Сегодня всё началось плохо, погода плохо,
и настроение тоже плохо. Но потом мне исправили оценку, и стало все так же плохо!"""

print(censor_text.replace("плохо", "хорошо"))


print("===Задание 3. Email===")

email = "   FERZulkA@Mail.ru"
print(email)
print(email.strip())
print(email.strip().lower())
print(email.strip().replace("mail.ru", "yandex.ru"))

#тут мне выдавал итог - FERZulkA@Mail.ru , не меняя почту - проблема в том, что я не перезаписала переменную email, а просто вывела результат на экран. + у меня мэйл с большой буквы, а он ищет маленькую.
print("===Задание 3. Email===") # SECOND TRY

email = "   FERZulkA@Mail.ru"
email = email.strip().lower().replace("mail.ru", "yandex.ru")
print(email)

print("===Задание 4. Скидка===")

price = 723412
discount = 25

economia = price * discount / 100
precio_final = price - economia

print(round(economia, 2))
print(round(precio_final, 2))

#other_way
print(f"Экономия: {round(economia, 2)}")
print(f"Итоговая цена: {round(precio_final, 2)}")

print("===Задание 5. Минуты===")

minute = 1231

# //  → сколько целых
# %   → что осталось

hours = minute // 60
minutes = minute % 60

print(hours)
print(minutes)