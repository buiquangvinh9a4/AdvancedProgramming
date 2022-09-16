
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if (a > 0) and (b > 0) and (c > 0) and (a + b > c) and (a + c > b) and (b + c > a):
    if (a == b) or (b == c) or (a == c) :
        if a == b == c:
            print('Tam giác đều')
        else:
            print('Tam giác cân')
    else:
        print('Tam giác thường')
else:
    print('Đây không phải là tam giác')