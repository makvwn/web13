# Ввод строки
input_string = input("Введите строку: ")

# Подсчет символов 'x' и 'y' в строке
count_x = input_string.count('x')
count_y = input_string.count('y')

# Формирование строки с результатом
result_string = f'x: {count_x}, y: {count_y}'

# Вывод результата
print(result_string)