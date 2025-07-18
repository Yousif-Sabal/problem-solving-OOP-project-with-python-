class Car:
    def __init__(self,name,fuelRate,velocity):
        self.name = name
        self.fuelRate = fuelRate
        self.velocity = velocity
    @property
    def fuel_Rate(self):
        if self.fuelRate >= 100:
            self.fuelRate = 100
        elif self.fuelRate <= 0:
            self.fuelRate = 0
        else:
            pass
    @property
    def Velocity(self):
        if self.velocity >= 200:
            self.velocity = 200
        else:
            pass
            
        
   
    def run(self,velocity,distance):
        self.velocity = velocity
        self.distance = distance
        self.fuelRate -= 0.1*distance
        
        
    def stop(self):
        self.velocity= 0 
        if self.run().distance == 0:
            print('You arrived the destination')
        else:
            print(f"The remain distance is {self.distance} km")
    
    
        
        

