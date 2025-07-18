class Person:
    def __init__(self,name,money,mood,healthRate):
        self.name = name
        self.money = money
        self.mood = mood
        self.healthRate = healthRate
    def sleep(self,hours):
        if hours == 7:
            self.mood ="Happy"
        elif hours < 7:
            self.mood = "Tired"
        elif hours > 7 :
            self.mood = "Lazy"
        else:
            raise ValueError
        
            
    def eat(self,Meals):
        if Meals == 3:
            return('health = 100%')
        elif Meals == 2:
            return('health = 75%')
        elif Meals == 1:
            return('health = 50%')
        else:
            raise ValueError

            
        
    def buy(self,items):
        self.items = items
        for i in range(items):
            self.money -=10
    
    


person1 = Person("ahmed", 2500,"Happy",20)
person2 = Person("Yousif",5000,"Tired",70)

# print (person1.money)

# print(person1.buy(5))

# print (person1.money)
# person1.sleep(3)
# print(person1.mood)

