# Получить ввод от пользователя
num1, num2 = map(int, input("Введите два числа, разделенных пробелом: ").split())

# Определить большее число
if num1 > num2:
    print(num1)
else:
    print(num2)