import math
n = int(input('Enter n = '))
x = float(input('Enter x = '))

s1 = 0; s2 = x

for i in range(1, n + 1):
    s1 += pow(x, 2 * i)
    s2 += pow(x, 2 * i + 1)

print(f's1 = {round(s1, 2)}, s2 = {round(s2, 2)}')