import math
n = int(input())
print(math.factorial(n))

# 2 
n = int(input())
s = 1
for son in range(1, n+1):
    s *= son
print(s)