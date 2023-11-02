numbers = [ 13, 26, 39, 52, 64, 78, 92, 19, 38, 58, 76, 95, 114]
result = list(filter(lambda x: (x%13 == 0) or  (x%19 == 0), numbers)) 
print(result)