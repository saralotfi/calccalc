import math

class Operation:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b): 
        return a * b
    def divide(self, a, b): 
        if b != 0:
            return a / b 
        else :
            return "Error: Division by zero!"
    def power(self, a, b): 
        return a ** b
    def modulus(self, a, b): 
        return a % b
    def cosine(self, a): 
        return math.cos(a)
    def sine(self, a): 
        return math.sin(a)
    def radical(self, a): 
        return math.sqrt(a)

class Calculator:
    def __init__(self, operation):
        self.operation = operation
    
    def answer(self, operation, a, b=None):
        if operation == '+':
            return self.operation.add(a, b)
        elif operation == '-':
            return self.operation.subtract(a, b)
        elif operation == '*':
            return self.operation.multiply(a, b)
        elif operation == '/':
            return self.operation.divide(a, b)
        elif operation == '**':
            return self.operation.power(a, b)
        elif operation == '%':
            return self.operation.modulus(a, b)
        elif operation == 'cos':
            return self.operation.cosine(a)
        elif operation == 'sin':
            return self.operation.sine(a)
        elif operation == 'radical':
            return self.operation.radical(a)
        else:
            return "Invalid operation!"


calculator = Calculator(Operation())

while True:
    a = float(input("Enter the first number: "))
    operation = input("Enter the operation (+, -, *, /, **, %, cos, sin, radical): ")
    b = None
    if operation in ['+', '-', '*', '/', '**', '%']:
        b = float(input("Enter the second number: "))
    result = calculator.answer(operation, a, b)
    print("Result:", result)
    if input("Do you want to continue? (yes/no): ") != "yes":
        break
