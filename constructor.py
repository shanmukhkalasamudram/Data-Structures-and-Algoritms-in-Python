#The primary purpose of a constructor is to set up the initial state of the object, 
#ensuring that it is ready for use immediately after creation.

class Car:
    def __init__(self, make, model, year):
        self.make = make  # Attribute 'make' is initialized with the value of the parameter 'make'
        self.model = model  # Attribute 'model' is initialized with the value of the parameter 'model'
        self.year = year  # Attribute 'year' is initialized with the value of the parameter 'year'

# Self refers to an instance
