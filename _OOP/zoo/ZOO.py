from Animal import Animal,Lion,Monkey,Bear
class Zoo:
    def __init__(self,zoo_name):
        self.zoo_name=zoo_name
        self.animals=[]
    
    def add_animal(self,obj_ins):
        self.animals.append(obj_ins)
        return self
    
    def printAllInfo(self):
        print("-"*30,f"{self.zoo_name}","-"*30)
        for animal in self.animals:
            animal.display_info()
        
        return self    
        
    
    
zoo1=Zoo("Moayad zoo")
lion1=Lion(name="Nala", age=5, health_level=80, Happiness_level=70,sound="Roar")
lion2=Lion(name="Simba", age=7, health_level=90, Happiness_level=65,sound="Grrr")
Monkey1=Monkey(name="George", age=3, health_level=60, Happiness_level=85,sound="Ooh ooh aah aah")
Monkey2=Monkey(name="Abu", age=4, health_level=55, Happiness_level=90,sound="Eee eee")
Bear1=Bear(name="Baloo", age=10, health_level=95, Happiness_level=50,sound="Growl")
Bear2=Bear(name="Paddington", age=6, health_level=75, Happiness_level=80,sound="Huff")
lion1.feed()
lion2.feed()
Monkey1.feed()
Monkey2.feed()
Bear1.feed()
Bear2.feed()
zoo1.add_animal(lion1).add_animal(lion2).add_animal(Monkey1).add_animal(Monkey2).add_animal(Bear1).add_animal(Bear2).printAllInfo()

    
        
            