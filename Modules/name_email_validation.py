#When calling this function it asks you to enter your name and check if it's a valid or not valid email
#then it asks you to enter your email and also checks if it's a valid or not. 

def name_email_validation():
    user_name = input('please enter your name: ')    
    if user_name and not user_name.isdigit() and user_name.strip():
        print(f'Hello {user_name} you are welcome')
        email = input('your email? ')
        if '@'not in email or '.' not in email:
            print("Your email is not valid")
        elif email[0] == "@" or email[-1] == "@":
            print("your email is not valid")
        elif email.index('@') >= email.index('.'):
            print("Not a valid Email")
        else:
            print(f"Thanks {user_name} valid email \nyour email is {email}")
            
    else:
        print("name is not valid")
    
name_email_validation()


#this function checks if the name and the email is valid to use
#it takes 2 arguments user name and user email and return if they are valid.

def validation(user_name,user_email):
    if user_name and not user_name.isdigit() and user_name.strip():
        print(f'Hello {user_name} you are welcome')
        if '@'not in user_email or '.' not in user_email:
            print("email is not valid")
        elif user_email[0] == "@" or user_email[-1] == "@":
            print("not a valid")
        elif user_email.index('@') >= user_email.index('.'):
            print("email Not valid")
        else:
            print(f"valid email \nHello {user_name} your email is {user_email}")
    else:
        print("name is not valid")

validation('Yousif','Yousef@sabal.net')


