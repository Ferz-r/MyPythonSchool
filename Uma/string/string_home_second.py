print("====Задание 1 — «Капитализация имени»====")

name = "аЛександР"
first_letter = name[:1].upper()
other_letters = name[1:].lower()
imya = first_letter + other_letters
print(imya)

#второй вариант в одну строчку
new = name[:1].upper() + name[1:].lower()
print(new)


