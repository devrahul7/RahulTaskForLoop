# 21. Python program to calculate the sum of all the odd numbers within the given range.

Number = int(input("enter the number"))
sum = 0
for i in range(1,Number+1,2):
    sum += i
print(f'sum of odd numbers till {Number} is {sum}')