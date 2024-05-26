# 30  Write a for loop which appends the square of each number to the new list.
n = int(input("Enter a range? "))
newlst = []

for i in range(1,n+1):
    newlst.append(i ** 2)

print(f"the every possible square number in the given list {n} is:- {newlst}")