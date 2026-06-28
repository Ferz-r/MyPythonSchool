t = "  huhvuigu YFYUTFUFVUYyftytfuhfuyFUYF \n \t"
print(t)

# Методы строк
print("strip обрезает лишние пробелы, знаки табуляции и переноса строки в начале и в конце строки!!")
t.strip()
print(t.strip())

print("lower переводит всю строку в нижний регистр")
t.lower()
print(t.lower())

print("upper переводит всю строку в ВЕРХНИЙ регистр")
t.upper()
print(t.upper())

print("replace меняет одно значение текста на другое")
t.replace("","")
print(t.replace("huhvuigu","hello"))



text = """\t \n ==hello 
wolrd
human my love
my SOUL
End==

"""


print(text.strip())
print(text.lower())
print(text.upper())


sentence = "\n   Мы ЖИВЕМ в городе МОСква \n"
print(1, sentence)
#  print(sentese.lower().strip())
sentence = sentence.strip()
print(2, sentence)
sentence = sentence.lower()
print(3, sentence)
sentence = sentence.replace("москва", "Нью-Йорк")
print(4, sentence)