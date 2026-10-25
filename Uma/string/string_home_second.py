print("====Задание 1 — «Капитализация имени»====")

name = "аЛександР"
first_letter = name[:1].upper()
other_letters = name[1:].lower()
imya = first_letter + other_letters
print(imya)

#второй вариант в одну строчку
new = name[:1].upper() + name[1:].lower()
print(new)




print("====Задание 2 — «Визитка»====")

first_name = "ферз"
last_name = "ПеТроВиЧ"
age = 33
city = "москва"

new_first_name = first_name[:1].upper() + first_name[1:].lower()
new_last_name = last_name[:1].upper() + last_name[1:].lower()
new_city = city[:1].upper() + city[1:].lower()
print(f"""
Имя: {new_first_name}
Фамилия: {new_last_name}
Возраст: {age}
Город: {new_city}
""")



print("====Задание 3 — «Секретный пароль»====")

password = "SuperSecret123!"
new_password = len(password) 
scrit_password = new_password * "*"
print(f"""
Длина пароля: {new_password}
Скрытый пароль: {scrit_password}
""")



print("====Задание 4 — «Домен почты»====")

email = "   FERZulkA@Mail.ru   "
new_email = email.strip().lower()
finded_index = new_email.find("@") 
need_index = finded_index + 1
domen = new_email[need_index :] 
print(domen)




print("====Задание 5 — «Палиндром»====")

word1 = "казак"
word2 = "привет"

polindrom = word1[::-1] == word1
print(f"{word1} - полиндром: {polindrom}" )
polindrom = word2[::-1] == word2
print(f"{word2} - полиндром: {polindrom}" )



print("====Задание 6 — «Форматирование даты»====")

date_iso = "2026-07-06"

day = date_iso[8:]
mounth = date_iso[5:7]
year = date_iso[:4]

date = f"Дата: {day}.{mounth}.{year}"
print(date)



print("====Задание 7 — «Жёсткая цензура»====")

review = input("Напиши свой аналогичный отзыв о ресторане: Этот ресторан — полное говно, а не еда. Повторю: говно!:\n")

# print(review.replace("говно", "***").lower())
review = review[:1] + review[1:].lower().replace("говно", "***")
print(review)


print("===Задание 8 — «Очистка телефона====")

phone_raw = input("Введи свой номер телефона, на примере: +7 (999) 123-45-67:\n")

phone_raw = phone_raw.replace(" ","").replace("(","").replace(")","").replace("-","")
print(phone_raw)



print("====Задание 9 — «Подсчёт гласных»====")

text = "Мама мыла раму"

text = (text.count('а'))
itog = f"Букв 'а' встречаются : {text}"
print(itog)



print("====Задание 10 — «Анонимайзер документов»====")

document = input("Введите данные пациента в формате: Пациент Иван Иванов, паспорт 4500 123456, диагноз: COVID-19:\n")

document = "Пациент Иван Иванов, паспорт 4500 123456, диагноз: COVID-19"
start = document.index("паспорт ") + len("паспорт ") 
end = document.index(",", start)
 
passport_data = document[start : end]
print(passport_data)
new_doc = document.replace(passport_data, "**** ******" ).replace("COVID-19", "ОРВИ")

print(new_doc)
# document = document.replace("")