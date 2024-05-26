# 22. Python program to calculate the sum of all the even numbers within the given range.

Number = int(input("enter the number"))
sum = 0
for i in range(0,Number+1,2):
    sum += i
print(f'sum of odd numbers till {Number} is {sum}')