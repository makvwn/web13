def calculate_digit_sum(number):
    # Инициализируем переменную для хранения суммы
    digit_sum = 0
    
    # Проходим по каждой цифре в числе
    while number > 0:
        # Получаем последнюю цифру числа
        digit = number % 10
        
        # Прибавляем цифру к общей сумме
        digit_sum += digit
        
        # Убираем последнюю цифру числа
        number //= 10
    
    return digit_sum

# Запрашиваем у пользователя ввод числа
user_input = int(input("Введите число: "))

# Рассчитываем сумму цифр числа
result = calculate_digit_sum(user_input)

# Выводим результат
print("Сумма цифр числа", user_input, "равна", result)