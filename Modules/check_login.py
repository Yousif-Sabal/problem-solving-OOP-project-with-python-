#this function checks for the name and the password to login
users = [{"name":"Ahmed","password":"123"},{"name":"Yousif","password":"awd"},{"name":"Mohamed","password":"mohamed123"}]
def check_login():
    user_name = input("Please enter your name: ")
    for user in users:
        if user_name == user["name"]:
            password = input("Please enter your password: ")
            if password == user["password"]:
                print(f"Welcome {user_name} you are in.")
                break
            else:
                print("Password is incorect")
    else:
        print("Not found")
        
check_login()
        






