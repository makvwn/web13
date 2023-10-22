# Чтение фамилий школьников, решивших задачи по разным предметам
algebra_students = set(input().split())
geometry_students = set(input().split())
trigonometry_students = set(input().split())

# Находим пересечение множеств школьников, которые решили все задачи
students_solved_all = algebra_students & geometry_students & trigonometry_students

# Выводим фамилии учащихся, решивших все задачи, в алфавитном порядке через пробел
if students_solved_all:
    sorted_students = sorted(students_solved_all)
    print(" ".join(sorted_students))
else:
    print("Все три задачи никто не решил")