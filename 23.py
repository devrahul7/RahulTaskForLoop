# 23. Python program to count the space of a given string

rahul = 'rahul  Shah'
print(rahul.count(" "))



a = input("Enter string? ")

add = 0

for i in a:
    if i.isspace():
        add += 1

print("Number of space :{}".format(add))