import math
x = 10**6
def divsum(n):
    sum = 1
    if(n == 1):
        return sum
    i = 2
    m = int(math.sqrt(n))
    for i in range (2,m+1):
    	if (n%i==0):
            if(i==n/i):
                sum += i
            else:
                sum += (i+n/i)
    return int(sum)
def abundant(n):
    return divsum(n)>n
def check(m,n):
	return divsum(m)==n and divsum(n)==m
count = 0
for i in range (1,x):
    if(abundant(i)):
        if(check(i,divsum(i)) and (divsum(i)<x)):
            print(i," - ",divsum(i))
            count += 1
print(count)
