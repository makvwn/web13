from functools import reduce

list1 = [-1, 2, 9, 0, 100]
print(reduce(lambda x, y: x if x > y else y, list1))