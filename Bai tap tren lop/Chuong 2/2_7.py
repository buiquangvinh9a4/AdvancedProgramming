from math import sqrt

# nhập dữ liệu
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))


# kiểm tra tam giác
if (a > 0) and (b > 0) and (c > 0) and (a + b > c) and (a + c > b) and (b + c > a):
    p = (a + b + c) / 2
    S = sqrt(p * (p - a) * (p - b) * (p - c))
    r = S / (a + b + c)
    R = (a * b * c) / (4 * S)

    print(f'Diện tích tam giác S = {S: .4f}')
    print(f'Bán kính đường tròn nội tiếp tam giác = {r: .4f}')
    print(f'Bán kính đường tròn ngoại tiếp tam giác = {R: .4f}')
else:
    print('Đây không phải là tam giác')