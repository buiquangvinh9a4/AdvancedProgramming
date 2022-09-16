n = int(input())

def nua_tren(n):
    for i in range(0, n):
        for j in range(0, i + 1):
            if j == 0:
                print('*', end = '')
            else:
                print('**', end = '')
        print()

nua_tren(n)

def nua_duoi(n):
    for i in range(n, 1, -1):
        for j in range(i, 1, -1):
            if j == i:
                print('*', end = '')
            else:
                print('**', end = '')
        print()

nua_duoi(n)
