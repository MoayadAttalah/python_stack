class Animal:
    def __init__(self,name,age,health_level,Happiness_level):
        self.name=name
        self.age=age
        self.health_level=health_level
        self.Happiness_level=Happiness_level
        
    def display_info(self):
        print(f"{self.name} has health level of {self.health_level} and happiens level of {self.Happiness_level}")  
    
    def feed(self):
        self.health_level+=10
        self.Happiness_level+=10
        return self
    
class Lion(Animal):
    def __init__(self, name, age, health_level, Happiness_level,sound):
        super().__init__(name, age, health_level, Happiness_level)                      
        self.sound=sound
    
    def feed(self):
            self.health_level+=15
            self.Happiness_level+=20
            return self
                
class Monkey(Animal):
    def __init__(self, name, age, health_level, Happiness_level,sound):
            super().__init__(name, age, health_level, Happiness_level)
            self.sound=sound
    def feed(self):
            self.health_level+=5
            self.Happiness_level+=35
            return self        
class Bear(Animal):
    def __init__(self, name, age, health_level, Happiness_level,sound):
            super().__init__(name, age, health_level, Happiness_level) 
            self.sound=sound
    def feed(self):
            self.health_level+=6
            self.Happiness_level+=6
            return self
            
                    
            