# Python Basics for Blockchain Development

This guide covers essential Python concepts you'll need for Algorand development. If you're already comfortable with Python, you can skip this section.

## What is Python?

Python is a high-level, interpreted programming language known for:
- **Readability**: Code that's easy to read and understand
- **Simplicity**: Clean, concise syntax
- **Versatility**: Used in web development, data science, AI, and blockchain
- **Large community**: Extensive libraries and support

## Basic Syntax

### Variables and Data Types

```python
# Numbers
wallet_balance = 1000  # Integer
transaction_fee = 0.001  # Float

# Strings
user_address = "ABCD1234..."
message = 'Hello, Algorand!'

# Booleans
is_valid = True
is_complete = False

# Lists (arrays)
transaction_history = [100, 200, 150, 300]
user_addresses = ["addr1", "addr2", "addr3"]

# Dictionaries (key-value pairs)
account_info = {
    "address": "ABCD1234...",
    "balance": 1000,
    "status": "active"
}
```

### Comments

```python
# This is a single-line comment

"""
This is a multi-line comment
Useful for explaining complex code
"""

# Comments help explain what your code does
wallet_balance = 1000  # Current balance in microAlgos
```

## Control Flow

### If Statements

```python
wallet_balance = 1000
transaction_amount = 500

# Basic if statement
if wallet_balance >= transaction_amount:
    print("Transaction can proceed")
else:
    print("Insufficient funds")

# Multiple conditions
if wallet_balance > 1000:
    print("High balance account")
elif wallet_balance > 100:
    print("Medium balance account")
else:
    print("Low balance account")
```

### Loops

```python
# For loop - iterate through a list
transaction_amounts = [100, 200, 150, 300]
total = 0

for amount in transaction_amounts:
    total += amount
    print(f"Processing transaction: {amount}")

print(f"Total processed: {total}")

# While loop - repeat until condition is met
counter = 0
while counter < 5:
    print(f"Block number: {counter}")
    counter += 1
```

## Functions

Functions are reusable blocks of code:

```python
def calculate_fee(amount, fee_rate=0.001):
    """
    Calculate transaction fee based on amount and rate.
    
    Args:
        amount (int): Transaction amount
        fee_rate (float): Fee rate (default 0.001)
    
    Returns:
        float: Calculated fee
    """
    return amount * fee_rate

# Using the function
transaction_amount = 1000
fee = calculate_fee(transaction_amount)
print(f"Fee for {transaction_amount}: {fee}")

# Using with custom fee rate
custom_fee = calculate_fee(transaction_amount, 0.002)
print(f"Custom fee: {custom_fee}")
```

### Function with Multiple Parameters

```python
def validate_transaction(sender_balance, amount, recipient_address):
    """
    Validate if a transaction can proceed.
    
    Returns:
        bool: True if transaction is valid
    """
    # Check if sender has sufficient balance
    if sender_balance < amount:
        return False
    
    # Check if recipient address is valid (simplified)
    if len(recipient_address) < 10:
        return False
    
    return True

# Example usage
balance = 1000
amount = 500
recipient = "ABCD1234567890"

if validate_transaction(balance, amount, recipient):
    print("Transaction is valid")
else:
    print("Transaction is invalid")
```

## Error Handling

```python
def safe_divide(a, b):
    """
    Safely divide two numbers, handling division by zero.
    """
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
        return None
    except TypeError:
        print("Error: Invalid input types")
        return None

# Example usage
result1 = safe_divide(10, 2)  # Returns 5.0
result2 = safe_divide(10, 0)  # Returns None, prints error
```

## Working with Files

