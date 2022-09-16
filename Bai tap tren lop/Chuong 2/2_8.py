

def Sum_U(a):
    sum = 0
    for i in range(1, (a // 2) + 1):
        if a % i == 0:
            sum += i
    return sum


for i in range(2, 10 ** 6 + 1):
    x = Sum_U(i)
    if x <= 10 ** 6 and Sum_U(x) == i and x > i:
        print(i, x)


