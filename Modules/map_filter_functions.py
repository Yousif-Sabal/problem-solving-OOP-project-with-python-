#this module contains two main built in functions filter and map
# filter will filter the emails inserted and return only the valid ones
# we will use map function in the process to return the domains 

def validemail(email):
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

emails = ['yousef@yahoo.com','mohamed@google.com','yaser@co.dev','maha@asu.net','ahmed@','ahmed.set','nader.co'  ]

validemails=list(filter(validemail,emails))
# print(validemails)

domains = map(lambda x: x.split('@')[1],validemails)
# print(list(domains))
