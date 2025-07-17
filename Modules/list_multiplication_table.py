#that function generate a multiplication table from 1 to the number passed and return a nested list.
def multiblication(number_passed):
    list=[]
    for x in range(1,number_passed+1):
        list2=[]
        for y in range(1,x+1):
            list2.append(x*y)
        list.append(list2)
    print(list)
multiblication(5)