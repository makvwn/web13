count = int(input("Введите количество городов: "))
cities = []

for i in range(count):
    cities.append(input("Введите название города: ").capitalize())

result = 0
for i in range(count):
    cities_repeat = 0
    city = cities[i]
    for j in range(i, count):
        if city == cities[j]:
            cities_repeat += 1
    if cities_repeat > 1:
        result += cities_repeat

print(result)
