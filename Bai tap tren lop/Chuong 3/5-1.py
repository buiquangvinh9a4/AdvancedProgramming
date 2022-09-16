# def line(n):
#     for i in range(n):
#         print(end='-')
#     print()
        
# def multi(n):
#     print(n, end='|\t')
#     for i in range(1, 11):
#         print(n * i, end='\t')
#     print()

# multi(1); line(85)
# for i in range(1, 11):
#     multi(i)

print('x', end = '|\t')     # in ra chữ x
for i in range(1, 11):      # lệnh lặp in ra dãy số từ 1 -> 10 ở dòng đầu
    print(i, end = '\t')
print()                     # xuống dòng 

for i in range(85):         # lệnh lặp in ra 85 kí tự '-'
    print(end = '-')
print()                     # xuống dòng 

for i in range(1, 11):             # vòng lặp đầu in theo dòng
    print(i, end = ' |\t')         # in số nhân và dấu '|' + tab
    for j in range(1, 11):         # vòng lặp thứ hai in theo cột     
        print(i * j, end = '\t')   # in kết quả của i * j
    print()                        # xuống dòng 
        
        
        
