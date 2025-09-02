# Functions in Python

Functions are reusable blocks of code that perform specific tasks. In blockchain development, functions are essential for creating modular, maintainable code that can be easily tested and reused.

## What are Functions?

Think of functions as **recipes** that take ingredients (inputs) and produce a dish (output):

```
Recipe: Make Sandwich
Ingredients: bread, meat, cheese
Instructions: Put meat and cheese between bread
Result: Sandwich
```

Functions work the same way:
- **Input**: Parameters (ingredients)
- **Process**: Code logic (instructions)
- **Output**: Return value (result)

## Basic Function Syntax

### Simple Function

```python
def greet_user():
    """Simple function that greets the user"""
    print("Hello, welcome to Algorand!")

# Call the function
greet_user()  # Output: Hello, welcome to Algorand!
```

### Function with Parameters

```python
def greet_user_by_name(name):
    """Function that greets a specific user"""
    print(f"Hello {name}, welcome to Algorand!")

# Call the function with a parameter
greet_user_by_name("Alice")  # Output: Hello Alice, welcome to Algorand!
```

### Function with Return Value

```python
def calculate_fee(amount, fee_rate=0.001):
    """Calculate transaction fee"""
    fee = amount * fee_rate
    return fee

# Call the function and use the result
transaction_amount = 1000
fee = calculate_fee(transaction_amount)
print(f"Fee: {fee}")  # Output: Fee: 1.0
```

## Function Parameters

### 1. **Positional Parameters**

```python
def transfer_tokens(sender, recipient, amount):
    """Transfer tokens between accounts"""
    print(f"Transferring {amount} tokens from {sender} to {recipient}")
    return True

# Call with positional arguments
result = transfer_tokens("Alice", "Bob", 100)
```

### 2. **Default Parameters**

```python
def create_transaction(amount, fee=1000, priority=False):
    """Create a transaction with optional parameters"""
    total_cost = amount + fee
    if priority:
        total_cost += 500  # Priority fee
    
    return {
        "amount": amount,
        "fee": fee,
        "priority": priority,
        "total_cost": total_cost
    }

# Call with default values
tx1 = create_transaction(1000)  # Uses default fee=1000, priority=False
tx2 = create_transaction(1000, 2000)  # Uses custom fee=2000, priority=False
tx3 = create_transaction(1000, 2000, True)  # Uses custom fee=2000, priority=True
```

### 3. **Keyword Arguments**

```python
def create_wallet(address, balance=0, status="active"):
    """Create a wallet with keyword arguments"""
    return {
        "address": address,
        "balance": balance,
        "status": status
    }

# Call with keyword arguments
wallet = create_wallet(
    address="ABCD1234567890EFGH",
    balance=1000,
    status="active"
)
```

### 4. **Variable Arguments (*args)**

```python
def calculate_total(*amounts):
    """Calculate total of multiple amounts"""
    total = sum(amounts)
    return total

# Call with multiple arguments
total1 = calculate_total(100, 200, 300)  # 600
total2 = calculate_total(50, 75, 100, 125)  # 350
```

### 5. **Keyword Arguments (**kwargs)**

```python
def create_transaction(**kwargs):
    """Create transaction with flexible parameters"""
    transaction = {
        "amount": kwargs.get("amount", 0),
        "fee": kwargs.get("fee", 1000),
        "sender": kwargs.get("sender", ""),
        "recipient": kwargs.get("recipient", ""),
        "timestamp": kwargs.get("timestamp", 0)
    }
    return transaction

# Call with keyword arguments
tx = create_transaction(
    amount=1000,
    sender="Alice",
    recipient="Bob",
    fee=500
)
```

## Blockchain-Specific Examples

### 1. **Wallet Management Functions**

```python
def create_wallet():
    """Create a new wallet"""
    import random
    import string
    
    # Generate random address (simplified)
    address = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))
    balance = 0
    status = "active"
    
    return {
        "address": address,
        "balance": balance,
        "status": status,
        "created_at": "2024-01-01"
    }

def get_balance(wallet_address, wallets):
    """Get balance for a specific wallet"""
    for wallet in wallets:
        if wallet["address"] == wallet_address:
            return wallet["balance"]
    return None

def update_balance(wallet_address, new_balance, wallets):
    """Update balance for a specific wallet"""
    for wallet in wallets:
        if wallet["address"] == wallet_address:
            wallet["balance"] = new_balance
            return True
    return False

# Example usage
wallets = []
wallet1 = create_wallet()
wallets.append(wallet1)

print(f"Wallet created: {wallet1['address']}")
print(f"Initial balance: {wallet1['balance']}")

# Update balance
update_balance(wallet1['address'], 1000, wallets)
print(f"Updated balance: {get_balance(wallet1['address'], wallets)}")
```

### 2. **Transaction Processing Functions**

