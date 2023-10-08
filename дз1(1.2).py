def average_and_round(number1, number2):
    average = (number1 + number2) / 2
    rounded_average = round(average)
    return rounded_average
num1 = 4
num2 = 2
result = average_and_round(num1, num2)
print(f"Среднее арифметическое и округленное значение: {result}")