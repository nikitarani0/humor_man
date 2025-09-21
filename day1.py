# Create a class Student with attributes roll_no, name, marks.
# Add methods to:
# Display student details.
# Calculate grade based on marks.
# Compare two students by marks.
# Write a class BankAccount:
# Functions: deposit(), withdraw(), display_balance().
# Prevent withdrawal if balance < withdrawal amount.
# Implement inheritance:
# Person (name, age).
# Employee(Person) (emp_id, salary).
# Add method to calculate yearly bonus (10% of salary).
# Demonstrate polymorphism with a Shape base class and Rectangle & Circle subclasses that override an area() method.

class Student:
    # roll_no = se
    # name = self.name
    def __init__(self, roll_no ,name,marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks
    def grade(self,marks):
        if self.marks > 90:
            return 'A'
        elif self.marks <=90 and self.marks > 70:
            return 'B'
        elif self.marks <=70 and self.marks > 40:
            return 'C'
        else :
            return 'Fail'  

    def display(self):
        print(f"The marks of {self.name} and {self.roll_no} is: {self.marks}.")
        print("The grade of student is: ",self.grade(self))

class BankAccount:
    def __init__(self):
        self.money = 0
    def deposit(self):
        amount = int(input("Enter the amount to deposit: "))
        self.money += self.amount

    def Withdraw(self):
        wamount = int(input("Enter the amount to withdraw: "))
        if self.money < self.wamount:
            self.money -= self.wamount
        else:
            print("Insufficient Balance.")

    def display_balance(self):
        print("Your current balance is: ",self.money)

class Person:
    def __init__(self, name ,age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, emp_id, salary):
        self.emp_id = emp_id
        self.salary = salary
    def eligibilty(self):
        if self.age > 45:
            self.salary+=1000
            return self.salary
    def yearlyBonus(self):
        yBonus = self.salary*0.1
        return yBonus
import math
class Shape:
    def __init__(self, *args):
        self.args = args

class Retangle(Shape):
    def __init__(self):
        super().__init__()
    def Area(self):
        return self.l*self.b

class Circle(Shape):
    def __init__(self):
        super().__init__()
    def Area(self):
        return math.pi*self.rad*self.rad


        
        
if __name__ == '__main__':
    Student1 = Student(1,'Nikita', 66)
    Student1.display()
    b1 = BankAccount()
    b1.Withdraw()
    b1.deposit()
    b1.Withdraw()
    b1.display_balance()


