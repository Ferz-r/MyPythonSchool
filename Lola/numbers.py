x = 11
y = 2
z = 32.12

print(f"summary: {x + y + z} \n minus {x - y}")

multiply = x * y
divide = x / y

print("umnozhenie", multiply)
print(type(multiply))

print("delenie", divide)
print(type(divide))

divide_without_float = x // y
print("divide_without_float", divide_without_float)
print(type(divide_without_float))

ostatok = x % y
print("ostatok", ostatok)
print(type(ostatok))

stepen = x ** y
print("stepen", stepen)
print(type(stepen))

print(z)
z = "privet"  # поменяла значение переменной
print(z)

z = 16.124566
y = 13.822345
print(round(z))  # option+shift+vniz, copiruet
print(round(y))
# okruglenie = 16 , 14

print(round(z, 1))  # столько цифр округления , сколько мы указали после ,
print(round(y, 3))