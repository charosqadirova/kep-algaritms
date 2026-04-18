def sum_digits(number):
  s = 0
  for digit in str(number):
    raqam = int(digit)
    s += raqam
         
  return s
print(sum_digits(123))
  

# number = 357 => "357"
# 1. d = "3" => 3;  s = 0 + 3 = 3
# 2. d = "5" => 5;  s = 3 + 5 = 8
# 3. d = "7" => 7;  s = 8 + 7 = 15
# s = 15


