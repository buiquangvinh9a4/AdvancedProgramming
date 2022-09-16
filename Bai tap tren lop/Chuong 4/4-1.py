def enter():
    n = int(input('Enter n = '))              # Nhập n với điều kiện 0 < n < 1000
    while not (0 < n < 1000):
        n = int(input('ReEnter n = '))
    return n

A = []                        # Tạo danh sách A trống

def enter_list(A, n):
    for i in range(n):            # Nhập dãy n số thực  
        x = float(input(f'- Enter A[{i}]= '))
        A.append(x)
    return A

n = enter()


min_list = min(A)             # Tìm giá trị bé nhất của dãy
max_list = max(A)             # Tìm giá trị lớn nhất của dãy

min2_list = max_list         # Gán giá trị bé thứ hai của dãy cho max

for i in range(n):            # Tìm giá trị bé thứ hai
    if min2_list > A[i] and A[i] != min_list:
        min2_list = A[i]
        
max2_list = min_list          # Gán giá trị lớn thứ hai của dãy cho min


for i in range(n):            # Tìm giá trị lớn thứ hai
    if max2_list < A[i] and A[i] != max_list:
        max2_list = A[i]

print(f'Min_2 of list = {min2_list}, Max_2 of list = {max2_list}')      # hiển thị ra min2 và max2

print(f'First List = {A}')                 # hiển thị dãy ban đầu

for i in range(n):                         # nhân 2 với phần tử chẵn trong dãy
    if A[i] % 2 == 0:
        A[i] *= 2

print(f'After List = {A}')                # hiển thị dãy sau khi nhân 2 với phần tử chẵn