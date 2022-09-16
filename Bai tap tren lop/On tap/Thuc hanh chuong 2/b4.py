n = int(input('Enter n = '))
s1 = 0; s2 = 0; s = 0

for i in range(1, n + 1):
    s1 += 1 / float((i * (i + 1)))
    s += i
    s2 += 1 / float(s)

print(f's1 = {round(s1, 2)}, s2 = {round(s2, 2)}')
