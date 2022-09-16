#VD4-1: Chương trình quản lý danh bạ
danhba = {}
i = 0
while True:
    i += 1
    print(f'Nhập thông tin thứ {i}:')
    hoten = input('\t Họ tên: ')
    sdt = input('\t Số điện thoại: ')
    danhba.update({hoten:sdt})
    ch = input('Bạn có muốn tiếp tục (C/K): ')
    if ch == 'K' or ch == 'k':
        break
    
print(f'Tong so nguoi trong danh ba: {len(danhba)}')

danhba_sx = sorted(danhba) 

print('Danh ba sau khi sap xep:')
print(danhba_sx)

shoten = input('Bạn cần tìm tên nào: ')
print('Thông tin tìm thấy: ')
d = 0
for k in danhba.keys():
    if shoten == k:
        print(f'\t{k} - {danhba.get(k)}')
        d += 1

print(f'Tim thay {d} ten trong danh ba')

ssdt = input('Bạn cầm tìm số điện thoại: ')
print('Thông tin tìm thấy: ')
d = 0
for k, v in danhba.items():
    if ssdt in v:
        print(f'\t{k} - {v}')
        d += 1

print(f'Tìm thấy {d} số điện thoại trong danh bạ')