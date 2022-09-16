def count_x(s, x):
    count = 0
    for i in s:
        if i == x:
            count += 1
    return count

def thong_ke(s):
    dic = {}
    for i in s:
        if i not in dic.keys():
            dic[i] = 1
        else:
            dic[i] += 1
    return dic

def main():
    s = input('Nhập xâu s: ')
    x = input('Nhập kí tự x cần tìm: ')
    count = count_x(s, x)
    print(f'Có {count} kí tự {x} trong xâu.')
    dic = thong_ke(s)
    print('Tần suất xuất hiện của các kí tự trong xâu là: ')
    print(dic)

if __name__ == '__main__':
    main()



