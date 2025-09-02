# ARC4 Types

ARC4 provides a comprehensive set of types for Algorand smart contracts. Understanding these types is essential for building type-safe and efficient smart contracts.

## ARC4 Type Categories

### 1. **Numeric Types**

#### UInt64
```python
from algopy import UInt64

# 64-bit unsigned integer (0 to 18,446,744,073,709,551,615)
amount: UInt64 = UInt64(1000)
balance: UInt64 = UInt64(0)
max_value: UInt64 = UInt64(18446744073709551615)

# Arithmetic operations
result: UInt64 = amount + UInt64(500)
result: UInt64 = amount - UInt64(200)
result: UInt64 = amount * UInt64(2)
result: UInt64 = amount / UInt64(2)

# Comparisons
if amount > UInt64(0):
    print("Positive amount")

if amount == UInt64(1000):
    print("Exact amount")
```

#### BigUInt
```python
from algopy import BigUInt

# Arbitrary precision unsigned integer
large_amount: BigUInt = BigUInt(1000000000000000000)
very_large: BigUInt = BigUInt(999999999999999999999999999)

# Operations
result: BigUInt = large_amount + BigUInt(1000)
result: BigUInt = large_amount * BigUInt(2)
```

### 2. **String Types**

#### String
```python
from algopy import String

# UTF-8 encoded string
name: String = String("Alice")
message: String = String("Hello, World!")
address: String = String("ABCD1234567890EFGH")

# String operations
length: UInt64 = len(name)
upper_name: String = name.upper()
lower_name: String = name.lower()

# String concatenation
full_name: String = name + String(" Smith")

# String comparison
if name == String("Alice"):
    print("Name matches")
```

#### Bytes
```python
from algopy import Bytes

# Raw bytes
data: Bytes = Bytes(b"hello")
hash_data: Bytes = Bytes(b"0x1234567890abcdef")

# Bytes operations
length: UInt64 = len(data)
hex_data: String = data.hex()
```

### 3. **Account Types**

#### Account
```python
from algopy import Account

# Algorand account
account: Account = Account("ABCD1234567890EFGH")
creator: Account = Account("CREATOR1234567890EFGH")

# Account properties
balance: UInt64 = account.balance
address: String = account.address
status: String = account.status

# Account operations
if account.balance > UInt64(1000):
    print("Account has sufficient balance")
```

#### Asset
```python
from algopy import Asset

# Algorand Standard Asset
asset: Asset = Asset(12345)
token: Asset = Asset(67890)

# Asset properties
asset_id: UInt64 = asset.id
total_supply: UInt64 = asset.total_supply
decimals: UInt64 = asset.decimals
name: String = asset.name
```

### 4. **Collection Types**

#### StaticArray
```python
from algopy import StaticArray

# Fixed size array
numbers: StaticArray[UInt64, 3] = StaticArray([UInt64(1), UInt64(2), UInt64(3)])
names: StaticArray[String, 2] = StaticArray([String("Alice"), String("Bob")])

# Access elements
first_number: UInt64 = numbers[0]
second_name: String = names[1]

# Array length
length: UInt64 = len(numbers)
```

#### DynamicArray
```python
from algopy import DynamicArray

# Variable size array
numbers: DynamicArray[UInt64] = DynamicArray([UInt64(1), UInt64(2)])
names: DynamicArray[String] = DynamicArray([String("Alice")])

# Add elements
numbers.append(UInt64(3))
names.append(String("Bob"))

# Access elements
first_number: UInt64 = numbers[0]
last_name: String = names[-1]

# Array length
length: UInt64 = len(numbers)
```

### 5. **Boolean Type**

#### bool
```python
from algopy import bool

# Boolean values
is_active: bool = True
is_frozen: bool = False

# Boolean operations
if is_active and not is_frozen:
    print("Account is active and not frozen")

# Boolean conversion
result: bool = UInt64(1000) > UInt64(500)
```

## ARC4 Type Table

| Type | Description | Range/Format | Example |
|------|-------------|--------------|---------|
| **UInt64** | 64-bit unsigned integer | 0 to 18,446,744,073,709,551,615 | `UInt64(1000)` |
| **BigUInt** | Arbitrary precision integer | Unlimited | `BigUInt(1000000000000000000)` |
| **String** | UTF-8 encoded string | Any valid UTF-8 | `String("Hello")` |
| **Bytes** | Raw bytes | Any byte sequence | `Bytes(b"hello")` |
| **Account** | Algorand account | Valid account address | `Account("ABCD1234...")` |
| **Asset** | Algorand Standard Asset | Valid asset ID | `Asset(12345)` |
| **StaticArray[T, N]** | Fixed size array | N elements of type T | `StaticArray[UInt64, 3]` |
| **DynamicArray[T]** | Variable size array | Variable elements of type T | `DynamicArray[String]` |
| **bool** | Boolean value | True or False | `True`, `False` |

## Type Conversion

### 1. **Explicit Conversion**

```python
from algopy import UInt64, String, Bytes

# UInt64 to String
amount: UInt64 = UInt64(1000)
amount_str: String = String(str(amount))

# String to UInt64
amount_str: String = String("1000")
amount: UInt64 = UInt64(int(amount_str))

# String to Bytes
text: String = String("hello")
data: Bytes = Bytes(text.encode())

# Bytes to String
data: Bytes = Bytes(b"hello")
text: String = String(data.decode())
```

### 2. **Safe Conversion**

