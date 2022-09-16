t = int(input('Nhập vào nhiệt dộ ngày hôm nay: '))

if t < 10 or t > 37:
    print('Hãy ở nhà!')
elif t > 20 and t < 30:
    print('Hãy đi chơi!')
elif t >= 10 and t <= 20:
    print('Hãy đi mua sắm!')
else:
    print('Hãy chơi game LOL!')