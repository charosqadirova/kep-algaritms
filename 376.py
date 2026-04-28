n = int(input())
sonlar = list(map(int, input().split()))
sonlar.sort()  # o‘sish tartibida saralaydi
print(*sonlar)