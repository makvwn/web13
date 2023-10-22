# Ввод строки
input_text = input("Введите текст: ")

# Инициализация пустого списка для хранения содержимого скобок
result = []

while '(' in input_text:
    # Находим позиции открывающей и закрывающей скобок
    start_index = input_text.find('(')
    end_index = input_text.find(')')

    # Добавляем содержимое скобок в результат
    result.append(input_text[start_index + 1:end_index])

    # Обновляем строку, удаляя текущее содержимое скобок
    input_text = input_text[:start_index] + input_text[end_index + 1:]

# Вывод результата
for item in result:
    print(item)