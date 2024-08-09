db_username = "adamya"
db_password = 12345
is_admin = True

username = input("Enter Username: ")
password = input("Enter Password: ")

if (((username == db_username) and (password == db_password)) or is_admin):
    print("Welcome to the app, admin.")
else: 
    print("Username or Password not found")