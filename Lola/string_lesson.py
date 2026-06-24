pervyi = """ \t \n
                   What is Lorem Ipsum?
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since 1966, when designers at Letraset and James Mosley, the librarian at St Bride Printing Library in London, took a 1914 Cicero translation and scrambled it to make dummy text for Letraset's Body Type sheets. It has survived not only many decades, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised thanks to these sheets and more recently with desktop publishing software including versions of Lorem Ipsum.

Why do we use it?
It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).
\n
"""
# Методы строк
# .strip()
# .lower()
# .upper()
# .replace("", "")

print(pervyi)
print(".strip")
# print(pervyi.strip())  # удаляет ненужные пробелы ВНАЧАЛЕ и в КОНЦЕ предложения, а также удаляет перенос строки
# \n - перенести строку

print(".lower")
print(pervyi.lower())  # меняет ВСЕ на маленькую букву

print(".upper")
print(pervyi.upper())  # меняет ВСЕ на большую букву

sentence = "Lola is walking in the park"
print(sentence)

print("====.replace===")
sentence = sentence.replace("Lola", "Umka")  # создаем новую переменную (не заменяет текст)
print(sentence)

print("===.replace===")
sentence = sentence.replace("park", "home")
print(sentence)

# заменили исходный текст = перезаписали ИСХОДНУЮ переменную (sentence)

