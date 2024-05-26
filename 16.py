# 16.  Python program to check the validity of username and password input by users

for i in range(5):
    name = input("Enter name? ")
    password = input("Enter password? ") 

    if len(name) >= 10 and len(password) >= 10 and  "*" in password:
        print(f"Your name {name}")
        print(f"Your password {password}")
        break    
    else:
         print("Your name must be at least 10 characters.")
         print("Your password must contain '*' and must be a minimum length 10 ")

    if i == 3:
        print("This is final attempt to enter correct details or your you will be blocked")
