
import math

def enter():                    # hàm nhập 1 số nguyên
    n = int(input())
    return n

def line(n):
    for i in range(n):
        print(end = '-')
    print()

def enter_list_of_list(n, m):   # hàm nhập danh sách 2 kích thước n x m
    A = []
    print('Enter list: ')
    for i in range(n):
        A.append([])
        for j in range(m):
            x = int(input())
            A[i].append(x)
    return A

def print_list_of_list(A, n, m):      # hàm in ra danh sách 2 kích thước n x m
    for i in range(n):
        for j in range(m):
            print(A[i][j], end = ' ')
        print()
    line(10)

def sum_k(A, n, k):                  # hàm tính tổng cột K của danh sách
    s = 0
    for i in range(n):
        s += A[i][k]
    return s

def matrix_swap(A, n, m):            # hàm hoán vị cột dòng của danh sách, trả về danh sách đã hoán vị
    B = []                         
    for i in range(m):
        B.append([])
        for j in range(n):
            x = A[j][i]
            B[i].append(x)
    return B

def prime_number(n):                 # hàm kiểm tra số nguyên tố
    if n < 2:
        return False
    else:
        k = int(math.sqrt(n))
        for i in range(2, k + 1):
            if n % i == 0:
                return False
    return True
            

def main():
    n = int(input('- Enter n = '))
    m = int(input('- Enter m = '))
    
    line(10)
    
    A = enter_list_of_list(n, m);   # nhập list A, in ra list A
    line(10)  

    k = int(input('- Enter k = '))
    print(f'Sum column K = {sum_k(A, n, k)}')
    
    line(10)
    
    B = matrix_swap(A, n, m)         # swap cột và dòng của list A gán cho B, in ra list A và B
    print('Before Matrix Swap: '); print_list_of_list(A, n, m)
    print('After Matrix Swap: '); print_list_of_list(B, m, n)
 
    count_nt1 = 0;
    NT = []
    for i in range(n):
        for j in range(m):
            if (prime_number(A[i][j])):
                count_nt1 += 1
                if A[i][j] not in NT:
                    NT.append(A[i][j])

                    
    # print(f'COUNT prime_number = {count_nt1}')
    # print(f'COUNT prime_number = {len(NT)}')
    
    

    
    
    # B = matrix_out(A, n, m)
    # print_list_of_list(B, m, n)
    
    
    
        
    
    
    # print_list_of_list(A, n, m)
    # print(sum_k)

if __name__ == '__main__':
    main()