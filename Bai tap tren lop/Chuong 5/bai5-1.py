

def nhap(n):
    s = input(f'Nhập vào câu {n}: ')
    return s

def trung_nhau(s1, s2):
    lst = []
    for i in s1:
        for j in s2:
            if i == j:
                lst.append(i)
    return lst
    
def max_string(s):
    max = len(s[0])
    for i in s:
        if max < len(i):
            max = len(i)
    for i in s:
        if max == len(i):
            print(f'Từ dài nhất có mặt trong cả hai xâu là: {i}')
            break
        

def main():
    s1 = nhap(1)
    s2 = nhap(2)
    lst1 = s1.split()
    lst2 = s2.split()
    lst3 = trung_nhau(lst1, lst2)
    max_string(lst3)
    
if __name__ == '__main__':
    main()