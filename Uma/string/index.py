word = "Человеколюбие"
print(word[0])  #выводит значение под индексом слева направо
print(word[5])
print(word[8])
print(word[12])
print(word[-1])
print(word[-5]) #выводит индекс справа налево при - 


t = "hello"
print(t[0:3]) #когда мы говорим 0:3 это значит вывести 3 элемента начиная с 0



text = "У У У У У меня зовут Ума, мне 23 года"
#in - позволяет искать подстроку в тескте. Возвращает bool.
correct_name = "Ума" in text
print(correct_name)
incorrect_name = "Света" in text
print(incorrect_name)

# is not - отсутсвие чего-либо в тексте 
incorrect_name = "Света" is not text
print(incorrect_name)


# .find() - где находится (индекс первого символа)
finded_index = text.find("у")
print(finded_index)
bukva = text[finded_index]
print(bukva)
bukva_plus_one = text[finded_index + 1]
print(bukva_plus_one)

finded_name = text.find("Ума")
print(finded_name)


# if else - это условные циклы, выполняют код в зависимости от выполнения условия
# if 5>3: 
#     print ("bolshe")
# else: 
#     print ("menshe")

pravda = 5>3
print(pravda)

if pravda: 
    print ("bolshe")
else: 
    print ("menshe")

email = "ferzulka@mail.ru"
if "@" in email:
    print("кажется это настоящий email")
else:
    print("это не настоящий email")


sentence = input("Введите предложение в котором нужно искать слово: ")
name_to_find = input("Слово которое нужно найти: ")
name_to_replace = input("Слово на которое нужно поменять: ")
novaya = len(sentence)

if name_to_find in sentence:
    sentence = sentence.replace(name_to_find, name_to_replace)
    print(sentence)
else: 
    print(f"{name_to_find} не найдено")

lenght_sentence = len(sentence)
print(f"Длина вашего первоначального предложени: {novaya}")
print(f"Длина вашего конечного предложени: {lenght_sentence}")
