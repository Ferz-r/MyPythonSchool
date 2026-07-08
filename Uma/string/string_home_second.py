print("=== Задание 'Визитка' ===")

first_name = "ферз"
last_name = "ПеТроВиЧ"
age = 33
city = "москва"


first_name = first_name[0].upper() + first_name[1:].lower()
last_name = last_name[0].upper() + last_name[1:].lower()
city = city[0].upper() + city[1:].lower()

print(f"""Визитка:
Имя: {first_name}
Фамилия: {last_name}
Возраст: {age}
Город: {city}
""")




print("===Задание 'Инициалы'===")

full_name = "гаджимурад шамильевич абдурасулов"
words = full_name.split()
print(words)
initials = ".".join(word[0].upper() for word in words) + "."
print("Инициалы:", initials)



print("===Задание'Секретный пароль'===")

password = "SuperSecret123!"
dlina = len(password)
print(f"Длина пароля: {dlina}")

scritii = "*" * dlina
print(f"Скрытый пароль: {scritii}")



print("===Задание 'Домен почты'===")

email = "   FERZulkA@Mail.ru   "
email = email.strip().lower()

finded_index = email.find("@")+1
domen = email[finded_index:]
print(domen)



print("===Задание'Палиндром'===")

word1 = "казак"
word2 = "привет"
# print(word2[::-1])
sravnenie = word1==word1[::-1]
print(sravnenie)
sravnenie = word2==word2[::-1]
print(sravnenie)



print("===Задание'Форматирование даты'===")

date_iso = "2026-07-06"

year = date_iso[0:4]
mounth = date_iso[5:7]
day = date_iso[8:10]

date_result = f"{day}.{mounth}.{year}"
print(date_result)




print("===Задание'Жёсткая цензура'===")

review = "Этот ресторан — полное говно, а не еда. Повторю: говно!"
review = review[:1]+ review[1:].lower().replace("говно","***")
print(review)




print("===Задание'Очистка телефона'===")

phone_raw = "+7 (999) 123-45-67"
phone_raw = (phone_raw
                .replace(" ","")
                .replace("(", "")
                .replace(")","")
                .replace("-","")
            )
print(phone_raw)




print("===Задание'Подсчёт гласных'===")

text = "Мама мыла раму"
text_count = text.count("а")
print(f"Буква 'а' встречается: {text}")






print("===='Счастливый билет'===")

ticket = "481722"

first_p= ticket[0:3]
print(first_p)

second_p = ticket[3:6]
print(second_p)

# first_p = int(first_p)
# second_p = int(second_p)
# sum = first_p + second_p 
# print(sum)


first_sum = sum(int(digit) for digit in first_p)
second_sum = sum(int(digit) for digit in second_p)

# 3. Сравниваем суммы
if first_sum == second_sum:
    print(f"Билет {ticket} — счастливый 🍀")
else:
    print(f"Билет {ticket} — несчастливый 😢")

# 'счастливый 🍀' if first_sum == second_sum else 'несчастливый 😢'



print("===='Анонимайзер документов'===")

document = "Пациент Иван Иванов, паспорт 4500 123456, диагноз: COVID-19"
start = document.index("паспорт ") + len("паспорт ") 
end = document.index(",", start)
 
passport_data = document[start : end]
print(passport_data)
new_doc = document.replace(passport_data, "**** ******" ).replace("COVID-19", "ОРВИ")

print(new_doc)




print("===='Капитализация имени'===")

name = "аЛександР"
first_index = name[0].upper() + name[1:].lower()
print(first_index)


