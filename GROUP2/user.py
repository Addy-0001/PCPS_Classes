my_username = "Adamya"
under_approval = "Gaurav"
ui_username = input("Enter your username: ")

if(ui_username == my_username):
    print("Welcome to the app.")
    print(my_username)
elif(ui_username == under_approval):
   print("User under approval")
   print("Thank you for the patience")
else: 
    print("User not found")