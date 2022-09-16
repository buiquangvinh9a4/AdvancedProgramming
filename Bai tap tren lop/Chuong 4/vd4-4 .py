# VD 4-4:

def line(n):              # in ra đường kẻ line
    for i in range(n):
        print(end = '-')
    print()

def insert_dic(n, name):        # nhập danh sách n mặt hàng vào dic
    dic = {}
    print(f'Nhập thông tin cửa hàng {name}: ')
    for name in range(1, n + 1):
        name = input(f' - Nhập vào tên sách: ')
        if name not in dic.keys():
            dic[name] = 1
        else:
            dic[name] += 1
    return dic

def print_dic(dic, name):        # in danh sách n mặt hàng
    line(40)
    print(f'Thống kê số lượng sách bán được tại của hàng {name}: ')
    for k, v in dic.items():
        print(f'Quyển: {k} - {v}')
    line(40)
    



def main():
    n = int(input('Nhập số lượng sách bán được tại cửa hàng A: '))
    store_A = insert_dic(n, 'A')
    
    m = int(input('Nhập số lượng sách bán được tại cửa hàng B: '))
    store_B = insert_dic(m, 'B')
    
    print_dic(store_A, 'A')
    print_dic(store_B, 'B')
    
    store_A_sorted = sorted(store_A.items(), key = lambda x: x[1])
    store_B_sorted = sorted(store_B.items(), key = lambda x: x[1])
    print(store_A_sorted, 'A')
    print(store_B_sorted, 'B')
    
    temp = []
    for k1, v1 in store_A.items():
        for k2, v2 in store_B.items():
            if v1 > v2:
                if k1 not in temp:
                    print(f'Sách {k1}')
                    temp.append(k1)
    
    
    

    name_book = input('Nhập vào tên sách cần kiểm tra: ')
    count = 0
    for k, v in store_A.items():
        if name_book == k:
            count += v
    for k, v in store_B.items():
        if name_book == k:
            count += v
    print(f'Có {count} quyển sách {name_book} đã được bán')
    
    
   
    
    
    
if __name__ == '__main__':
    main()