```python
def validate_transaction(sender_balance, amount, recipient_address):
    """Validate transaction before processing"""
    # Check if sender has sufficient balance
    if sender_balance < amount:
        return False, "Insufficient balance"
    
    # Check if amount is positive
    if amount <= 0:
        return False, "Invalid amount"
    
    # Check if recipient address is valid
    if len(recipient_address) < 10:
        return False, "Invalid recipient address"
    
    return True, "Transaction valid"

def process_transaction(sender, recipient, amount, wallets):
    """Process a transaction between wallets"""
    # Get sender balance
    sender_balance = get_balance(sender, wallets)
    if sender_balance is None:
        return False, "Sender wallet not found"
    
    # Validate transaction
    is_valid, message = validate_transaction(sender_balance, amount, recipient)
    if not is_valid:
        return False, message
    
    # Process the transaction
    new_sender_balance = sender_balance - amount
    recipient_balance = get_balance(recipient, wallets) or 0
    new_recipient_balance = recipient_balance + amount
    
    # Update balances
    update_balance(sender, new_sender_balance, wallets)
    update_balance(recipient, new_recipient_balance, wallets)
    
    return True, "Transaction processed successfully"

# Example usage
wallets = [
    {"address": "ALICE1234567890", "balance": 1000, "status": "active"},
    {"address": "BOB0987654321", "balance": 500, "status": "active"}
]

success, message = process_transaction("ALICE1234567890", "BOB0987654321", 200, wallets)
if success:
    print("Transaction successful!")
    print(f"Alice's balance: {get_balance('ALICE1234567890', wallets)}")
    print(f"Bob's balance: {get_balance('BOB0987654321', wallets)}")
else:
    print(f"Transaction failed: {message}")
```

### 3. **Smart Contract Functions**

```python
def create_voting_contract(owner, max_votes=1000):
    """Create a new voting contract"""
    return {
        "owner": owner,
        "max_votes": max_votes,
        "total_votes": 0,
        "voting_active": True,
        "votes": {},
        "created_at": "2024-01-01"
    }

def cast_vote(contract, voter, choice):
    """Cast a vote in the voting contract"""
    # Check if voting is active
    if not contract["voting_active"]:
        return False, "Voting is not active"
    
    # Check if user has already voted
    if voter in contract["votes"]:
        return False, "User has already voted"
    
    # Check if choice is valid
    valid_choices = ["yes", "no", "abstain"]
    if choice not in valid_choices:
        return False, "Invalid vote choice"
    
    # Record the vote
    contract["votes"][voter] = choice
    contract["total_votes"] += 1
    
    return True, "Vote recorded successfully"

def get_voting_results(contract):
    """Get voting results"""
    if contract["total_votes"] == 0:
        return "No votes cast yet"
    
    yes_votes = sum(1 for choice in contract["votes"].values() if choice == "yes")
    no_votes = sum(1 for choice in contract["votes"].values() if choice == "no")
    abstain_votes = sum(1 for choice in contract["votes"].values() if choice == "abstain")
    
    return {
        "total_votes": contract["total_votes"],
        "yes": yes_votes,
        "no": no_votes,
        "abstain": abstain_votes
    }

# Example usage
contract = create_voting_contract("ADMIN1234567890", 1000)

# Cast votes
cast_vote(contract, "VOTER1", "yes")
cast_vote(contract, "VOTER2", "no")
cast_vote(contract, "VOTER3", "yes")

# Get results
results = get_voting_results(contract)
print(f"Voting results: {results}")
```

### 4. **Fee Calculation Functions**

```python
def calculate_transaction_fee(amount, user_type="standard", is_priority=False):
    """Calculate transaction fee based on amount and user type"""
    base_fee = 1000  # 0.001 ALGO
    
    # Calculate fee based on amount
    if amount < 100000:  # Less than 0.1 ALGO
        amount_fee = 0
    elif amount < 1000000:  # Less than 1 ALGO
        amount_fee = amount * 0.001  # 0.1%
    else:  # 1 ALGO or more
        amount_fee = amount * 0.002  # 0.2%
    
    # Apply user type discount
    if user_type == "premium":
        amount_fee *= 0.5  # 50% discount
    elif user_type == "standard":
        amount_fee *= 0.8  # 20% discount
    
    # Apply priority fee
    priority_fee = base_fee * 2 if is_priority else 0
    
    total_fee = base_fee + amount_fee + priority_fee
    return total_fee

def calculate_total_cost(amount, user_type="standard", is_priority=False):
    """Calculate total cost including amount and fee"""
    fee = calculate_transaction_fee(amount, user_type, is_priority)
    total_cost = amount + fee
    return total_cost, fee

# Example usage
amount = 500000  # 0.5 ALGO
user_type = "premium"
is_priority = True

total_cost, fee = calculate_total_cost(amount, user_type, is_priority)
print(f"Amount: {amount} microAlgos")
print(f"Fee: {fee} microAlgos")
print(f"Total cost: {total_cost} microAlgos")
```

