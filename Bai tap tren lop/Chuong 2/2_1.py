name1 = input('Nhập vào họ tên người 1: ')
age1 = int(input('Nhập vào tuổi người 1: '))
name2 = input('Nhập vào họ tên người 2: ')
age2 = int(input('Nhập vào tuổi người 2: '))

if age1 < age2:
    print(f'{name1} trẻ hơn {name2}.')
elif age1 > age2:
    print(f'{name1} già hơn {name2}.')
else:
    print(f'{name1} và {name2} bằng tuổi nhau.')