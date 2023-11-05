from math import sqrt

n = int(input("n = "))
primes = []
if n < 2:
    pass
else:
    for i in range(2, n):
        if i % 2 == 0:
            pass
        else:
            f = True
            for j in range(2, int(sqrt(i)) + 1):
                if i % j == 0:
                    f = False
                    break
            if f:
                primes.append(i)
print(primes)