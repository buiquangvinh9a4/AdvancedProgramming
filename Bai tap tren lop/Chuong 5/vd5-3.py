

def nhap():
    s = input('Cho biết một xâu: ')
    return s

def so_tu(s):
    list = []
    for i in range(len(s)):
        x = len(s[i])
        if x not in list:
            list.append(x)
    return list


def thong_ke(s):
    dic = {}
    key = so_tu(s)
    for i in range(len(key)):
        k = []
        for j in range(len(s)):
            if len(s[j]) == key[i]:
                if s[j] not in k:
                    k.append(s[j])
        dic.update({key[i]:k})
    return dic
            
def in_dic(dic):
    for k, v in dic.items():
        print(f'{k} : {v}')

def main():
    # s = nhap()
    s = "ha noi mua nay vang nhung con mua cai ret dau dong"
    print('Xâu đã nhập: ')
    print(s)
    print('Kết quả là: ')
    s1 = s.upper()
    a = s1.split()
    dic = thong_ke(a)
    dic_sort = sorted(dic.items())
    in_dic(dict(dic_sort))
    
if __name__ == '__main__':
    main()
    
#----------------------------------------------------------------------------
# Cách 2:
content = input('Cho biết một xâu: ')
groups = {}

words = content.split()

for word in words:
    word = word.upper()
    size = len(word)
    
    if size in groups:
        if word not in groups[size]:
            groups[size] += [word]
    else:
        groups[size] = [word]

print('Xâu đã nhập:')
print(content)
print('Kết quả là: ')
lstsize = sorted(groups.keys())

for size in lstsize:
    print(size,': ', groups[size])