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

**What are variables?**
Variables are like labeled boxes that store data. In Python, you create a variable by giving it a name and assigning a value with the `=` sign.

```python
# Numbers - Used for calculations and counting
wallet_balance = 1000  # Integer: Whole numbers (no decimals)
transaction_fee = 0.001  # Float: Decimal numbers

# Explanation: 
# - wallet_balance stores a whole number (1000 microAlgos)
# - transaction_fee stores a decimal number (0.001 Algos)
# - Python automatically determines the data type based on the value

# Strings - Text data enclosed in quotes
user_address = "ABCD1234..."  # Double quotes
message = 'Hello, Algorand!'  # Single quotes (both work the same)

# Explanation:
# - Strings are used for text, addresses, messages
# - Can use single or double quotes
# - The "..." indicates this is a shortened address for example

# Booleans - True or False values
is_valid = True   # Boolean: Represents a true condition
is_complete = False  # Boolean: Represents a false condition

# Explanation:
# - Booleans are used for yes/no, on/off, valid/invalid decisions
# - Only two possible values: True or False
# - Essential for making decisions in code

# Lists - Ordered collections of items (like arrays)
transaction_history = [100, 200, 150, 300]  # List of numbers
user_addresses = ["addr1", "addr2", "addr3"]  # List of strings

# Explanation:
# - Lists store multiple items in order
# - Items are separated by commas
# - Can access items by position (first item is at position 0)
# - transaction_history[0] would give us 100

# Dictionaries - Key-value pairs (like a phone book)
account_info = {
    "address": "ABCD1234...",  # Key: "address", Value: "ABCD1234..."
    "balance": 1000,           # Key: "balance", Value: 1000
    "status": "active"         # Key: "status", Value: "active"
}

# Explanation:
# - Dictionaries store data in pairs: key and value
# - Keys are like labels, values are the actual data
# - Access data using the key: account_info["balance"] gives 1000
# - Useful for storing structured data about accounts, transactions, etc.
```

### Comments

**What are comments?**
Comments are notes you write in your code that Python ignores. They help explain what your code does and make it easier for others (and yourself) to understand.

```python
# This is a single-line comment
# Comments start with a # symbol
# Everything after # on the same line is ignored by Python

"""
This is a multi-line comment
Useful for explaining complex code
You can write multiple lines
Python will ignore everything between the triple quotes
"""

# Comments help explain what your code does
wallet_balance = 1000  # Current balance in microAlgos

# Explanation:
# - Single-line comments start with # and go to the end of the line
# - Multi-line comments use triple quotes (""" or ''')
# - Comments are essential for documenting your code
# - They don't affect how your program runs, but make it readable
```

## Control Flow

### If Statements

**What are if statements?**
If statements let your program make decisions. They check if a condition is true or false, then run different code based on the result.

```python
# Set up our variables
wallet_balance = 1000  # Current balance in the wallet
transaction_amount = 500  # Amount we want to send

# Basic if statement - checks if we have enough money
if wallet_balance >= transaction_amount:  # >= means "greater than or equal to"
    print("Transaction can proceed")  # This runs if we have enough money
else:  # This runs if the condition above is false
    print("Insufficient funds")  # This runs if we don't have enough money

# Explanation:
# - if checks a condition (wallet_balance >= transaction_amount)
# - If true, runs the code after the colon
# - else runs if the condition is false
# - The indentation (4 spaces) shows which code belongs to which block

# Multiple conditions - checking different ranges
if wallet_balance > 1000:  # First condition: more than 1000
    print("High balance account")  # Runs if balance > 1000
elif wallet_balance > 100:  # Second condition: between 100 and 1000
    print("Medium balance account")  # Runs if 100 < balance <= 1000
else:  # Final condition: 100 or less
    print("Low balance account")  # Runs if balance <= 100

# Explanation:
# - elif means "else if" - check another condition if the first is false
# - Only one block will run (the first true condition)
# - else catches everything else that doesn't match the conditions above
```

