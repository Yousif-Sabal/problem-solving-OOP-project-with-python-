# the function here extracts a mario pyramid in five lines put in list shaped.
def mario_pyramid():
    list =[' ',' ',' ',' ',' ']
    for i in range(5):    
        list.append('*')
        list.remove(' ')
        print(list)

mario_pyramid()
