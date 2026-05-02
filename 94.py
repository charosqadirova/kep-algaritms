n = input()
sum = 0
s = 1
for raqam in range(100, 1000):
    sum += int(raqam)
    s *= int(raqam)
    if s != 0 and sum / s == 0:
        print(raqam)