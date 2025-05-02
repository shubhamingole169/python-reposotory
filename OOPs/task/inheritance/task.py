


class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def describe(self):
        print(f"this is vehicle {self.make} its model is {self.model} and year is {self.year}")


class Car(Vehicle):
    def __init__(self, make, model, year):
        super.__init__(make,model,year)
        
    def describe(self):
        print(f"this is car {self.make} its model is {self.model} and year is {self.year}")

class Motorcycle(Vehicle):
    def __init__(self, make, model, year):
        super.__init__(make, model, year)

    def describe(self):
        print(f"this is Motorcycle {self.make} its model is {self.model} and year is {self.year}")