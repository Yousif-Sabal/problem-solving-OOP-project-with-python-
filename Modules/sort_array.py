#this function takes any number of elements from the user and then display the array output and sort them in ascending and descending order 

def sort_array(*arguments):
    arguments=list(arguments)
    print(f"Original List = {arguments} \nAscending List = {sorted(arguments)} \nDecending List = {sorted(arguments,reverse = True)}")
     
sort_array(15,2,53,20,14,52,65,18)
    