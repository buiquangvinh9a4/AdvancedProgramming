
# i = 10000
# count = 0

# while i <= 99999:
#     p = i
#     sum = 0
#     while p > 0:
#         tmp = p % 10
#         sum += tmp
#         p //= 10
#     if sum == 25:
#         count += 1
#         print(i)
#     i += 1
# print(count)



p = int(input('Nhập p: '))
sum = 0
while p > 0:
    tmp = p % 10
    sum += tmp
    p //= 10
print(f'Tổng các chữ số của p = {sum}')