## Function Documentation

### Docstrings

```python
def transfer_tokens(sender, recipient, amount, fee=1000):
    """
    Transfer tokens between two accounts.
    
    Args:
        sender (str): Address of the sender account
        recipient (str): Address of the recipient account
        amount (int): Amount of tokens to transfer (in microAlgos)
        fee (int, optional): Transaction fee. Defaults to 1000.
    
    Returns:
        tuple: (success: bool, message: str)
    
    Raises:
        ValueError: If amount is negative or zero
    
    Example:
        >>> success, message = transfer_tokens("Alice", "Bob", 1000)
        >>> print(message)
        "Transfer successful"
    """
    if amount <= 0:
        raise ValueError("Amount must be positive")
    
    # Transfer logic here
    return True, "Transfer successful"
```

## Error Handling in Functions

### Try-Except Blocks

```python
def safe_divide(a, b):
    """Safely divide two numbers"""
    try:
        result = a / b
        return result, "Success"
    except ZeroDivisionError:
        return None, "Cannot divide by zero"
    except TypeError:
        return None, "Invalid input types"
    except Exception as e:
        return None, f"Unexpected error: {e}"

# Example usage
result, message = safe_divide(10, 2)
if result is not None:
    print(f"Result: {result}")
else:
    print(f"Error: {message}")
```

### Custom Exceptions

```python
class InsufficientBalanceError(Exception):
    """Raised when account has insufficient balance"""
    pass

class InvalidAddressError(Exception):
    """Raised when address format is invalid"""
    pass

def transfer_with_validation(sender, recipient, amount):
    """Transfer with custom error handling"""
    if not is_valid_address(sender):
        raise InvalidAddressError("Invalid sender address")
    
    if not is_valid_address(recipient):
        raise InvalidAddressError("Invalid recipient address")
    
    if get_balance(sender) < amount:
        raise InsufficientBalanceError("Insufficient balance")
    
    # Process transfer
    return True
```

## Function Best Practices

### 1. **Single Responsibility**
```python
# Good: Each function has one purpose
def validate_address(address):
    """Validate address format"""
    return len(address) >= 10

def check_balance(address):
    """Check account balance"""
    return get_balance(address)

def process_transfer(sender, recipient, amount):
    """Process the transfer"""
    # Transfer logic
    pass

# Bad: Function does too many things
def do_everything(sender, recipient, amount):
    """Validate, check balance, and transfer"""
    # Too many responsibilities
    pass
```

### 2. **Use Descriptive Names**
```python
# Good: Clear function names
def calculate_transaction_fee(amount, user_type):
    pass

def validate_user_permissions(user, action):
    pass

# Bad: Unclear function names
def calc(amt, type):
    pass

def check(user, act):
    pass
```

### 3. **Keep Functions Small**
```python
# Good: Small, focused function
def is_valid_amount(amount):
    """Check if amount is valid"""
    return amount > 0 and amount <= 1000000

# Bad: Large, complex function
def process_everything(data):
    """Process all data"""
    # 100+ lines of code
    pass
```

### 4. **Use Type Hints (Optional)**
```python
def transfer_tokens(sender: str, recipient: str, amount: int, fee: int = 1000) -> tuple[bool, str]:
    """Transfer tokens with type hints"""
    # Function implementation
    return True, "Success"
```

## Common Mistakes

### 1. **Missing Return Statement**
```python
# Error: Function doesn't return anything
def calculate_fee(amount):
    fee = amount * 0.001
    # Missing return statement

# Fix: Add return statement
def calculate_fee(amount):
    fee = amount * 0.001
    return fee
```

### 2. **Modifying Mutable Default Arguments**
```python
# Error: Mutable default argument
def add_to_list(item, my_list=[]):
    my_list.append(item)
    return my_list

# Fix: Use None as default
def add_to_list(item, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list
```

### 3. **Not Handling Errors**
```python
# Error: No error handling
def divide(a, b):
    return a / b  # Will crash if b is 0

# Fix: Add error handling
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None
```

## Key Takeaways

- **Functions are reusable** code blocks that perform specific tasks
- **Use parameters** to make functions flexible and reusable
- **Return values** to provide results to the caller
- **Document functions** with docstrings for clarity
- **Handle errors** gracefully with try-except blocks
- **Keep functions small** and focused on one task
- **Use descriptive names** that explain what the function does
- **Functions are essential** for building modular blockchain applications

## Next Steps

Now that you understand functions, let's explore:
1. **Imports** - How to use code from other modules
2. **Examples** - Practical examples combining all concepts
3. **Algorand Python** - How Python works specifically on Algorand

Functions are the building blocks of your blockchain applications - master them and you'll be able to create powerful, reusable code!
