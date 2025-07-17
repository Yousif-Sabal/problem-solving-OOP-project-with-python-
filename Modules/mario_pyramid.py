#this function returns a mario pyramid of stars with the number you passes.
def pyramid(num):
    for i in range(num+1):
        x,y=' ','*'
        x *= num
        y *=i
        num-=1
        print(x,y)

pyramid(5)
        