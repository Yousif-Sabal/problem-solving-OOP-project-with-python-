#this function returns the number of vowels in the sentence you entered
def Count_vowels(user_name):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    count=0
    for i in user_name:
        if i in vowels:
         count +=1
    print(count)

Count_vowels('my name is yousef Sabal')