def nhapdl(n):
    s = input(f'Nhập xâu thứ {n}: ')
    s1 = s.upper()
    return s1

def Dem_Dic(s):
    dic = {}
    for i in s:
        if i not in dic.keys():
            dic[i] = 1
        else:
            dic[i] += 1
    return dic

def in_dic(dic):
    for k, v in dic.items():
        print(f'{k} : {v}')
    
          
s1 = nhapdl(1)
s2 = nhapdl(2)
s3 = s1 + s2
dic = Dem_Dic(s3)
dic_sort = sorted(dic.items(), key = lambda x: x[1])
in_dic(dict(dic_sort))


