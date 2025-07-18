from person_class import Person

class Employee(Person):
    def __init__(self, name, money, mood, healthrate,id,car,email,salary,distanceToWork):
        super(Employee,self).__init__(name,money,mood,healthrate)
        self.id = id
        self.car = car
        self.email = email
        self.salary = salary
        self.distanceToWork = distanceToWork
    
    def work(self,hours):
        if hours == 8:
            self.mood = "Happy"
        elif hours > 8:
            self.mood = "Tired"
        elif hours < 8 :
            self.mood = "Lazy"
        else:
            raise ValueError
    def drive(self,distance):
        self.distance = distance
    def refuel(self):
        self.gasAmount = 100
    def send_mail(self):
        pass

# person1 = Employee("Yousif",5000,"Tired",70,123,'fiat28','sameh.com',5600,20)
# print(person1.car)