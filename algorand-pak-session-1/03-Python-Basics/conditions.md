# Conditions in Python

Conditions allow your code to make decisions and execute different code paths based on whether something is true or false. In blockchain development, conditions are crucial for validating transactions, checking permissions, and implementing business logic.

## What are Conditions?

Conditions are **decision points** in your code that check if something is true or false:

```
If condition is True:
    Do this
Else:
    Do that
```

Think of conditions like **traffic lights**:
- **Green light** (True) → Go
- **Red light** (False) → Stop

## Basic If Statements

### Simple If Statement

```python
# Check if user has sufficient balance
wallet_balance = 1000
transaction_amount = 500

if wallet_balance >= transaction_amount:
    print("Transaction can proceed")
    # Execute transaction logic here
```

### If-Else Statement

```python
# Check transaction validity
wallet_balance = 1000
transaction_amount = 1500

if wallet_balance >= transaction_amount:
    print("Transaction approved")
    # Process transaction
else:
    print("Insufficient funds")
    # Reject transaction
```

### If-Elif-Else Statement

```python
# Check account status
account_balance = 1000

if account_balance > 10000:
    print("Premium account")
    fee_rate = 0.001  # 0.1% fee
elif account_balance > 1000:
    print("Standard account")
    fee_rate = 0.002  # 0.2% fee
else:
    print("Basic account")
    fee_rate = 0.005  # 0.5% fee
```

## Comparison Operators

### 1. **Equality Operators**

```python
# Equal to (==)
user_address = "ABCD1234"
if user_address == "ABCD1234":
    print("Address matches")

# Not equal to (!=)
transaction_status = "pending"
if transaction_status != "confirmed":
    print("Transaction not confirmed yet")
```

### 2. **Numeric Comparisons**

```python
wallet_balance = 1000
transaction_amount = 500

# Greater than (>)
if wallet_balance > transaction_amount:
    print("Sufficient balance")

# Less than (<)
if transaction_amount < 1000:
    print("Small transaction")

# Greater than or equal to (>=)
if wallet_balance >= transaction_amount:
    print("Can afford transaction")

# Less than or equal to (<=)
if transaction_amount <= 1000:
    print("Transaction within limits")
```

### 3. **String Comparisons**

```python
# String equality
user_role = "admin"
if user_role == "admin":
    print("Admin access granted")

# String length
password = "mypassword"
if len(password) >= 8:
    print("Password is long enough")
else:
    print("Password too short")
```

## Logical Operators

### 1. **AND Operator (and)**

```python
# Both conditions must be true
wallet_balance = 1000
user_verified = True
transaction_amount = 500

if wallet_balance >= transaction_amount and user_verified:
    print("Transaction approved")
else:
    print("Transaction rejected")
```

### 2. **OR Operator (or)**

```python
# At least one condition must be true
user_role = "admin"
is_owner = True

if user_role == "admin" or is_owner:
    print("Access granted")
else:
    print("Access denied")
```

### 3. **NOT Operator (not)**

```python
# Inverts the condition
account_frozen = False

if not account_frozen:
    print("Account is active")
else:
    print("Account is frozen")
```

## Complex Conditions

### Multiple Conditions

```python
# Complex validation
wallet_balance = 1000
user_verified = True
transaction_amount = 500
is_business_hours = True

if (wallet_balance >= transaction_amount and 
    user_verified and 
    (is_business_hours or user_role == "admin")):
    print("Transaction approved")
else:
    print("Transaction rejected")
```

### Nested Conditions

```python
# Nested if statements
user_type = "premium"
transaction_amount = 5000

if user_type == "premium":
    if transaction_amount > 10000:
        print("Large transaction - requires approval")
    else:
        print("Premium transaction approved")
else:
    if transaction_amount > 1000:
        print("Standard transaction - requires verification")
    else:
        print("Standard transaction approved")
```


## Conditional Expressions (Ternary Operator)

### Simple Conditional

```python
# Traditional if-else
wallet_balance = 1000
if wallet_balance > 0:
    status = "active"
else:
    status = "empty"

# Conditional expression (shorter)
status = "active" if wallet_balance > 0 else "empty"
```

