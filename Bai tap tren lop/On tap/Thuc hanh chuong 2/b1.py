import math    # import thu vien math

i = 1000            # bat dau tu 1000 va ket thuc tai 9000
count = 0           # tao bien dem = 0
while i <= 9999:
    j = str(i)                      # ep kieu i thanh string
    k = int(j[0]) * int (j[3])      # tich cua chu so dau va chu so cuoi
    sqrt_k = int(math.sqrt(k))      # can bac hai cua tich
    if (sqrt_k * sqrt_k == k):      # so sanh dieu kien
        print(i)
        count += 1
    i += 1 
print(f'COUNT = {count}')           # in so luong ra man hinh