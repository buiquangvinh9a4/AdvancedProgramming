n = float(input('Nhập điểm trung bình: '))

if n >= 8.0:
    print('Giỏi')
elif n >= 6.0 and n < 8.0:
    print('Khá')
elif n >= 5.0 and n < 6.0:
    print('Trung bình')
else:
    print('Yếu')