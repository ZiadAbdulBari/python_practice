# PROBLEM-1
class Car:
    def __init__(self):
        self.brand="Toyota"
        self.model="X-Corola"
        self.year="2016"
    def display_info(self):
        print(f"{self.brand}\n{self.model}\n{self.year}")

car = Car()
car.display_info()

# PROBLEM-2
"""
Create three classes Animal, Mammal, and Dog where Animal has a method eat(), Mammal inherits from Animal and has a method walk(), and Dog inherits from Mammal and has a method bark(). Create an object of Dog and demonstrate all three methods. Also, create a class Calculator with an add() method that can take either two or three parameters, and then create a subclass AdvancedCalculator that overrides the add() method to add any number of parameters using variable-length arguments. Demonstrate both functionalities.
"""
class Animal:
    def eat(self):
        print("This is animal class")
class Mammal(Animal):
    def walk(self):
        print("This is mamal class")
class Dog(Mammal):
    def bark(self):
        print("This is dog class")
class Calculator:
    def add(self,first_number,second_number,third_number=0):
        print(first_number+second_number+third_number)
        pass
class AdvancedCalculator(Calculator):
    def add(self,*args):
        result = 0
        for i in args:
            result+=i
        print(result)
dog = Dog()
dog.eat()
dog.walk()
dog.bark()
calculator = Calculator()
calculator.add(2,3)
advance=AdvancedCalculator()
advance.add(10,20,30,40)

"""
Create a class BankAccount with a private attribute balance and provide methods deposit() and withdraw() to modify the balance safely so that the balance cannot be accessed directly. Then create two subclasses SavingsAccount and CurrentAccount, each having a method account_type() that prints its respective account type. Demonstrate polymorphism by calling account_type() from different account objects.
"""