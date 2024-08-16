class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start(self):
        print(f"{self.make} {self.model} is starting.")

class Car(Vehicle):  # Car inherits from Vehicle
    def __init__(self, make, model, year):
        super().__init__(make, model)
        self.year = year

    def honk(self):
        print(f"{self.make} {self.model} is honking.")

my_car = Car("Honda", "Civic", 2022)
my_car.start()  # Inherited method: Output: Honda Civic is starting.
my_car.honk()   # Output: Honda Civic is honking.
