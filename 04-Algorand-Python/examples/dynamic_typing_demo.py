# Dynamic Typing Demo - Regular Python

# This demonstrates how regular Python handles dynamic typing
# Run this with: python dynamic_typing_demo.py

print("=== Dynamic Typing Demo - Regular Python ===")

# 1. Variables can change types
print("\n1. Variables can change types:")
x = 10
print(f"x = {x}, type: {type(x)}")

x = "hello"
print(f"x = {x}, type: {type(x)}")

x = [1, 2, 3]
print(f"x = {x}, type: {type(x)}")

x = {"name": "Alice", "age": 30}
print(f"x = {x}, type: {type(x)}")

# 2. Functions can accept any type
print("\n2. Functions can accept any type:")
def process_data(data):
    if isinstance(data, int):
        return data * 2
    elif isinstance(data, str):
        return data.upper()
    elif isinstance(data, list):
        return len(data)
    else:
        return str(data)

# Test with different types
print(f"process_data(42): {process_data(42)}")
print(f"process_data('hello'): {process_data('hello')}")
print(f"process_data([1, 2, 3]): {process_data([1, 2, 3])}")
print(f"process_data({'a': 1}): {process_data({'a': 1})}")

# 3. Runtime type checking
print("\n3. Runtime type checking:")
def add_numbers(a, b):
    return a + b

# These work at runtime
print(f"add_numbers(5, 3): {add_numbers(5, 3)}")
print(f"add_numbers('5', '3'): {add_numbers('5', '3')}")

# This fails at runtime
try:
    result = add_numbers(5, "3")
    print(f"add_numbers(5, '3'): {result}")
except TypeError as e:
    print(f"add_numbers(5, '3'): Error - {e}")

# 4. Dynamic attribute access
print("\n4. Dynamic attribute access:")
class Wallet:
    def __init__(self, address):
        self.address = address

wallet = Wallet("ABCD1234")
print(f"Initial wallet: {wallet.address}")

# Add attributes at runtime
wallet.balance = 1000
wallet.status = "active"
wallet.created_at = "2024-01-01"

print(f"Wallet balance: {wallet.balance}")
print(f"Wallet status: {wallet.status}")
print(f"Wallet created: {wallet.created_at}")

# 5. Dynamic function creation
print("\n5. Dynamic function creation:")
def create_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier

double = create_multiplier(2)
triple = create_multiplier(3)

print(f"double(5): {double(5)}")
print(f"triple(5): {triple(5)}")

# 6. Dynamic module loading
print("\n6. Dynamic module loading:")
import importlib

# Load module dynamically
module_name = "math"
math_module = importlib.import_module(module_name)

# Use the module
result = math_module.sqrt(16)
print(f"math.sqrt(16): {result}")

# 7. Rich error handling
print("\n7. Rich error handling:")
def risky_operation():
    x = 10
    y = 0
    return x / y

try:
    result = risky_operation()
    print(f"Result: {result}")
except ZeroDivisionError as e:
    print(f"Error: {e}")
    import traceback
    print("Stack trace:")
    traceback.print_exc()

# 8. Full standard library access
print("\n8. Full standard library access:")
import os
import sys
import json
import random
import datetime

# File operations
print(f"Current directory: {os.getcwd()}")
print(f"Python version: {sys.version}")

# JSON operations
data = {"name": "Alice", "balance": 1000}
json_string = json.dumps(data)
print(f"JSON: {json_string}")

# Random operations
random_number = random.randint(1, 100)
print(f"Random number: {random_number}")

# Date operations
now = datetime.datetime.now()
print(f"Current time: {now}")

# 9. Memory usage (unlimited)
print("\n9. Memory usage (unlimited):")
# Can create large data structures
large_list = [i for i in range(100000)]
large_dict = {i: i*2 for i in range(100000)}

print(f"Large list length: {len(large_list)}")
print(f"Large dict length: {len(large_dict)}")

# 10. Performance characteristics
print("\n10. Performance characteristics:")
import time

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

start = time.time()
result = fibonacci(30)
end = time.time()
print(f"Fibonacci(30): {result}")
print(f"Time taken: {end - start:.4f} seconds")

print("\n" + "="*50)
print("Dynamic typing demo completed!")
print("Regular Python is flexible but slower due to interpretation.")
