# 15. Python program that accepts a string and calculate the number of digits and letters and space

a = "rahul7777777"
digit = 0
letters = 0
space = 0

for i in a:
    if i.isalpha():
        letters += 1
    elif i.isdigit():
        digit += 1
    else:
        space += 1
        
print(f"the total letters is:",letters)
print(f"the total  digit is:", digit)
print(f"the total space is:",space)