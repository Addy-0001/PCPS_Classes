db_username = "adamya"
db_password = 12345
is_admin = False

username = input("Enter Username: ")
password = int(input("Enter Password: "))

if((username == db_username) and (password == db_password)):
    if(is_admin):
        print("Welcome to the app, admin.")
    else: 
        print("Welcome to the app, user.")
else: 
    print("Username or Password not found")
    
    
# #Program for looping
# for i in range(10): 
#     print(i)
    
list1 = [1, 2, 3, 4, 5]

# for data in list1: 
#     print(data)
    
data = 0
    
# while data in range(10):
#     print(data)
#     data += 1
    

while data in list1:
    print(data)