```python
# Writing to a file
def save_transaction_log(transactions, filename="transactions.txt"):
    """
    Save transaction data to a file.
    """
    try:
        with open(filename, 'w') as file:
            for tx in transactions:
                file.write(f"{tx}\n")
        print(f"Transactions saved to {filename}")
    except Exception as e:
        print(f"Error saving file: {e}")

# Reading from a file
def load_transaction_log(filename="transactions.txt"):
    """
    Load transaction data from a file.
    """
    try:
        with open(filename, 'r') as file:
            transactions = file.readlines()
        return [tx.strip() for tx in transactions]
    except FileNotFoundError:
        print(f"File {filename} not found")
        return []
    except Exception as e:
        print(f"Error reading file: {e}")
        return []

# Example usage
transactions = ["tx1", "tx2", "tx3"]
save_transaction_log(transactions)
loaded_transactions = load_transaction_log()
```

## Classes and Objects

```python
class Wallet:
    """
    A simple wallet class to demonstrate object-oriented programming.
    """
    
    def __init__(self, address, initial_balance=0):
        """
        Initialize a new wallet.
        
        Args:
            address (str): Wallet address
            initial_balance (int): Starting balance
        """
        self.address = address
        self.balance = initial_balance
        self.transaction_count = 0
    
    def send_transaction(self, amount, recipient):
        """
        Send a transaction to another address.
        
        Args:
            amount (int): Amount to send
            recipient (str): Recipient address
        
        Returns:
            bool: True if transaction successful
        """
        if self.balance >= amount:
            self.balance -= amount
            self.transaction_count += 1
            print(f"Sent {amount} to {recipient}")
            return True
        else:
            print("Insufficient balance")
            return False
    
    def receive_transaction(self, amount):
        """
        Receive a transaction.
        
        Args:
            amount (int): Amount received
        """
        self.balance += amount
        self.transaction_count += 1
        print(f"Received {amount}")
    
    def get_info(self):
        """
        Get wallet information.
        
        Returns:
            dict: Wallet information
        """
        return {
            "address": self.address,
            "balance": self.balance,
            "transactions": self.transaction_count
        }

# Example usage
wallet = Wallet("ABCD1234...", 1000)
print(wallet.get_info())

wallet.send_transaction(200, "EFGH5678...")
wallet.receive_transaction(100)
print(wallet.get_info())
```

## Importing Modules

```python
# Import entire module
import math

# Use functions from the module
result = math.sqrt(16)  # Returns 4.0

# Import specific functions
from math import sqrt, pi

# Use imported functions directly
result = sqrt(16)
circumference = 2 * pi * 5

# Import with alias
import datetime as dt

# Use with alias
current_time = dt.datetime.now()

# Import from custom modules (we'll create these later)
# from algopy import UInt64, Account
# from pyteal import *
```

## Best Practices

1. **Use descriptive variable names**:
   ```python
   # Good
   wallet_balance = 1000
   transaction_fee = 0.001
   
   # Bad
   wb = 1000
   tf = 0.001
   ```

2. **Write docstrings for functions**:
   ```python
   def calculate_fee(amount, rate):
       """
       Calculate transaction fee.
       
       Args:
           amount (int): Transaction amount
           rate (float): Fee rate
       
       Returns:
           float: Calculated fee
       """
       return amount * rate
   ```

3. **Handle errors gracefully**:
   ```python
   try:
       result = risky_operation()
   except SpecificError as e:
       print(f"Specific error occurred: {e}")
   except Exception as e:
       print(f"Unexpected error: {e}")
   ```

4. **Use type hints (optional but recommended)**:
   ```python
   def calculate_fee(amount: int, rate: float) -> float:
       return amount * rate
   ```

## Practice Exercises

Try these exercises to reinforce your Python knowledge:

1. **Create a simple calculator** that can add, subtract, multiply, and divide
2. **Build a basic address validator** that checks if an address has the right format
3. **Write a function** that processes a list of transaction amounts and returns statistics
4. **Create a simple class** for managing a list of contacts

## Next Steps

Now that you understand Python basics, you're ready to:
1. Learn about blockchain fundamentals in `01-Blockchain-Introduction/`
2. Start working with Algorand-specific Python features

## Additional Resources

- [Python Official Tutorial](https://docs.python.org/3/tutorial/)
- [Python for Beginners](https://www.python.org/about/gettingstarted/)
- [Real Python Tutorials](https://realpython.com/)