### Complex Conditional

```python
# Fee calculation with conditional
amount = 500000
user_type = "premium"

fee = (amount * 0.001 if user_type == "standard" 
       else amount * 0.0005 if user_type == "premium" 
       else amount * 0.002)
```

## Membership Testing

### Check if Item is in List

```python
# Check if user is in whitelist
whitelist = ["ABCD1234", "IJKL0987", "QRST1357"]
user_address = "ABCD1234"

if user_address in whitelist:
    print("User is whitelisted")
else:
    print("User is not whitelisted")
```

### Check if Key is in Dictionary

```python
# Check if user has specific permission
user_permissions = {
    "ABCD1234": ["deposit", "withdraw"],
    "IJKL0987": ["deposit"]
}

user_address = "ABCD1234"
permission = "withdraw"

if user_address in user_permissions:
    if permission in user_permissions[user_address]:
        print("Permission granted")
    else:
        print("Permission denied")
else:
    print("User not found")
```

## Error Handling with Conditions

```python
def safe_divide(a, b):
    """
    Safely divide two numbers
    """
    if b == 0:
        return None, "Cannot divide by zero"
    elif not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return None, "Invalid input types"
    else:
        result = a / b
        return result, "Success"

# Example usage
result, message = safe_divide(10, 2)
if result is not None:
    print(f"Result: {result}")
else:
    print(f"Error: {message}")
```

## Best Practices

### 1. **Use Clear Conditions**
```python
# Good: Clear and readable
if wallet_balance >= transaction_amount:
    process_transaction()

# Bad: Unclear
if not (wallet_balance < transaction_amount):
    process_transaction()
```

### 2. **Handle Edge Cases**
```python
# Good: Handle all cases
if amount > 0:
    process_positive_amount()
elif amount < 0:
    process_negative_amount()
else:  # amount == 0
    process_zero_amount()
```

### 3. **Use Meaningful Variable Names**
```python
# Good: Descriptive names
if user_has_sufficient_balance and user_is_verified:
    approve_transaction()

# Bad: Unclear names
if x and y:
    do_something()
```

### 4. **Avoid Deep Nesting**
```python
# Good: Early returns
def process_user(user):
    if not user.is_verified:
        return "User not verified"
    
    if not user.has_balance:
        return "Insufficient balance"
    
    if not user.is_active:
        return "Account inactive"
    
    return "User processed successfully"

# Bad: Deep nesting
def process_user(user):
    if user.is_verified:
        if user.has_balance:
            if user.is_active:
                return "User processed successfully"
            else:
                return "Account inactive"
        else:
            return "Insufficient balance"
    else:
        return "User not verified"
```

## Common Mistakes

### 1. **Using = Instead of ==**
```python
# Error: Assignment instead of comparison
if wallet_balance = 1000:  # SyntaxError
    print("Balance is 1000")

# Fix: Use == for comparison
if wallet_balance == 1000:
    print("Balance is 1000")
```

### 2. **Missing Colon**
```python
# Error: Missing colon
if wallet_balance > 0  # SyntaxError
    print("Positive balance")

# Fix: Add colon
if wallet_balance > 0:
    print("Positive balance")
```

### 3. **Incorrect Indentation**
```python
# Error: Wrong indentation
if wallet_balance > 0:
print("Positive balance")  # IndentationError

# Fix: Correct indentation
if wallet_balance > 0:
    print("Positive balance")
```

## Key Takeaways

- **Conditions make decisions** in your code
- **Use comparison operators** (==, !=, >, <, >=, <=) to compare values
- **Use logical operators** (and, or, not) to combine conditions
- **Handle all cases** including edge cases
- **Use clear and readable** condition statements
- **Conditions are essential** for blockchain validation and business logic

## Next Steps

Now that you understand conditions, let's explore:
1. **Functions** - How to create reusable code blocks
2. **Imports** - How to use code from other modules
3. **Examples** - Practical examples combining variables and conditions

Conditions are the decision-making power of your code - master them and you'll be able to build intelligent blockchain applications!
