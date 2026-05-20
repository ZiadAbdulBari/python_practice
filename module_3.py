class Car:
    def __init__(self):
        self.brand="Toyota"
        self.model="X-Corola"
        self.year="2016"
    def display_info(self):
        print(f"{self.brand}\n{self.model}\n{self.year}")

car = Car()
car.display_info()
"""
Question 2: Create three classes Animal, Mammal, and Dog where Animal has a method eat(), Mammal inherits from Animal and has a method walk(), and Dog inherits from Mammal and has a method bark(). Create an object of Dog and demonstrate all three methods. Also, create a class Calculator with an add() method that can take either two or three parameters, and then create a subclass AdvancedCalculator that overrides the add() method to add any number of parameters using variable-length arguments. Demonstrate both functionalities.

Question 3: Create a class BankAccount with a private attribute balance and provide methods deposit() and withdraw() to modify the balance safely so that the balance cannot be accessed directly. Then create two subclasses SavingsAccount and CurrentAccount, each having a method account_type() that prints its respective account type. Demonstrate polymorphism by calling account_type() from different account objects.
"""