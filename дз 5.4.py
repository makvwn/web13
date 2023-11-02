algebra = "Смирнов Сидоров Попов"
geometry = "Смирнов Сидоров Попов"
trigonometry = "Смирнов Сидоров Попов"

algebra = input().split()
geometry = input().split()
trigonometry = input().split()
allSolved = set(algebra) & set(geometry) & set(trigonometry)
for i in allSolved:
    print(i)
    print(" ")
if len(allSolved) == 0:
    print('Никто не решил все три задачи')