```python
from algopy import UInt64, String

def safe_string_to_uint64(value: String) -> UInt64:
    # Check if string represents a valid number
    if value.isdigit():
        return UInt64(int(value))
    else:
        return UInt64(0)

def safe_uint64_to_string(value: UInt64) -> String:
    # Always safe to convert UInt64 to String
    return String(str(value))
```

## Type Validation

### 1. **Input Validation**

```python
from algopy import UInt64, String, Account

def validate_inputs(
    amount: UInt64,
    recipient: Account,
    message: String
) -> UInt64:
    # Validate amount
    if amount <= UInt64(0):
        return UInt64(0)
    
    # Validate recipient
    if recipient == Account(""):
        return UInt64(0)
    
    # Validate message length
    if len(message) > UInt64(100):
        return UInt64(0)
    
    return UInt64(1)
```

### 2. **Type Checking**

```python
from algopy import UInt64, String, Account

def check_types(
    amount: UInt64,
    name: String,
    account: Account
) -> UInt64:
    # Types are guaranteed by ARC4
    # No need for runtime type checking
    
    if amount > UInt64(0) and len(name) > UInt64(0):
        return UInt64(1)
    else:
        return UInt64(0)
```

## Common Patterns

### 1. **State Management**

```python
from algopy import UInt64, String, Global

def manage_global_state():
    # Store different types in global state
    Global.state[String("total_supply")] = UInt64(1000000)
    Global.state[String("name")] = String("MyToken")
    Global.state[String("decimals")] = UInt64(6)
    
    # Retrieve and use
    total_supply: UInt64 = Global.state[String("total_supply")]
    name: String = Global.state[String("name")]
    decimals: UInt64 = Global.state[String("decimals")]
    
    return total_supply
```

### 2. **Transaction Processing**

```python
from algopy import UInt64, String, Account, Txn

def process_transaction() -> UInt64:
    # Get transaction data with proper types
    amount: UInt64 = Txn.amount
    sender: Account = Txn.sender
    recipient: Account = Txn.receiver
    
    # Process with type safety
    if amount > UInt64(0) and sender != recipient:
        return UInt64(1)
    else:
        return UInt64(0)
```

### 3. **Asset Operations**

```python
from algopy import UInt64, Asset, Account

def transfer_asset(
    asset: Asset,
    sender: Account,
    recipient: Account,
    amount: UInt64
) -> UInt64:
    # Type-safe asset transfer
    if sender.asset_balance(asset) >= amount:
        # Transfer logic here
        return UInt64(1)  # Success
    else:
        return UInt64(0)  # Insufficient balance
```

### 4. **Array Operations**

```python
from algopy import UInt64, StaticArray, DynamicArray

def array_operations():
    # Static array
    numbers: StaticArray[UInt64, 3] = StaticArray([UInt64(1), UInt64(2), UInt64(3)])
    
    # Dynamic array
    dynamic_numbers: DynamicArray[UInt64] = DynamicArray([UInt64(1), UInt64(2)])
    dynamic_numbers.append(UInt64(3))
    
    # Process arrays
    total: UInt64 = UInt64(0)
    for i in range(len(dynamic_numbers)):
        total += dynamic_numbers[i]
    
    return total
```

## Type Safety Examples

### 1. **Preventing Type Errors**

```python
from algopy import UInt64, String, Account

def safe_operations(
    amount: UInt64,
    name: String,
    account: Account
) -> UInt64:
    # All operations are type-safe
    
    # Safe arithmetic
    double_amount: UInt64 = amount * UInt64(2)
    
    # Safe string operations
    upper_name: String = name.upper()
    
    # Safe account operations
    balance: UInt64 = account.balance
    
    return double_amount
```

### 2. **Type Validation**

```python
from algopy import UInt64, String, Account

def validate_transaction(
    sender: Account,
    recipient: Account,
    amount: UInt64,
    message: String
) -> UInt64:
    # Validate all inputs
    if sender == Account(""):
        return UInt64(0)  # Invalid sender
    
    if recipient == Account(""):
        return UInt64(0)  # Invalid recipient
    
    if amount <= UInt64(0):
        return UInt64(0)  # Invalid amount
    
    if len(message) > UInt64(100):
        return UInt64(0)  # Message too long
    
    return UInt64(1)  # Valid
```

## Best Practices

### 1. **Always Use ARC4 Types**

```python
# Good: Use ARC4 types
from algopy import UInt64, String, Account

def good_function(amount: UInt64, name: String, account: Account) -> UInt64:
    return amount

# Bad: Don't use regular Python types
def bad_function(amount, name, account):
    return amount
```

### 2. **Explicit Type Declarations**

```python
# Good: Explicit types
from algopy import UInt64, String

def explicit_types(amount: UInt64, name: String) -> UInt64:
    return amount

# Bad: Implicit types
def implicit_types(amount, name):
    return amount
```

### 3. **Type Validation**

```python
# Good: Validate types
from algopy import UInt64, String

def validate_types(amount: UInt64, name: String) -> UInt64:
    if amount > UInt64(0) and len(name) > UInt64(0):
        return amount
    else:
        return UInt64(0)
```

## Key Takeaways

- **ARC4 types** provide type safety for smart contracts
- **Numeric types** include UInt64 and BigUInt
- **String types** include String and Bytes
- **Account types** include Account and Asset
- **Collection types** include StaticArray and DynamicArray
- **Type conversion** must be explicit and safe
- **Type validation** ensures data integrity
- **Best practices** include explicit types and validation

## Next Steps

Now that you understand ARC4 types, let's explore:
1. **Examples** - Practical examples using ARC4 types
2. **Session Recap** - Summary of everything learned

Understanding ARC4 types is essential for building type-safe and reliable smart contracts!
