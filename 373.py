# 1- usul
n = int(input())
sonlar = list(map(int, input().split()))
max_value = sonlar
for son in sonlar:
   if son < max_value:
    max_value=son

max_value
# 2 - usul
n = int(input())
sonlar = list(map(int, input().split()))

print(max(sonlar))