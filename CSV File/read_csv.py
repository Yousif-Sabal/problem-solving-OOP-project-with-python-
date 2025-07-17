#in this module we will use import function to import csv and then we will read a csv file and manipulate the data in it.
import csv
file = open(r"D:\ITI\python course\emails.csv",'r',newline="")
read =csv.reader(file)
Data = list(read)
emails = []
for i in range(1,len(Data)):
    emails.append(Data[i][3])
#in this part we will import validmail function from a module we created before to simplify the code     
#the validmail function will return only the valid mails.
from map_filter_functions import validemail
validemails=list(filter(validemail,emails))
domains = list(map(lambda x: x.split('@')[1],validemails))
unique_domains = set(domains)
print(validemails,'\n',unique_domains)
print(f'All emails are {len(emails)} and valid ones are {len(validemails)}')
print(f'Valid domains are {len(domains)} and the unique are {len(unique_domains)}')