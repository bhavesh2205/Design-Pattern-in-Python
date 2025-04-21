## object oriented programming

from datetime import datetime

class Car:
    def __init__(self, make, model, year, price):
        self.make = make
        self.model = model
        self.year = year
        self.price = price

    def get_description(self):
        return f"{self.year} {self.make} {self.model} {self.price}"
    
# car1 = Car("Toyota", "Corolla", 2020)
# car2 = Car("Ford", "Mustang", 2021)

# print(car1.get_description())
# print(car2.get_description())
    
class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size, price):
        super().__init__(make, model, year, price)
        self.battery_size = battery_size

    def __str__(self):
        return f"{self.year} {self.make} {self.model} with a {self.battery_size} kWh battery {self.price}"
    
    def car_perchase_year(self):
        return self.year

    def current_year(self):
        return datetime.now().year

    def car_lifespan(self):
        car_age = self.current_year() - self.car_perchase_year()
        return car_age
    
    def inflation(self):
        inflation_rate = 0.05
        current_price = self.price * inflation_rate
        return current_price

car1 = ElectricCar("Toyota", "Corolla",2010, 100, 10000)

print(car1.__str__())
print(car1.car_lifespan())
print(car1.inflation())


#class that will calculate avg of number given list as input.

class AvgCalculator:
    def __init__(self, numbers: tuple):
        self.numbers = numbers
        
    def total(self):
        total = 0
        for number in self.numbers:
            total += number
        return total
    
    def length(self):
        length = 0
        for number in self.numbers:
            length += 1
        return length
    
    def avg(self):
        avg = self.total() / self.length()
        return avg
    
avg_calculator = AvgCalculator([1, 2, 3, 4, 5])
print(avg_calculator.avg())


#class for calculating age of the person

class AgeCalculator:
    def __init__(self, birth_year: int):
        self.birth_year = birth_year
        
    def age(self):
        age = datetime.now().year - self.birth_year
        return age
    
age_calculator = AgeCalculator(2000)
print(age_calculator.age())
        
        
#polymorphism
'''
polimorphism is a concept that allows objects to take on multiple forms.
'''
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        
    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}"
    
class Employee(Person):
    def __init__(self, name: str, age: int, salary: int):
        super().__init__(name, age)
        self.salary = salary
        
    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"
    
class Customer(Person):
    def __init__(self, name: str, age: int, balance: int):
        super().__init__(name, age)
        self.balance = balance
        
    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}, Balance: {self.balance}"
    
person1 = Person("John", 20)
employee1 = Employee("Jane", 30, 50000)
customer1 = Customer("Jim", 40, 1000)

print(person1.get_info())
print(employee1.get_info())
print(customer1.get_info())


##class for calculating interest of the bank account

class BankAccount:
    def __init__(self, balance: int):
        self.balance = balance
        
    def get_balance(self):
        return self.balance
    
class SavingsAccount(BankAccount):
    def __init__(self, balance: int, interest_rate: float = 0.05):
        super().__init__(balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest =  self.balance * self.interest_rate
        return interest
    
savings_account = SavingsAccount(100000)
print(savings_account.calculate_interest())

##class for calculating area of the circle

class Circle:
    def __init__(self, radius: int, pi: float = 3.14):
        self.radius = radius
        self.pi = pi
        
    def area(self):
        area = self.pi * self.radius ** 2
        return area 
    
    def circumference(self):
        circumference = round(2 * self.pi * self.radius, 2)
        return circumference
    
circle = Circle(5)
print(circle.area())
print(circle.circumference())



# incapsulation -
'''
incapsulation is a concept that restricts access to certain parts of an object.
'''

class BankAccount:
    def __init__(self, balance: int):
        self.__balance = balance
        
    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount: int):
        self.__balance += amount
        return self.__balance
    
    def withdraw(self, amount: int):
        self.__balance -= amount
        return self.__balance
    
    def transfer(self, amount: int, to_account: 'BankAccount'):
        self.withdraw(amount)
        to_account.deposit(amount)
        return self.__balance, to_account.__balance
    
    def __str__(self):
        return f"Balance: {self.__balance}"   
    
account1 = BankAccount(1000)
account2 = BankAccount(2000)

print(account1.transfer(500, account2))
print(account1)
print(account2)

print(account1.get_balance())
    
    
# example of abstraction
'''
abstraction is a concept that hides the implementation details of an object and exposes only the necessary parts of the object.

'''
class Animal:
    def __init__(self, name: str):
        self.name = name
        
    def make_sound(self):
        pass
    
class Dog(Animal):
    def make_sound(self):
        return "Woof"
    
class Cat(Animal):
    def make_sound(self):
        return "Meow"
    
dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.make_sound())
print(cat.make_sound())


