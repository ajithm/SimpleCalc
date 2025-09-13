"""
Main script for SimpleCalc project.
Provides a simple CLI for calculator operations.
"""

import sys
from .calculator import add, subtract, multiply, divide, multiCalc

def main():
    if len(sys.argv) != 5:
        print("Usage: python -m SimpleCalc <add|subtract|multiply|divide> <num1> <num2>")
        sys.exit(1)
op, a, b, mOp = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), sys.argv[4]
# Uncomment and adjust the following logic as needed for your operations
# if op == "add":
#     result = add(a, b)
# elif op == "subtract":
#     result = subtract(a, b)
# elif op == "multiply":
#     result = multiply(a, b)
# elif op == "divide":
#     try:
#         result = divide(a, b)
#     except ValueError as e:
#         print(e)
#         sys.exit(1)
if op == "multiCalc":
    result = multiCalc(a, b, mOp)    
else:
    print(f"Unknown operation: {op}")
    sys.exit(1)
print(f"Result: {result}")

if __name__ == "__main__":
    main()