### Loops

**What are loops?**
Loops let you repeat code multiple times. Instead of writing the same code over and over, you can use loops to do it automatically.

```python
# For loop - go through each item in a list one by one
transaction_amounts = [100, 200, 150, 300]  # List of transaction amounts
total = 0  # Start with zero total

# This loop runs once for each item in the list
for amount in transaction_amounts:  # "amount" takes each value from the list
    total += amount  # Add this amount to our total (same as total = total + amount)
    print(f"Processing transaction: {amount}")  # Print what we're processing

print(f"Total processed: {total}")  # Print the final total

# Explanation:
# - for amount in transaction_amounts means "for each amount in the list"
# - First time: amount = 100, total becomes 100
# - Second time: amount = 200, total becomes 300
# - Third time: amount = 150, total becomes 450
# - Fourth time: amount = 300, total becomes 750
# - The f"..." is an f-string for formatting text with variables

# While loop - keep repeating until a condition becomes false
counter = 0  # Start counting from 0
while counter < 5:  # Keep looping while counter is less than 5
    print(f"Block number: {counter}")  # Print the current block number
    counter += 1  # Add 1 to counter (same as counter = counter + 1)

# Explanation:
# - while counter < 5 means "keep looping while counter is less than 5"
# - First time: counter = 0, prints "Block number: 0", counter becomes 1
# - Second time: counter = 1, prints "Block number: 1", counter becomes 2
# - This continues until counter = 5, then the condition becomes false and loop stops
# - Be careful: if you forget to increase counter, the loop runs forever!
```

## Functions

**What are functions?**
Functions are like recipes - they're reusable blocks of code that do a specific task. Instead of writing the same code multiple times, you write it once in a function and call it whenever you need it.

```python
# Define a function to calculate transaction fees
def calculate_fee(amount, fee_rate=0.001):  # Function name and parameters
    """
    Calculate transaction fee based on amount and rate.
    
    Args:
        amount (int): Transaction amount
        fee_rate (float): Fee rate (default 0.001)
    
    Returns:
        float: Calculated fee
    """
    return amount * fee_rate  # Multiply amount by fee rate and return the result

# Explanation:
# - def means "define a function"
# - calculate_fee is the function name
# - amount and fee_rate are parameters (inputs the function needs)
# - fee_rate=0.001 means if no fee_rate is provided, use 0.001 as default
# - return sends the result back to whoever called the function
# - The docstring (triple quotes) explains what the function does

# Using the function - call it with just the amount
transaction_amount = 1000  # We want to send 1000 microAlgos
fee = calculate_fee(transaction_amount)  # Call function with amount, use default fee rate
print(f"Fee for {transaction_amount}: {fee}")  # Print the result

# Explanation:
# - calculate_fee(transaction_amount) calls the function
# - Python uses the default fee_rate of 0.001
# - The function returns 1000 * 0.001 = 1.0
# - We store this result in the variable 'fee'

# Using with custom fee rate - provide both parameters
custom_fee = calculate_fee(transaction_amount, 0.002)  # Call with custom fee rate
print(f"Custom fee: {custom_fee}")  # Print the custom fee

# Explanation:
# - calculate_fee(transaction_amount, 0.002) provides both parameters
# - amount = 1000, fee_rate = 0.002
# - The function returns 1000 * 0.002 = 2.0
# - This overrides the default fee rate
```

### Function with Multiple Parameters

**Functions can take multiple inputs and make decisions:**

