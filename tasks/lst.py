lst = [18, 22, 5, 38, 0, 7 ]
for element in lst:
    if element < 30 and element % 3 == 0:
        print(element , end = " ")
    else:
         s += element

print(s)