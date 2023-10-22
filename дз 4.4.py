# Ввод строки с текстом и символа для удвоения
input_string = input("Введите строку с текстом: ")
character_to_double = input("Введите символ для удвоения: ")

# Используем метод replace для удвоения символа в тексте
result_string = input_string.replace(character_to_double, character_to_double * 2)

# Вывод результата
print(result_string)