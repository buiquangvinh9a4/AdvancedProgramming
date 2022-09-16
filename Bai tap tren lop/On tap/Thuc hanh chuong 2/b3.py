# Bài 3: Cho số nguyên N trong hệ cơ số 10, hãy chuyển N sang hệ cơ số 2, hiển thị kết qủa lên màn hình.

N = int(input('Enter N: '))
S = ''
i = N
while i > 0:
    j = i % 2
    S += str(j)
    i //= 2

p = ''
for k in range(len(S)):
    p += S[len(S) - k - 1]

print(p)

# cach 2
print(bin(N).replace("0b", ""))