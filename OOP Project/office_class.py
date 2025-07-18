from employee_class import Employee
class Office:
    Num_of_emp = 0
    def __init__(self,name,employees):
        self.name = name
        self.employees = employees
    def get_all_employees (self):
        return(self.employees)
    @property    
    def get_employee(self,empid):
        for employee in self.employees:
            if employee.id == empid:
                return employee
        
    def hire(self, employee):
        self.employees.append(employee)
        Office.Num_of_emp += 1
        
    def fire(self, emp_id):
        new_employees = []
        for employee in self.employees:
            if employee.id != emp_id:
                new_employees.append(employee)
                Office.Num_of_emp -= 1   
            
        
    @staticmethod
    def calculate_lateness(self,targetHour,moveHour,distance,velocity):
        Road_time = distance / velocity  
        arrival_time = moveHour + Road_time
        if arrival_time <= targetHour:
            return 'Welcome,In time'
        else:
            return 'You are late'
    
    def deduct(self,empid,deduct):
        for emp in self.employees:
                if emp.id == empid:
                    emp.salary -= deduct
    def reward(self,empid,reward):
        for emp in self.employees:
                if emp.id == empid:
                    emp.salary -= reward
    
    @classmethod
    def change_emps_num(cls,num):
        pass
        