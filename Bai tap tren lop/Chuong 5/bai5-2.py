
def line(n):
    for i in range(n):
        print(end = '-')
    print()

def enter(n):
    dic = {}
    for i in range(n):
        k = input(f'  - Nhập họ tên đầy đủ NV {i+1}: ')
        v = input(f'  - Hãy nhập quê quán: ')
        dic.update({k : v})
    return dic

def show(dic):
    line(40)
    for k, v in dic.items():
        print(f'{k}  -  {v}')
    line(40)
    
def cut_name(s):
    lst = s.split()
    return lst[len(lst)-1]

def count_name(dic):
    count = 0
    for k, v in dic.items():
        name = cut_name(k)
        if name == 'Nam' and v == 'Ha Noi':
            count += 1
    return count

def update_nv(dic, n):
    for i in range(n):
        k = input(f'  - Nhập họ tên đầy đủ NV {i+1}: ')
        v = input(f'  - Hãy nhập quê quán: ')
        dic.update({k : v})


def main():
    # n = int(input('Số nhân viên cần nhập là: '))
    # dic = enter(n)
    dic = {'Bui Quang Vinh': 'Quang Ninh', 'Dang Thi Thu Trang': 'Nam Dinh', 'Lionel Messi': 'Ha Noi',
           'Dao Hai Nam': 'Ha Noi', 'Nam Nam': 'Ha Noi'}
    show(dic)
    
    count = count_name(dic)
    if count == 0:
        print('Không có nhân viên nào có tên là \'Nam\' và quê quán ở \'Ha Noi\' ')
    else:
        print(f'Có {count} nhân viên có tên là \'Nam\' và quê quán ở \'Ha Noi\' ')
    line(40)
        
    lc = input('Bạn có muốn thêm nhân viên vào danh sách không? (C\K): ')
    if lc == 'C' or lc == 'c':
        m = int(input('Số nhân viên cần thêm là: '))
        update_nv(dic, m)
        line(40)
        print(f'Đã thêm {m} nhân viên. Danh sách hiện tại là: ')
        show(dic)
    else:
        print('Thanks!!!')
    
    
if __name__ == '__main__':
    main()