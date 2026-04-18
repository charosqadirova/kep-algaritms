n = input()
if int(n[0]) + int(n[1]) + int(n[2]) == int(n[3]) + int(n[4]) + int(n[5]):
    print(True)
else:
     print(False)

#  2 - usul
def sum_digits(number):
  s = 0
  for digit in str(number):
    raqam = int(digit)
    s += raqam

  return s

n = input()
n1 =sum_digits(n[:3])
n2 = sum_digits(n[3:6])
if n1 == n2:
    print(True)
else:    
    print(False)
