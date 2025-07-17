# this function generate a multiplication table from 1 to the number passed.
def multi_table(num):
    for i in range(num+1):
        for j in range(1,i+1):
            print(f"multiplication of {i} and {j} = {i*j}")
            
multi_table(10)