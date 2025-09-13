"""
Calculator module for SimpleCalc project.
Implements basic arithmetic operations.
"""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def multiCalc(a, b, operation):
    operations = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }
    if operation not in operations:
        raise ValueError(f"Unknown operation: {operation}")
    return operations[operation](a, b)