```python
def validate_transaction(sender_balance, amount, recipient_address):
    """
    Validate if a transaction can proceed.
    
    Returns:
        bool: True if transaction is valid
    """
    # Check if sender has sufficient balance
    if sender_balance < amount:  # If not enough money
        return False  # Transaction is invalid
    
    # Check if recipient address is valid (simplified check)
    if len(recipient_address) < 10:  # If address is too short
        return False  # Transaction is invalid
    
    return True  # If we get here, transaction is valid

# Explanation:
# - This function takes 3 parameters: sender_balance, amount, recipient_address
# - It checks two conditions before allowing the transaction
# - If either condition fails, it returns False (invalid)
# - If both conditions pass, it returns True (valid)
# - return False stops the function immediately and sends back False
# - return True only runs if the previous checks passed

# Example usage - test the function with real data
balance = 1000  # Sender has 1000 microAlgos
amount = 500    # Wants to send 500 microAlgos
recipient = "ABCD1234567890"  # Recipient address (12 characters)

# Call the function and check the result
if validate_transaction(balance, amount, recipient):  # If function returns True
    print("Transaction is valid")  # Print success message
else:  # If function returns False
    print("Transaction is invalid")  # Print error message

# Explanation:
# - validate_transaction(balance, amount, recipient) calls our function
# - The function checks: 1000 >= 500 (True) and len("ABCD1234567890") >= 10 (True)
# - Since both checks pass, the function returns True
# - The if statement sees True, so it prints "Transaction is valid"
```

## Error Handling

