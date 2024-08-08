username = "Adamya"
# password = "123"
user_approval = "Shirish"

ui_username = input("Enter your username: ")
# ui_password = input("Enter your password: ")

if(ui_username == username):
    print("User Exists")
elif(ui_username == user_approval):
    print("User Under approval")
else: 
    print("User Not Authorised")