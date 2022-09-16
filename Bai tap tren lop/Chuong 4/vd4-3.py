# VD 4-3:

def line(n):              # in ra đường kẻ line
    for i in range(n):
        print(end = '-')
    print()

def insert_dic(n):        # nhập danh sách n mặt hàng vào dic
    dic = {}
    for i in range(1, n + 1):
        name = input(f' - Nhập tên mặt hàng {i}: ')
        money = int(input(f' - Giá của {name} là: '))
        dic.update({name: money})
    return dic

def print_dic(dic):        # in danh sách n mặt hàng
    line(40)
    print('Danh sách mặt hàng là: ')
    for name, money in dic.items():
        print(f'{name} - {money}')
    line(40)

def max_money(dic):        # tìm hàng có giá cao nhất            # có thể use hàm sorted và popitem()
    max_v = max(dic.values())
    for k, v in dic.items():
        if v == max_v:
            print(f'Hàng có giá bán cao nhất: {k} - {v}')
            break

def min_money(dic):         # tìm hàng có giá thấp nhất         # có thể use hàm sort reverse = True và 
    min_v = min(dic.values())
    for k, v in dic.items(): 
        if v == min_v:
            print(f'Hàng có giá bán thấp nhất: {k} - {v}')
            break
        
def count_G(dic, g1, g2):       # đếm hàng có giá trị không thấp hơn g1 
    count_g = 0
    for v in dic.values():
        if v >= g1 and v <= g2:
            count_g += 1
    return count_g





def main():
    n = int(input('Nhập số mặt hàng: '))
    # hh = {'Bim bim': 20000, 'Sữa': 5000, 'Kẹo mút': 1694}
    
    hh = insert_dic(n)
    
    print_dic(hh)
    
    max_money(hh)
    min_money(hh)
    line(40)
    
    
    g1 = float(input('Nhập số thực 1: '))

    while True:
        g2 = float(input('Nhập số thực 2: '))
        if g1 < g2:
            break
        else:
            print(f'{g1} >= {g2}, vui lòng nhập lại!')
    
    # thấp hơn g2, cao hơn g1
    count_g = count_G(hh, g1, g2)
    
    line(40)
    print(f'Có {count_g} mặt hàng không thấp hơn {g1} và không cao hơn {g2}')
    line(40)
    
    k = int(input('Nhập thêm k mặt hàng: '))
    hh_2 = insert_dic(k)
    
    line(40)
    print(f'Đã update thêm {k} mặt hàng, danh sách mới sẽ là: ')
    hh.update(hh_2)
    print_dic(hh)
    
    
    
    
if __name__ == '__main__':
    main()