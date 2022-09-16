def quytac():
    dic = {'2' : ['A', 'B', 'C'], '3' : ['D', 'E', 'F'], '4' : ['G', 'H', 'I'],
        '5' : ['J', 'K', 'L'], '6': ['M', 'N', 'O'], '7' : ['P', 'Q', 'R', 'S'],
        '8' : ['T', 'U', 'V'], '9' : ['W', 'X', 'Y', 'Z']}
    return dic

def mahoa(s):
    dic = quytac()
    s1 = s.upper()
    s2 = ""
    for i in range(len(s1)):
        if s1[i] >= 'A' and s1[i] <= 'Z':
            for k, v in dic.items():
                if s1[i] in v:
                    s2 = s2 + k
        else:
            s2 = s2 + s1[i]
    return s2

def main():
    s = input('Nhập chuỗi cần mã hóa: ')
    print(f'--> Chuỗi đã mã hóa: {mahoa(s)}')
    
    
    
    
if __name__ == '__main__':
    main()