# inheritance
'''
inheritance is a concept that allows a class to inherit the properties and methods of another class.

'''
import pandas as pd

class Insurance:
    def __init__(self, policy_number: str, policy_holder: str, policy_type: str, policy_start_date: str, policy_end_date: str):
        self.policy_number = policy_number
        self.policy_holder = policy_holder
        self.policy_type = policy_type
        self.policy_start_date = policy_start_date
        self.policy_end_date = policy_end_date

class AutoInsurance(Insurance):
    def __init__(self, policy_number: str, policy_holder: str, policy_type: str, policy_start_date: str, policy_end_date: str, car_make: str, car_model: str, car_year: int):
        super().__init__(policy_number, policy_holder, policy_type, policy_start_date, policy_end_date)
        self.car_make = car_make
        self.car_model = car_model
        self.car_year = car_year
        
    def get_info(self):
        data=pd.DataFrame({"Policy Number": [self.policy_number],
                           "Policy Holder": [self.policy_holder], 
                           "Policy Type": [self.policy_type], 
                           "Policy Start Date": [self.policy_start_date], 
                           "Policy End Date": [self.policy_end_date], 
                           "Car Make": [self.car_make], 
                           "Car Model": [self.car_model], 
                           "Car Year": [self.car_year]})
        return data
    
class HomeInsurance(Insurance):
    def __init__(self, policy_number: str, policy_holder: str, policy_type: str, policy_start_date: str, policy_end_date: str, home_address: str, home_value: int):
        super().__init__(policy_number, policy_holder, policy_type, policy_start_date, policy_end_date)
        self.home_address = home_address
        self.home_value = home_value
        
    def get_info(self):
        data=pd.DataFrame({"Policy Number": [self.policy_number],
                           "Policy Holder": [self.policy_holder], 
                           "Policy Type": [self.policy_type], 
                           "Policy Start Date": [self.policy_start_date], 
                           "Policy End Date": [self.policy_end_date], 
                           "Home Address": [self.home_address], 
                           "Home Value": [self.home_value]})
        return data

auto_insurance = AutoInsurance("1234567890", "John Doe", "Auto", "2024-01-01", "2024-12-31", "Toyota", "Corolla", 2020)
home_insurance = HomeInsurance("1234567890", "John Doe", "Home", "2024-01-01", "2024-12-31", "123 Main St", 100000)

print(auto_insurance.get_info())
print(home_insurance.get_info())


## class method and static method
'''
class method is a method that is bound to the class and not the instance of the class.
static method is a method that is not bound to the class or instance of the class.
'''

class MathOperations:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b
        
    def add(self):
        return self.a + self.b
    
    @classmethod
    def multiply(cls, a: int, b: int):
        return a * b
    
    @staticmethod
    def divide(a: int, b: int):
        return a / b
    
    def subtract(self):
        return self.a - self.b

math_operations = MathOperations(10, 5)

print(math_operations.add())
print(MathOperations.multiply(10, 5))
print(math_operations.divide(10, 5))
print(math_operations.subtract())


## property decorator
'''
property decorator is a decorator that is used to define a property of a class.
it is a way to hide the implementation details of an object and expose only the necessary parts of the object.
'''

class House:
    def __init__(self, price: int):
        self.__price = price
        
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value: int):
        self.__price = value
        
    @price.deleter
    def price(self):
        del self.__price
        
house = House(1000000)

print(house.price)
house.price = 200000
print(house.price)
del house.price


# magic methods
'''
magic methods are methods that are used to define the behavior of an object.
'''

class Vector:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y  
        
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __mul__(self, other):
        return Vector(self.x * other.x, self.y * other.y)
    
    def __len__(self):
        return self.x + self.y  
    
vector1 = Vector(1, 2)
vector2 = Vector(3, 4)

print(vector1 + vector2)
print(vector1 * vector2)
print(vector1.__str__())
print(vector2.__str__())
print(vector1.__add__(vector2))
print(vector1.__mul__(vector2))
print(vector1.__len__())


    
#class for tokenization if we pass string it will return list of tokens

class Tokenizer:
    def __init__(self, string: str):
        self.string = string    
        
    def tokenize(self):
        return self.string.split()
    
tokenizer = Tokenizer("Hi my name is bhavesh and i am a Data Scientist")
print(tokenizer.tokenize())

## class to convert temperature from celsius to fahrenheit

class TemperatureConverter:
    def __init__(self, celsius: float):
        self.celsius = celsius

    def convert_to_fahrenheit(self):
            return (self.celsius * 9/5) + 32
    
    def __str__(self):
        return f"Temperature in Celsius: {self.celsius}"
    
temperature_converter = TemperatureConverter(20.20)
print(temperature_converter.convert_to_fahrenheit())
      
        
        
        



        
        
