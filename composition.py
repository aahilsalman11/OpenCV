class Car:
    def __init__(self, color, model, brand, design):
        self.color = color
        self.model = model
        self.brand = brand
        self.design = design

    def display_info(self):
        print("Colour: ", self.color)
        print("Model: ", self.model)
        print("Brand: ", self.brand)
        print("Design: ", self.design)
    
    def change_colour(self):
        new_colour = input("Enter new colour: ")
        self.color = new_colour
        print("Colour changed to: ", self.color)

car1 = Car("red", "sedan", "Toyota", "sleek")
print(car1.color)
print(car1.model)
car1.display_info()
car1.change_colour()

car2 = Car("blue", "SUV", "Honda", "rugged")
print(car2.color)
print(car2.model)
car2.display_info()
car2.change_colour()


