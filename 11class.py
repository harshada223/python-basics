class Employee:
    name="John"
    age=26
emp=Employee()
type(emp)
print(emp.name)
print(emp.age)
print("________________________________________")

class Employee:
    name="sana"
    age=26
    def hello(self):
        print("Hello")
emp=Employee()
emp.hello()
print("________________________________________")

class Employee:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def details(self):
        print("Employee Name: ", self.name)
        print("Employee Age:", self.age)
emp1=Employee("John", 26)
emp2=Employee("Jane",24)
emp1.details()
emp2.details()
print("________________________________________")

class Student:
    def __init__(self , name):
        self.name=name
    def intro(self):
        print('Hi I am', self.name)
    def change_name(self, name):
        self.name=name
john=Student('john')
john.intro()
print(john.name)
john.change_name('JJOOHHNN')
john.intro()
print("________________________________________")

class Rectangle:
    def __init__(self, length, width):
        self.length=length
        self.width=width
    def area(self):
        print(f"Length - {self.length}, Width-{self.width}")
        return self.length * self.width
first=Rectangle(5,2)
print(first.area())
print("________________________________________")

class Dog:
    def __init__(self, breed, age, color):
        self.breed=breed
        self.age=age
        self.color=color
    def details(self):
        print(f"Breed - {self.breed}, Age - {self.age}, Color - {self.age}")
dog1=Dog('Husky',5,'Blank')
dog1.details()