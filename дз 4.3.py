# Ввод списка чисел и степени
input_numbers = input("Введите список чисел через пробел: ").split()
n = int(input("Введите степень: "))

# Преобразование элементов списка в целые числа
numbers = [int(x) for x in input_numbers]

# Возведение чисел в заданную степень и создание нового списка
result = [num ** n for num in numbers]

# Вывод результата
print(result)