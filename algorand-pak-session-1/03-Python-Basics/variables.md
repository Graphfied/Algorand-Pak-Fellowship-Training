# Variables in Python

Variables are containers that store data values. In blockchain development, variables are essential for managing wallet balances, transaction counters, and other important data.

## What are Variables?

Think of variables as **labeled boxes** that hold information:

```
┌─────────────┐
│ wallet_balance │  ← Variable name (label)
├─────────────┤
│    1000     │  ← Value stored inside
└─────────────┘
```

## Basic Variable Types

### 1. **Numbers**

#### Integers (Whole Numbers)
```python
# Wallet balance in microAlgos
wallet_balance = 1000000  # 1 ALGO = 1,000,000 microAlgos

# Transaction counter
transaction_count = 5

# Block number
current_block = 12345

# User ID
user_id = 42
```

#### Floats (Decimal Numbers)
```python
# Transaction fee rate
fee_rate = 0.001  # 0.1%

# Exchange rate
algo_to_usd = 0.85

# Percentage
success_rate = 99.9
```

### 2. **Strings (Text)**

```python
# Wallet address
wallet_address = "ABCD1234567890EFGH"

# Transaction hash
tx_hash = "0x1234567890abcdef"

# User name
username = "alice"

# Contract name
contract_name = "VotingContract"

# Error message
error_msg = "Insufficient balance"
```

### 3. **Booleans (True/False)**

```python
# Transaction status
is_confirmed = True
is_pending = False

# Account status
account_active = True
account_frozen = False

# Validation results
is_valid_address = True
is_valid_amount = False
```

### 4. **Lists (Collections)**

```python
# Transaction history
transaction_history = [100, 200, 150, 300, 250]

# User addresses
user_addresses = [
    "ABCD1234567890EFGH",
    "IJKL0987654321MNOP",
    "QRST1357924680UVWX"
]

# Contract functions
contract_functions = ["deposit", "withdraw", "transfer", "balance"]

# Block numbers
recent_blocks = [12340, 12341, 12342, 12343, 12344]
```

### 5. **Dictionaries (Key-Value Pairs)**

```python
# Account information
account_info = {
    "address": "ABCD1234567890EFGH",
    "balance": 1000000,
    "status": "active",
    "created_at": "2024-01-01"
}

# Transaction details
transaction_details = {
    "from": "ABCD1234567890EFGH",
    "to": "IJKL0987654321MNOP",
    "amount": 500000,
    "fee": 1000,
    "timestamp": 1640995200
}

# Contract configuration
contract_config = {
    "name": "VotingContract",
    "version": "1.0",
    "owner": "ABCD1234567890EFGH",
    "max_votes": 1000
}
```

## Variable Naming Rules

### ✅ **Good Variable Names**
```python
# Descriptive and clear
wallet_balance = 1000
transaction_count = 5
user_address = "ABCD1234..."
is_transaction_valid = True
contract_functions = ["deposit", "withdraw"]

# Use underscores for multiple words
current_block_number = 12345
total_transaction_fee = 1000
is_account_active = True
```

### ❌ **Bad Variable Names**
```python
# Too short or unclear
wb = 1000  # What is wb?
tc = 5     # What is tc?
x = "ABCD" # What does x represent?

# No spaces or special characters
wallet balance = 1000  # Error: spaces not allowed
user-address = "ABCD"  # Error: hyphens not allowed
user@address = "ABCD"  # Error: @ not allowed
```

## Variable Operations

### 1. **Arithmetic Operations**

```python
# Basic math
wallet_balance = 1000
transaction_amount = 100
fee = 1

# Addition
new_balance = wallet_balance + transaction_amount  # 1100

# Subtraction
remaining_balance = wallet_balance - transaction_amount - fee  # 899

# Multiplication
total_fee = transaction_amount * 0.01  # 1.0 (1% fee)

# Division
average_transaction = wallet_balance / 10  # 100.0

# Modulo (remainder)
remainder = wallet_balance % 3  # 1 (1000 ÷ 3 = 333 remainder 1)
```

### 2. **String Operations**

```python
# String concatenation
first_name = "Alice"
last_name = "Smith"
full_name = first_name + " " + last_name  # "Alice Smith"

# String formatting
wallet_address = "ABCD1234"
balance = 1000
message = f"Wallet {wallet_address} has {balance} ALGO"  # "Wallet ABCD1234 has 1000 ALGO"

# String methods
address = "ABCD1234567890EFGH"
address_lower = address.lower()  # "abcd1234567890efgh"
address_upper = address.upper()  # "ABCD1234567890EFGH"
address_length = len(address)    # 18
```

### 3. **List Operations**

```python
# Create list
transactions = [100, 200, 150]

# Add to list
transactions.append(300)  # [100, 200, 150, 300]

# Remove from list
transactions.remove(200)  # [100, 150, 300]

# Access elements
first_transaction = transactions[0]   # 100
last_transaction = transactions[-1]   # 300

# List length
transaction_count = len(transactions)  # 3

# List slicing
recent_transactions = transactions[-2:]  # [150, 300]
```

### 4. **Dictionary Operations**

