n = int(input())

for i in range(n):
    for j in range(i + 1):
        if j == 0:
            print('*', end = '')
        else:
            print('**', end = '')
    print()

for i in range(n, 1, -1):
    for j in range(i, 1, -1):
        if j == i:
            print('*', end = '')
        else:
            print('**', end = '')
    print()
