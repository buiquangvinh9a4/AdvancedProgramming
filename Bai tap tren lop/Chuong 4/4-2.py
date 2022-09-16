def enter():
    n = int(input('Enter n student = '))
    while not (0 < n < 100):
        n = int(input('ReEnter n student = '))
    return n

def enter_list_name(n):
    A = []
    for i in range(n):
        x = input()
        A.append(x)
    return A

def enter_list_score(n):
    A = []
    for i in range(n):
        x = float(input())
        A.append(x)
    return A

def average_score(A):
    return sum(A) / len(A)
    
def rank_student(n):
    if 8.0 <= n <= 10:
        return 4
    elif 6.0 <= n < 8.0:
        return 3
    elif 5.0 <= n < 6.0:
        return 2
    return 1

def score_max(A, B, n):
    max_score = max(A)
    S = None
    for i in range(n):
        if A[i] == max_score:
            S = B[i]
    return S

def score_min(A, B, n):
    min_score = min(A)
    S = None
    for i in range(n):
        if A[i] == min_score:
            S = B[i]
    return S

def main():
    n = enter()
    B = enter_list_name(n)
    A = enter_list_score(n)

    ave_score = average_score(A)
    print(f'Average Score = {ave_score}')


    max_name = score_max(A, B, n)
    min_name = score_min(A, B, n)
    print(f'Max Student = {max_name}')
    print(f'Min Student = {min_name}')


    X = [0, 0, 0, 0]
    for i in range(n):
        if rank_student(A[i]) == 4:
            X[0] += 1
        elif rank_student(A[i]) == 3:
            X[1] += 1
        elif rank_student(A[i]) == 2:
            X[2] += 1
        else:
            X[3] += 1

    print(f'G = {X[0]}, K = {X[1]}, TB = {X[2]}, Y = {X[3]}')

if __name__ == '__main__':
    main()

def Kiem_tra(n):
    if(n >= 8.0):
        return 1
    elif(n >= 6.0):
        return 2
    elif (n >= 5.0):
        return 3
    else:
        return 4
    
def Tong_Gioi(a, n):
    sum = 0
    for i in range(n):
        if (Kiem_tra(a[i]) == 1):
            sum += 1
    return sum