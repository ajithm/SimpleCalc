"""
Main script for SimpleCalc project.
Provides a simple CLI for calculator operations.
"""

import sys
from .calculator import add, subtract, multiply, divide

def main():
    if len(sys.argv) != 4:
        print("Usage: python -m SimpleCalc <add|subtract|multiply|divide> <num1> <num2>")
        sys.exit(1)
    op, a, b = sys.argv[1], float(sys.argv[2]), float(sys.argv[3])
    if op == "add":
        result = add(a, b)
    elif op == "subtract":
        result = subtract(a, b)
    elif op == "multiply":
        result = multiply(a, b)
    elif op == "divide":
        try:
            result = divide(a, b)
        except ValueError as e:
            print(e)
            sys.exit(1)
    else:
        print(f"Unknown operation: {op}")
        sys.exit(1)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
