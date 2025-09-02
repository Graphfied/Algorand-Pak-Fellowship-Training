# Type Error Demo - Comparing Regular Python vs Algorand Python

# This demonstrates the differences in error handling between regular Python and Algorand Python

print("=== Type Error Demo ===")

# 1. Regular Python - Runtime Type Errors
print("\n1. Regular Python - Runtime Type Errors:")

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
    print(f"add_numbers(5, '3'): Runtime Error - {e}")

# 2. Regular Python - Dynamic Type Changes
print("\n2. Regular Python - Dynamic Type Changes:")

x = 10
print(f"x = {x}, type: {type(x)}")

x = "hello"
print(f"x = {x}, type: {type(x)}")

x = [1, 2, 3]
print(f"x = {x}, type: {type(x)}")

# 3. Regular Python - Type Checking at Runtime
print("\n3. Regular Python - Type Checking at Runtime:")

def process_data(data):
    if isinstance(data, int):
        return data * 2
    elif isinstance(data, str):
        return data.upper()
    elif isinstance(data, list):
        return len(data)
    else:
        return str(data)

# Type checking happens at runtime
print(f"process_data(42): {process_data(42)}")
print(f"process_data('hello'): {process_data('hello')}")
print(f"process_data([1, 2, 3]): {process_data([1, 2, 3])}")

# 4. Regular Python - Rich Error Information
print("\n4. Regular Python - Rich Error Information:")

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

# 5. Algorand Python - Compile-Time Type Errors (Simulated)
print("\n5. Algorand Python - Compile-Time Type Errors (Simulated):")
print("# In Algorand Python:")
print("from algopy import UInt64, String")
print("")
print("def add_numbers(a: UInt64, b: UInt64) -> UInt64:")
print("    return a + b")
print("")
print("# These are checked at compile time")
print("result1 = add_numbers(UInt64(5), UInt64(3))  # Correct")
print("# result2 = add_numbers(UInt64(5), String('3'))  # Compile error!")
print("# result3 = add_numbers(5, 3)  # Compile error!")

# 6. Algorand Python - No Dynamic Type Changes (Simulated)
print("\n6. Algorand Python - No Dynamic Type Changes (Simulated):")
print("# In Algorand Python:")
print("amount: UInt64 = UInt64(1000)")
print("# amount = String('hello')  # Compile error!")
print("# Variables cannot change types")

# 7. Algorand Python - Type Safety (Simulated)
print("\n7. Algorand Python - Type Safety (Simulated):")
print("# In Algorand Python:")
print("def process_data(amount: UInt64, name: String) -> UInt64:")
print("    # Cannot mix types")
print("    # return amount + name  # Compile error!")
print("    return amount")

# 8. Algorand Python - No Runtime Type Errors (Simulated)
print("\n8. Algorand Python - No Runtime Type Errors (Simulated):")
print("# In Algorand Python:")
print("def safe_operation(amount: UInt64) -> UInt64:")
print("    # All type errors caught at compile time")
print("    # No runtime type checking needed")
print("    return amount * UInt64(2)")

# 9. Algorand Python - Limited Error Information (Simulated)
print("\n9. Algorand Python - Limited Error Information (Simulated):")
print("# In Algorand Python:")
print("def risky_operation() -> UInt64:")
print("    # No try-except blocks")
print("    # Errors cause transaction failure")
print("    # Limited error information")
print("    return UInt64(1)")

# 10. Comparison Summary
print("\n10. Comparison Summary:")
print("Regular Python:")
print("  - Types checked at runtime")
print("  - Dynamic type changes allowed")
print("  - Rich error information")
print("  - Runtime type errors")
print("  - Flexible but slower")
print("")
print("Algorand Python:")
print("  - Types checked at compile time")
print("  - No dynamic type changes")
print("  - Limited error information")
print("  - No runtime type errors")
print("  - Type-safe but less flexible")

# 11. Error Prevention Examples
print("\n11. Error Prevention Examples:")

# Regular Python - Manual error prevention
def safe_add_regular(a, b):
    try:
        return a + b
    except TypeError:
        return None

print(f"safe_add_regular(5, 3): {safe_add_regular(5, 3)}")
print(f"safe_add_regular(5, '3'): {safe_add_regular(5, '3')}")

# Algorand Python - Compile-time error prevention (simulated)
print("\n# Algorand Python - Compile-time error prevention:")
print("def safe_add_algorand(a: UInt64, b: UInt64) -> UInt64:")
print("    # Compiler ensures types are correct")
print("    # No runtime type checking needed")
print("    return a + b")

# 12. Performance Implications
print("\n12. Performance Implications:")

# Regular Python - Runtime type checking overhead
import time

def slow_operation():
    start = time.time()
    for i in range(1000000):
        if isinstance(i, int):
            pass
    end = time.time()
    return end - start

overhead = slow_operation()
print(f"Regular Python type checking overhead: {overhead:.4f} seconds")

# Algorand Python - No runtime type checking (simulated)
print("\n# Algorand Python - No runtime type checking:")
print("# Types are checked at compile time")
print("# No runtime overhead")
print("# Better performance")

# 13. Development Workflow Differences
print("\n13. Development Workflow Differences:")
print("Regular Python:")
print("  1. Write code")
print("  2. Run directly")
print("  3. Fix runtime errors")
print("  4. Repeat")
print("")
print("Algorand Python:")
print("  1. Write code")
print("  2. Compile (catch type errors)")
print("  3. Deploy to blockchain")
print("  4. Execute")

# 14. Best Practices
print("\n14. Best Practices:")
print("Regular Python:")
print("  - Use type hints for better documentation")
print("  - Implement runtime error handling")
print("  - Test with different data types")
print("  - Use isinstance() for type checking")
print("")
print("Algorand Python:")
print("  - Always declare types explicitly")
print("  - Validate inputs manually")
print("  - Test thoroughly before deployment")
print("  - Use ARC4 types consistently")

print("\n" + "="*50)
print("Type error demo completed!")
print("Understanding these differences helps choose the right approach.")
