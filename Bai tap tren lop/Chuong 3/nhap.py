n = int(input('Nhập vào năm: '))

if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0:
    print('Năm nhuận')
else:
    print('Không là năm nhuận')