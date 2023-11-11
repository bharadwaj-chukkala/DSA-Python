'''
Use object oriented programming to create a calculator
that can add, subtract, multiply, divide, and find the square root of numbers
It should be able to perform all of these functions both on a single number or between two numbers.
'''
import math
import numpy as np


class Calculator:
    def __init__(self, Num1, Num2) -> None:
        self.Num1 = Num1
        self.Num2 = Num2
    
    def add(self, Num1, Num2):
        return Num1 + Num2
    
    def sub(self, Num1, Num2):
        if Num1 >= Num2:
            return Num1 - Num2
        else:
            return Num2 - Num1
    
    def mul(self, Num1, Num2):
        return Num1 * Num2
    
    def div(self, Num1, Num2):
        return Num1/Num2
    
    def sroot(self, Num1):
        return math.sqrt(Num1)

if __name__=="__main__":

    
    print("Please type what operation do you want me to perform?")
    print("add - Addition")
    print("sub - Subtraction")
    print("mul - Multiplication")
    print("div - Division")
    print("sroot - Square root\n")
    Operations = ["add", "sub", "mul", "div", "sroot"]
    while True:
        Operation = input("Enter the name of your operation: ")
        if Operation not in Operations:
            print("Please input the right term")
            continue
        else:
            break

    Num1 = int(input("Enter the first value: "))
    Num2 = int(input("Enter the second number. Just press enter if you are just finding square root: "))
    my_calculation = Calculator(Num1, Num2)

    if Operation == 'add':
        print("The sum of two numbers is: ", my_calculation.add(Num1, Num2))
    if Operation == 'sub':
        print("The difference of two numbers is: ", my_calculation.sub(Num1, Num2))
    if Operation == 'mul':
        print("The product of two numbers is: ", my_calculation.mul(Num1, Num2))
    if Operation == 'div':
        print("The Division of two numbers is: ", my_calculation.div(Num1, Num2))
    if Operation == 'sroot':
        print("The square root of the number is: ", my_calculation.sroot(Num1))