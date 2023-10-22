def are_anagrams(str1, str2):
    # Удаляем пробелы и преобразуем строки в нижний регистр
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Сравниваем множества уникальных символов
    return set(str1) == set(str2)

# Получаем ввод от пользователя
input_str1 = input("Введите первую строку: ")
input_str2 = input("Введите вторую строку: ")

# Проверяем, являются ли строки анаграммами
if are_anagrams(input_str1, input_str2):
    print("Строки являются анаграммами.")
else:
    print("Строки не являются анаграммами.")