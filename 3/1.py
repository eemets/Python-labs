#3.18
from random import random
tmp = 0
n = int(input("Enter n\t"))
for m in range(100, 999):
    s = str(m)
    a = int(s[0])
    b = int(s[1])
    c = int(s[2])
    sum = (a + b + c)
    if sum>=n:
        tmp+=1
print(tmp)