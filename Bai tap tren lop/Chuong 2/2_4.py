import random

n1 = random.randint(0, 1)
n2 = random.randint(0, 1)
n3 = random.randint(0, 1)

print(f'An = {n1}, Bình = {n2}, Cường = {n3}')

if n1 != n2 and n1 != n3:
    print('An Win!')
elif n2 != n1 and n2 != n3:
    print('Bình Win!')
elif n3 != n1 and n3 != n2:
    print('Cường Win!')
else:
    print('Draw')

