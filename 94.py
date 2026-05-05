def raqamlar_yigindisi(son):
    s, p = 1, 0
    for n in str(son):
        s += int(n)
        p *= int(n)
    return s,p
for i in range(100, 1000):
   s,p = raqamlar_yigindisi_kopaytmasi(son)
   if p % s == 0: 
        print(son)