class Vehicle:
    def __init__(self, wheels, color, accomodation):
        self.wheels = wheels
        self.color = color
        self.accomodation = accomodation

    def display_info(self):
        print("Wheels: ", self.wheels)
        print("Colour: ", self.color)
        print("Accomodation: ", self.accomodation)
    
vehicle1 = Vehicle(4, "red", 5)
vehicle1.display_info()

class Car(Vehicle):
    def __init__(self, wheels = 0, color = " ", accomodation = 0, model = " ", brand = " "):
        super().__init__(wheels, color, accomodation)
        self.model = model
        self.brand = brand

    def display_info(self):
        super().display_info()
        print("Model: ", self.model)
        print("Brand: ", self.brand)

car1 = Car(4, "red", 5, "sedan", "Toyota")
car1.display_info()

car2 = Car()
car2.display_info()
