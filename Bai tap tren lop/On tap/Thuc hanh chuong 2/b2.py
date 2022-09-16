# Lập trình nhập vào một số nguyên dương N (N < 2 tỉ).
# Hãy tìm tất cả các số nguyên dương M <= N thoả mãn hiệu của chữ số lớn nhất và nhỏ nhất của M bằng 2.

while True:
    n = int(input('Enter n: '))
    if (0 <= n < 2000000000):
        break


i = 1
while i <= n:
    j = str(i)
    max_j = int(max(j))
    min_j = int(min(j))
    if max_j - min_j == 2:
        print(i)
    i += 1

