#use this function to know the index or locations of the character 'i' in any string.
def locations(string):
    string = string.lower()
    list=[]
    for i in range(len(string)):
        if string[i] == 'i':
            list.append(i)
    print(list)

locations('I am yousif and I like diving')
