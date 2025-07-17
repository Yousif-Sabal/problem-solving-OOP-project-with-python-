#this module consists from two parts. first one is the function that checks if the email is valid or not
# the second part is a for loop to give the user five tries to enter his email correctly.

x = input("Email: ")

def validemail(email):
 try:
    if '@' in email and '.' in email:
        username, domain = email.split('@')
        if username and domain:
            x,y=domain.split('.')
            if x and y:
                return True
            else :
                return False
        else : 
            return False
    else :
        return False   
 except:
     return False 



for i in range(5):
    if validemail(x):
        print("Right,valid email")
        break
    else:
        x=input("Wrong! try Email again: ")
else:
    raise False
        