# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

#See PyCharm help at https://www.jetbrains.com/help/pycharm/


# def multiply(a, b):
#     result = a * b
#     print(f"The result is {result}")  # Display the result
#     return result  # Send back for further use
#
# x = multiply(3, 4)  # Prints: The result is 12
# # print(x)  # Output: 12

class Car: # Created Car Class

    segment = "Sedan"
    car_amount = 2000

    def __init__(self, company, model, category): # Created __init__ Method & given instance variables
        self.company = company
        self.model = model
        self.category = category

    # def Full_Details(self):
    #     return f" my car company is {self.company} & model is {self.model} with {self.category}"

    def Full_Details(self):
        print (f" my car company is {self.company} & model is {self.model} with {self.category} {Car.segment}")

    @classmethod
    def amount_raise(cls, amtt):
        cls.car_amount = amtt


car1 = Car("Benz", "AMG", "Top_End") # instance of Class
car2 = Car("BMW", "M4", "Mid_End") # instance of Class
car3 = Car("Audi", "R7", "Top_End") # instance of Class

Car.amount_raise(10000)

# car1.Full_Details()
# car2.Full_Details()
# car3.Full_Details()

print(car1.car_amount)
print(car2.car_amount)
print(car3.car_amount)

# print(car1.Full_Details())

# print(car1.amount_raise(5000))

from abc import ABC, abstractmethod

class Fourwheelers(ABC): #Creating new_payment system for credit card, UPI paypal

    @abstractmethod
    def engine_capacity(self,capacity,model):
        pass

class Benz_Fourwheeler(Fourwheelers):
    def engine_capacity(self,capacity,model):
        return f" my engine capacity is {capacity} & model is {model}"

class audi_Fourwheeler(Fourwheelers):
    def engine_capacity(self,capacity,model):
        return f" my engine capacity is {capacity} & model is {model}"



benz = Benz_Fourwheeler()
audi = audi_Fourwheeler()


print(benz.engine_capacity('9.8 lit heavy engine','Benz-AMG'))
print(audi.engine_capacity("10.8engine","Audi R-7"))
print(audi_Fourwheeler().engine_capacity("10.8engine","Audi R-7"))

class Employee:
    company = "Tesla"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def change_company(cls, new_name):
        cls.company = new_name

    @staticmethod
    def info():
        return "This is the Employee class"

emp = Employee("John", 5000)
print(Employee.info())  # Static method
Employee.change_company("Google")
print(emp.company)  # Google


class MyTestClassCheck(ABC):
    first_name: str
    last_name: str
    rid: str

    def __init__(self, first_name, last_name, rid, **kwargs):
        self.first_name = first_name
        self.last_name = last_name
        self.rid = rid

class AgainCheck(MyTestClassCheck):
    def __init__(self):

        super().__init__("vk","k","1")


   ''

    def show_info(self):
        return f" my {self.first_name} {self.last_name} {self.rid}"

myinfo = AgainCheck()

print(myinfo.show_info())