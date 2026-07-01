print("===Задание чистое имя===")

input_name = "\t    ГаДжиМурад     \n"   

print(input_name.strip())
print(input_name.lower())
print(input_name.upper())


print("===задание цензура===")

censor_text = """Сегодня всё началось плохо, погода плохо,
и настроение тоже плохо. Но потом мне исправили оценку, и стало все так же плохо!"""
censor_text=censor_text.replace("плохо", "хорошо")
print(censor_text)



print("===email-валидатор===")

# email = "   FERZulkA@Mail.ru"
# print(email.strip())
# print(email.lower())
# print(email.replace("mail.ru","yandex.ru"))

email = "   FERZulkA@Mail.ru"
print(1,email)
email= email.strip()
print(2,email)
email= email.lower()
print(3,email)
email=email.replace("mail.ru","yandex.ru")
print(4,email)
print(email)



print("===скидка в магазине===")

price = 723412
discount = 25
razmer_discount = round(price*discount/100,2)
total_summ = price - razmer_discount

print(f"summa discount:{razmer_discount}")
print(f"itog price with discount:{total_summ}")



print("===перевод времени===")


minute = 1231
result = minute // 60
ostatok = minute % 60
print(f"poluchilos celih chasov:{result}")
print(f"ctolko minut stay:{ostatok}")