```python
# Create dictionary
account = {
    "address": "ABCD1234",
    "balance": 1000,
    "status": "active"
}

# Access values
address = account["address"]    # "ABCD1234"
balance = account["balance"]    # 1000

# Update values
account["balance"] = 1500
account["last_transaction"] = "2024-01-01"

# Add new keys
account["transaction_count"] = 5

# Check if key exists
if "status" in account:
    print("Account has status")
```

## Blockchain-Specific Examples

### 1. **Wallet Management**

```python
# Wallet information
wallet_address = "ABCD1234567890EFGH"
wallet_balance = 1000000  # 1 ALGO in microAlgos
wallet_status = "active"
wallet_created = "2024-01-01"

# Transaction history
transaction_history = [
    {"amount": 100000, "to": "IJKL0987654321MNOP", "timestamp": 1640995200},
    {"amount": 200000, "to": "QRST1357924680UVWX", "timestamp": 1640995300},
    {"amount": 50000, "to": "YZAB2468135790CDEF", "timestamp": 1640995400}
]

# Calculate total sent
total_sent = sum(tx["amount"] for tx in transaction_history)  # 350000
```

### 2. **Smart Contract State**

```python
# Global state variables
contract_name = "VotingContract"
total_votes = 0
voting_active = True
contract_owner = "ABCD1234567890EFGH"

# Local state (per user)
user_has_voted = False
user_vote_choice = None
user_balance = 1000

# Contract configuration
max_votes = 1000
voting_duration = 86400  # 24 hours in seconds
minimum_stake = 100000   # 0.1 ALGO
```

### 3. **Transaction Processing**

```python
# Transaction data
transaction = {
    "id": "tx_123456789",
    "from": "ABCD1234567890EFGH",
    "to": "IJKL0987654321MNOP",
    "amount": 500000,
    "fee": 1000,
    "timestamp": 1640995200,
    "status": "pending"
}

# Process transaction
def process_transaction(tx):
    # Check if sender has sufficient balance
    sender_balance = get_balance(tx["from"])
    required_amount = tx["amount"] + tx["fee"]
    
    if sender_balance >= required_amount:
        # Update balances
        update_balance(tx["from"], sender_balance - required_amount)
        update_balance(tx["to"], get_balance(tx["to"]) + tx["amount"])
        
        # Update transaction status
        tx["status"] = "confirmed"
        return True
    else:
        tx["status"] = "failed"
        return False
```

## Variable Scope

### Local Variables
```python
def calculate_fee(amount):
    fee_rate = 0.01  # Local variable
    fee = amount * fee_rate
    return fee

# fee_rate is only available inside the function
```

### Global Variables
```python
# Global variable
CONTRACT_OWNER = "ABCD1234567890EFGH"

def check_owner(address):
    return address == CONTRACT_OWNER  # Can access global variable
```

## Constants

```python
# Constants (usually in UPPER_CASE)
ALGO_TO_MICROALGO = 1000000
MAX_TRANSACTION_SIZE = 1000
DEFAULT_FEE = 1000
CONTRACT_VERSION = "1.0"

# Use constants instead of magic numbers
def convert_to_microalgo(algo_amount):
    return algo_amount * ALGO_TO_MICROALGO
```

## Best Practices

### 1. **Use Descriptive Names**
```python
# Good
wallet_balance = 1000
transaction_count = 5
is_account_active = True

# Bad
wb = 1000
tc = 5
active = True
```

### 2. **Use Constants for Fixed Values**
```python
# Good
ALGO_TO_MICROALGO = 1000000
DEFAULT_FEE = 1000

# Bad
amount = 1000 * 1000000  # Magic numbers
```

### 3. **Initialize Variables**
```python
# Good
wallet_balance = 0
transaction_count = 0
user_address = ""

# Bad
# wallet_balance  # Undefined variable
```

### 4. **Use Type Hints (Optional)**
```python
# Good (Python 3.6+)
wallet_balance: int = 1000
user_address: str = "ABCD1234"
is_active: bool = True
```

## Common Mistakes

### 1. **Using Undefined Variables**
```python
# Error: wallet_balance not defined
print(wallet_balance)  # NameError

# Fix: Define the variable first
wallet_balance = 1000
print(wallet_balance)  # Works
```

### 2. **Wrong Variable Names**
```python
# Error: Typo in variable name
wallet_balance = 1000
print(wallet_balnce)  # NameError (missing 'a')

# Fix: Use correct variable name
print(wallet_balance)  # Works
```

### 3. **Modifying Immutable Types**
```python
# Error: Strings are immutable
address = "ABCD1234"
address[0] = "X"  # TypeError

# Fix: Create new string
address = "X" + address[1:]  # "XBCD1234"
```

## Key Takeaways

- **Variables store data** and have names and values
- **Use descriptive names** that explain what the variable contains
- **Different types** serve different purposes (numbers, strings, booleans, lists, dictionaries)
- **Follow naming conventions** (use underscores, avoid spaces)
- **Initialize variables** before using them
- **Use constants** for fixed values
- **Variables are essential** for managing blockchain data

## Next Steps

Now that you understand variables, let's explore:
1. **Conditions** - How to make decisions in your code
2. **Functions** - How to create reusable code blocks
3. **Imports** - How to use code from other modules

Variables are the foundation of programming - master them and you'll be ready for more advanced concepts!
