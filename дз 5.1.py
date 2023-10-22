n = int(input("Введите количество городов: "))
cities = []

# Считываем названия городов и сохраняем их в списке
for i in range(n):
    city = input("Введите название города: ")
    cities.append(city)

# Создаем словарь для подсчета повторяющихся городов
city_counts = {}

# Подсчитываем количество каждого города
for city in cities:
    if city in city_counts:
        city_counts[city] += 1
    else:
        city_counts[city] = 1

# Находим количество городов с повторяющимися названиями
count_of_duplicates = 0
for count in city_counts.values():
    if count > 1:
        count_of_duplicates += 1

print("Количество городов с повторяющимися названиями:", count_of_duplicates)