class Grandparent:
    def __init__(self,house):
        self.house = house
    
    def display(self):
        print("House: ",self.house)

house1 = Grandparent("Mansion")#
house1.display()

class Parent(Grandparent):
    def __init__(self, house, car):
        super().__init__(house)
        self.car = car
    
    def display(self):
        super().display()
        print("Car: ",self.car)

parent1 = Parent("Mansion", "Lamborghini")
parent1.display()

class Child(Parent):
    def __init__(self, house, car, toy):
        super().__init__(house, car)
        self.toy = toy
    
    def display(self):
        super().display()
        print("Toy: ",self.toy)

child1 = Child("Mansion", "Lamborghini", "Lego Set")
child1.display()

print("I am a child and I have a ", child1.house, ", a ", child1.car, " and a ", child1.toy)

