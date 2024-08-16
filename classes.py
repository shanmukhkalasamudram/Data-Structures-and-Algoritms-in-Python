
#Class is a blueprint
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary  # Private attribute

    def get_salary(self):
        return self.__salary

    def set_salary(self, amount):
        if amount > 0:
            self.__salary = amount
        else:
            print("Invalid salary!")

# Creating an object (instance) of the Car class
emp = Employee("Alice", 50000)
print(emp.get_salary())  # Output: 50000
emp.set_salary(60000)   #Encapsulation
print(emp.get_salary())  # Output: 60000 

#Encapsulation is the concept of bundling the data (attributes) and methods that operate on the data into a single unit or class.