**What is error handling?**
Sometimes your code might encounter problems (like dividing by zero or trying to open a file that doesn't exist). Error handling lets you catch these problems and deal with them gracefully instead of crashing.

```python
def safe_divide(a, b):
    """
    Safely divide two numbers, handling division by zero.
    """
    try:  # Try to run this code
        result = a / b  # Attempt the division
        return result  # If successful, return the result
    except ZeroDivisionError:  # If we try to divide by zero
        print("Error: Cannot divide by zero")  # Print a helpful message
        return None  # Return None instead of crashing
    except TypeError:  # If we get wrong data types (like dividing text)
        print("Error: Invalid input types")  # Print a helpful message
        return None  # Return None instead of crashing

# Explanation:
# - try: means "try to run this code"
# - except: means "if this specific error happens, do this instead"
# - ZeroDivisionError happens when you divide by zero
# - TypeError happens when you use wrong data types
# - return None means "no valid result" instead of crashing the program

# Example usage - test the function with different inputs
result1 = safe_divide(10, 2)  # Normal division: 10 ÷ 2 = 5.0
print(f"10 ÷ 2 = {result1}")  # Prints: 10 ÷ 2 = 5.0

result2 = safe_divide(10, 0)  # Division by zero: should cause error
print(f"10 ÷ 0 = {result2}")  # Prints: Error: Cannot divide by zero, then 10 ÷ 0 = None

# Explanation:
# - safe_divide(10, 2) works normally, returns 5.0
# - safe_divide(10, 0) tries to divide by zero
# - The except ZeroDivisionError catches this and prints an error message
# - Instead of crashing, it returns None
# - This prevents your program from stopping unexpectedly
```

## Working with Files

**What is file handling?**
File handling lets your program read data from files and save data to files. This is useful for storing transaction logs, user data, or any information you want to keep between program runs.

```python
# Writing to a file - save data to disk
def save_transaction_log(transactions, filename="transactions.txt"):
    """
    Save transaction data to a file.
    """
    try:  # Try to write to the file
        with open(filename, 'w') as file:  # Open file for writing ('w' mode)
            for tx in transactions:  # Go through each transaction
                file.write(f"{tx}\n")  # Write each transaction on a new line
        print(f"Transactions saved to {filename}")  # Confirm success
    except Exception as e:  # If any error occurs
        print(f"Error saving file: {e}")  # Print the error message

# Explanation:
# - with open(filename, 'w') opens a file for writing
# - 'w' mode means "write" (creates new file or overwrites existing)
# - file.write() adds text to the file
# - \n adds a new line after each transaction
# - with automatically closes the file when done
# - try/except handles any errors that might occur

# Reading from a file - load data from disk
def load_transaction_log(filename="transactions.txt"):
    """
    Load transaction data from a file.
    """
    try:  # Try to read from the file
        with open(filename, 'r') as file:  # Open file for reading ('r' mode)
            transactions = file.readlines()  # Read all lines into a list
        return [tx.strip() for tx in transactions]  # Remove newline characters
    except FileNotFoundError:  # If file doesn't exist
        print(f"File {filename} not found")  # Print helpful message
        return []  # Return empty list
    except Exception as e:  # If any other error occurs
        print(f"Error reading file: {e}")  # Print the error message
        return []  # Return empty list

# Explanation:
# - with open(filename, 'r') opens a file for reading
# - 'r' mode means "read" (can't modify the file)
# - file.readlines() reads all lines and puts them in a list
# - tx.strip() removes the \n characters from each line
# - FileNotFoundError specifically handles missing files
# - If file doesn't exist, we return an empty list instead of crashing

# Example usage - test the file functions
transactions = ["tx1", "tx2", "tx3"]  # Some sample transaction data
save_transaction_log(transactions)  # Save to file
loaded_transactions = load_transaction_log()  # Load from file
print(f"Loaded transactions: {loaded_transactions}")  # Print what we loaded

# Explanation:
# - We create a list of transactions
# - save_transaction_log() writes them to "transactions.txt"
# - load_transaction_log() reads them back from the file
# - The loaded data should be the same as what we saved
# - This demonstrates how to persist data between program runs
```

## Classes and Objects

**What are classes and objects?**
Classes are like blueprints for creating objects. Think of a class as a cookie cutter and objects as the cookies. In blockchain, you might have a Wallet class that creates individual wallet objects.

```python
class Wallet:  # Define a class called Wallet
    """
    A simple wallet class to demonstrate object-oriented programming.
    """
    
    def __init__(self, address, initial_balance=0):  # Constructor - runs when creating a new wallet
        """
        Initialize a new wallet.
        
        Args:
            address (str): Wallet address
            initial_balance (int): Starting balance
        """
        self.address = address  # Store the wallet address
        self.balance = initial_balance  # Store the starting balance
        self.transaction_count = 0  # Start with zero transactions
    
    # Explanation:
    # - __init__ is a special method that runs when you create a new wallet
    # - self refers to the specific wallet object being created
    # - self.address stores the address for this wallet
    # - self.balance stores the balance for this wallet
    # - Each wallet object has its own address and balance
    
    def send_transaction(self, amount, recipient):  # Method to send money
        """
        Send a transaction to another address.
        
        Args:
            amount (int): Amount to send
            recipient (str): Recipient address
        
        Returns:
            bool: True if transaction successful
        """
        if self.balance >= amount:  # Check if we have enough money
            self.balance -= amount  # Subtract amount from our balance
            self.transaction_count += 1  # Increase transaction counter
            print(f"Sent {amount} to {recipient}")  # Print confirmation
            return True  # Transaction successful
        else:  # Not enough money
            print("Insufficient balance")  # Print error message
            return False  # Transaction failed
    
    # Explanation:
    # - This method belongs to the wallet object
    # - It checks if we have enough balance before sending
    # - If successful, it updates the balance and transaction count
    # - It returns True/False to indicate success/failure
    
    def receive_transaction(self, amount):  # Method to receive money
        """
        Receive a transaction.
        
        Args:
            amount (int): Amount received
        """
        self.balance += amount  # Add amount to our balance
        self.transaction_count += 1  # Increase transaction counter
        print(f"Received {amount}")  # Print confirmation
    
    # Explanation:
    # - This method adds money to the wallet
    # - It also increases the transaction counter
    # - No validation needed for receiving money
    
    def get_info(self):  # Method to get wallet information
        """
        Get wallet information.
        
        Returns:
            dict: Wallet information
        """
        return {  # Return a dictionary with wallet details
            "address": self.address,
            "balance": self.balance,
            "transactions": self.transaction_count
        }
    
    # Explanation:
    # - This method returns all the important wallet information
    # - It's useful for checking the wallet status
    # - Returns a dictionary that's easy to read

# Example usage - create and use wallet objects
wallet = Wallet("ABCD1234...", 1000)  # Create a new wallet with address and 1000 balance
print(wallet.get_info())  # Print initial wallet info

wallet.send_transaction(200, "EFGH5678...")  # Try to send 200 to another address
wallet.receive_transaction(100)  # Receive 100 from someone
print(wallet.get_info())  # Print updated wallet info

# Explanation:
# - Wallet("ABCD1234...", 1000) creates a new wallet object
# - The __init__ method runs and sets up the wallet
# - wallet.send_transaction() calls the send method on this specific wallet
# - wallet.receive_transaction() calls the receive method on this specific wallet
# - Each wallet object maintains its own balance and transaction count
```

## Object-Oriented Programming (OOP) Concepts

**What is Object-Oriented Programming?**
OOP is a programming approach that organizes code around objects and classes. Think of it like organizing a library - instead of having all books scattered around, you organize them into categories (classes) and each book (object) has specific properties and behaviors.

### The Four Pillars of OOP

#### 1. Encapsulation - Data Hiding and Protection

**What is Encapsulation?**
Encapsulation means keeping data and methods together inside a class, and controlling access to them. It's like a capsule that protects what's inside.

```python
class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number  # Public attribute
        self._balance = initial_balance       # Protected attribute (single underscore)
        self.__pin = "1234"                   # Private attribute (double underscore)
    
    def get_balance(self):  # Public method to access balance
        return self._balance
    
    def deposit(self, amount):  # Public method to deposit money
        if amount > 0:
            self._balance += amount
            print(f"Deposited {amount}. New balance: {self._balance}")
        else:
            print("Invalid amount")
    
    def withdraw(self, amount, pin):  # Public method to withdraw money
        if pin == self.__pin:  # Check PIN before allowing withdrawal
            if amount > 0 and amount <= self._balance:
                self._balance -= amount
                print(f"Withdrew {amount}. New balance: {self._balance}")
            else:
                print("Invalid amount or insufficient funds")
        else:
            print("Invalid PIN")
    
    def _validate_transaction(self, amount):  # Protected method (internal use)
        return amount > 0 and amount <= self._balance

# Example usage
account = BankAccount("ACC123", 1000)
print(f"Account balance: {account.get_balance()}")  # Access balance safely
account.deposit(500)  # Deposit money
account.withdraw(200, "1234")  # Withdraw with correct PIN
account.withdraw(200, "0000")  # Try to withdraw with wrong PIN

# Explanation:
# - account_number is public (can be accessed directly)
# - _balance is protected (should be accessed through methods)
# - __pin is private (cannot be accessed from outside the class)
# - get_balance() provides controlled access to the balance
# - withdraw() validates PIN before allowing withdrawal
# - _validate_transaction() is for internal use only
```

#### 2. Inheritance - Code Reuse and Extension

**What is Inheritance?**
Inheritance allows a class to inherit properties and methods from another class. It's like a family tree - children inherit traits from their parents.

```python
# Parent class (base class)
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0
    
    def start_engine(self):
        print(f"{self.brand} {self.model} engine started")
    
    def accelerate(self, speed_increase):
        self.speed += speed_increase
        print(f"Speed increased to {self.speed} km/h")
    
    def get_info(self):
        return f"{self.year} {self.brand} {self.model}"

# Child class (derived class) - inherits from Vehicle
class Car(Vehicle):  # Car inherits from Vehicle
    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)  # Call parent's __init__
        self.doors = doors
        self.fuel_type = "Gasoline"
    
    def honk(self):  # New method specific to Car
        print("Beep beep!")
    
    def get_info(self):  # Override parent's method
        return f"{super().get_info()} with {self.doors} doors"

# Another child class
class Motorcycle(Vehicle):  # Motorcycle also inherits from Vehicle
    def __init__(self, brand, model, year, engine_size):
        super().__init__(brand, model, year)
        self.engine_size = engine_size
        self.fuel_type = "Gasoline"
    
    def wheelie(self):  # New method specific to Motorcycle
        print("Doing a wheelie!")
    
    def get_info(self):  # Override parent's method
        return f"{super().get_info()} with {self.engine_size}cc engine"

# Example usage
car = Car("Toyota", "Camry", 2023, 4)
motorcycle = Motorcycle("Honda", "CBR600", 2023, 600)

# Both can use inherited methods
car.start_engine()  # Inherited from Vehicle
motorcycle.start_engine()  # Inherited from Vehicle

# Each has its own specific methods
car.honk()  # Specific to Car
motorcycle.wheelie()  # Specific to Motorcycle

# Both can override parent methods
print(car.get_info())  # Uses Car's version
print(motorcycle.get_info())  # Uses Motorcycle's version

# Explanation:
# - Vehicle is the parent class with common properties
# - Car and Motorcycle inherit from Vehicle using (Vehicle)
# - super() calls the parent class methods
# - Child classes can add new methods (honk, wheelie)
# - Child classes can override parent methods (get_info)
```

#### 3. Polymorphism - One Interface, Multiple Forms

**What is Polymorphism?**
Polymorphism allows objects of different classes to be treated as objects of a common parent class. It's like having different types of animals that all make sounds, but each makes a different sound.

```python
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):  # This will be overridden by child classes
        return "Some generic animal sound"

# Child classes
class Dog(Animal):
    def make_sound(self):  # Override parent method
        return f"{self.name} says Woof!"

class Cat(Animal):
    def make_sound(self):  # Override parent method
        return f"{self.name} says Meow!"

class Bird(Animal):
    def make_sound(self):  # Override parent method
        return f"{self.name} says Tweet!"

# Function that demonstrates polymorphism
def animal_concert(animals):
    for animal in animals:
        print(animal.make_sound())  # Same method call, different behaviors

# Example usage
animals = [
    Dog("Buddy"),
    Cat("Whiskers"),
    Bird("Tweety"),
    Dog("Max")
]

animal_concert(animals)  # Each animal makes its own sound

# Explanation:
# - All animals have a make_sound() method
# - Each animal type implements it differently
# - The animal_concert() function treats all animals the same way
# - Python automatically calls the correct make_sound() method for each animal
# - This is polymorphism - same interface, different implementations
```

#### 4. Abstraction - Hiding Complex Implementation

**What is Abstraction?**
Abstraction hides complex implementation details and shows only the essential features. It's like a car - you don't need to know how the engine works to drive it.

```python
from abc import ABC, abstractmethod  # Import for abstract classes

# Abstract class (cannot be instantiated directly)
class PaymentProcessor(ABC):  # ABC means Abstract Base Class
    def __init__(self, account_id):
        self.account_id = account_id
    
    @abstractmethod  # This method must be implemented by child classes
    def process_payment(self, amount):
        pass  # No implementation here
    
    def validate_amount(self, amount):  # Common method for all processors
        return amount > 0 and amount <= 10000

# Concrete implementations
class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        if self.validate_amount(amount):
            print(f"Processing ${amount} with Credit Card {self.account_id}")
            return True
        else:
            print("Invalid amount")
            return False

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        if self.validate_amount(amount):
            print(f"Processing ${amount} with PayPal {self.account_id}")
            return True
        else:
            print("Invalid amount")
            return False

class CryptoProcessor(PaymentProcessor):
    def process_payment(self, amount):
        if self.validate_amount(amount):
            print(f"Processing ${amount} with Crypto {self.account_id}")
            return True
        else:
            print("Invalid amount")
            return False

# Example usage
processors = [
    CreditCardProcessor("1234-5678-9012-3456"),
    PayPalProcessor("user@example.com"),
    CryptoProcessor("0x1234567890abcdef")
]

amount = 100
for processor in processors:
    processor.process_payment(amount)

# Explanation:
# - PaymentProcessor is abstract - you can't create it directly
# - @abstractmethod means child classes MUST implement this method
# - validate_amount() is common to all processors
# - Each processor implements process_payment() differently
# - The user doesn't need to know the internal details of each processor
```

### OOP in Blockchain Context

**How OOP applies to blockchain development:**

```python
class SmartContract:
    def __init__(self, contract_id, creator_address):
        self.contract_id = contract_id
        self.creator_address = creator_address
        self.state = {}
        self.transactions = []
    
    def execute_transaction(self, transaction):
        # Abstract method - each contract type implements differently
        pass

class TokenContract(SmartContract):
    def __init__(self, contract_id, creator_address, token_name, total_supply):
        super().__init__(contract_id, creator_address)
        self.token_name = token_name
        self.total_supply = total_supply
        self.balances = {}
    
    def execute_transaction(self, transaction):
        if transaction['type'] == 'transfer':
            return self._transfer(transaction)
        elif transaction['type'] == 'mint':
            return self._mint(transaction)
        return False
    
    def _transfer(self, transaction):
        from_addr = transaction['from']
        to_addr = transaction['to']
        amount = transaction['amount']
        
        if self.balances.get(from_addr, 0) >= amount:
            self.balances[from_addr] -= amount
            self.balances[to_addr] = self.balances.get(to_addr, 0) + amount
            return True
        return False
    
    def _mint(self, transaction):
        to_addr = transaction['to']
        amount = transaction['amount']
        
        if self.balances.get(to_addr, 0) + amount <= self.total_supply:
            self.balances[to_addr] = self.balances.get(to_addr, 0) + amount
            return True
        return False

# Example usage
token_contract = TokenContract("CONTRACT123", "CREATOR456", "MyToken", 1000000)
print(f"Created {token_contract.token_name} contract")

# Explanation:
# - SmartContract is the base class with common properties
# - TokenContract inherits from SmartContract
# - Each contract type can have different transaction types
# - OOP helps organize complex blockchain logic into manageable pieces
```

### OOP Best Practices

1. **Single Responsibility Principle**: Each class should have one job
2. **Open/Closed Principle**: Open for extension, closed for modification
3. **Liskov Substitution Principle**: Child classes should be substitutable for parent classes
4. **Interface Segregation**: Don't force classes to depend on methods they don't use
5. **Dependency Inversion**: Depend on abstractions, not concretions

## Importing Modules

**What are modules?**
Modules are pre-written code that you can use in your programs. Instead of writing everything from scratch, you can import useful functions and classes from modules. Python comes with many built-in modules, and you can install additional ones.

```python
# Import entire module - brings in all functions from the module
import math  # Import the math module (contains mathematical functions)

# Use functions from the module - need to specify the module name
result = math.sqrt(16)  # math.sqrt() calculates square root, returns 4.0
print(f"Square root of 16: {result}")  # Prints: Square root of 16: 4.0

# Explanation:
# - import math brings in the entire math module
# - To use functions, you write module_name.function_name()
# - math.sqrt() calculates the square root
# - This method is clear but requires typing the module name each time

# Import specific functions - brings in only what you need
from math import sqrt, pi  # Import only sqrt and pi from math module

# Use imported functions directly - no need for module name
result = sqrt(16)  # Use sqrt directly, returns 4.0
circumference = 2 * pi * 5  # Use pi directly, calculates 2 * 3.14159... * 5
print(f"Square root: {result}, Circumference: {circumference}")

# Explanation:
# - from math import sqrt, pi brings in only specific functions
# - You can use sqrt() and pi() directly without math.
# - This is shorter but you need to know exactly what you're importing
# - pi is a constant (approximately 3.14159...)

# Import with alias - give the module a shorter name
import datetime as dt  # Import datetime module but call it 'dt'

# Use with alias - use the shorter name
current_time = dt.datetime.now()  # Get current date and time
print(f"Current time: {current_time}")

# Explanation:
# - import datetime as dt creates an alias 'dt' for 'datetime'
# - This is useful when module names are long
# - dt.datetime.now() is shorter than datetime.datetime.now()
# - Aliases make code more readable

# Import from custom modules (we'll create these later)
# from algopy import UInt64, Account  # Import Algorand-specific types
# from pyteal import *  # Import all PyTeal functions (be careful with *)

# Explanation:
# - These are examples of importing from Algorand-specific modules
# - algopy contains Algorand Python types like UInt64, Account
# - pyteal contains functions for writing smart contracts
# - The * imports everything (convenient but can cause naming conflicts)
```

## Best Practices

**What are best practices?**
Best practices are coding habits that make your code better - easier to read, more reliable, and easier to maintain. Following these practices will make you a better programmer.

1. **Use descriptive variable names** - make your code self-explanatory:
   ```python
   # Good - names clearly describe what the variable contains
   wallet_balance = 1000      # Clearly shows this is a wallet's balance
   transaction_fee = 0.001    # Clearly shows this is a transaction fee
   user_address = "ABC123"    # Clearly shows this is a user's address
   
   # Bad - names are unclear and confusing
   wb = 1000      # What is wb? Wallet balance? Water bottle?
   tf = 0.001     # What is tf? Transaction fee? Total funds?
   ua = "ABC123"  # What is ua? User address? Unknown account?
   
   # Explanation:
   # - Good names make code self-documenting
   # - You can understand what the code does without comments
   # - Other programmers (and future you) will thank you
   ```

2. **Write docstrings for functions** - document what your functions do:
   ```python
   def calculate_fee(amount, rate):
       """
       Calculate transaction fee based on amount and rate.
       
       Args:
           amount (int): Transaction amount in microAlgos
           rate (float): Fee rate as a decimal (0.001 = 0.1%)
       
       Returns:
           float: Calculated fee amount
       
       Example:
           >>> calculate_fee(1000, 0.001)
           1.0
       """
       return amount * rate
   
   # Explanation:
   # - Docstrings explain what the function does
   # - Args section describes each parameter
   # - Returns section describes what the function gives back
   # - Example shows how to use the function
   # - This helps other programmers understand your code
   ```

3. **Handle errors gracefully** - don't let your program crash unexpectedly:
   ```python
   def safe_divide(a, b):
       """
       Safely divide two numbers, handling errors gracefully.
       """
       try:  # Try to do the division
           result = a / b
           return result
       except ZeroDivisionError as e:  # Catch specific error
           print(f"Error: Cannot divide by zero - {e}")
           return None  # Return None instead of crashing
       except TypeError as e:  # Catch another specific error
           print(f"Error: Invalid input types - {e}")
           return None
       except Exception as e:  # Catch any other unexpected errors
           print(f"Unexpected error occurred: {e}")
           return None
   
   # Explanation:
   # - try/except prevents your program from crashing
   # - Catch specific errors first, then general ones
   # - Provide helpful error messages
   # - Return sensible defaults instead of crashing
   ```

4. **Use type hints (optional but recommended)** - make your code more self-documenting:
   ```python
   def calculate_fee(amount: int, rate: float) -> float:
       """
       Calculate transaction fee with type hints.
       
       Args:
           amount: Transaction amount (must be integer)
           rate: Fee rate (must be decimal number)
       
       Returns:
           Calculated fee (decimal number)
       """
       return amount * rate
   
   # Explanation:
   # - amount: int means the parameter should be an integer
   # - rate: float means the parameter should be a decimal number
   # - -> float means the function returns a decimal number
   # - Type hints help catch errors before running the code
   # - They make the code more self-documenting
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
