import math

def cp(n):
    m = int(math.sqrt(n))
    if m * m == n:
        return True
    return False

i = 0; count = 0

while i <= 10000:
    if cp(i) == True:
        print(i)
        if i <= 1000:
            count += 1
    i += 1

print(f'Co {count} scp nho hon 1000')
    
