username = input("Enter your username")
password = input("Enter your password")

if (username == "Adamya" and password == "admin"): 
    print("Welcome Admin")
elif (username == "Bipin" and password == "user"):
    print("Welcome User")
else: 
    print("Not authorized")