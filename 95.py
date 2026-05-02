# 1-usul
n = int(input())
s = 0
for son in range(n):
   a = int(input())
   if a % 2 == 1:
      s += a
print(s)

# 2-usul
n = int(input())
s, i = 0, 0
while i < n:
   a = int(input())
   if a % 2 == 1:
      s += a
   i += 1
print(s)