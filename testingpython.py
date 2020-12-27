_username = input("Hi there!\nPlease tell us your name: ")
print("Hi "+_username)  
_password = input("Please create a password: ")

if _password.count<8:
    print("Please Enter a Password with more than 8 characters.")
else:
    print("Account created successfully")