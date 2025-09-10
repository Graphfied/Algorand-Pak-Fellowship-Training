# Conditions Examples for Blockchain Development

# 1. Basic If Statements
print("=== Basic If Statements ===")

# Check if user has sufficient balance
wallet_balance = 1000
transaction_amount = 500

if wallet_balance >= transaction_amount:
    print("Transaction can proceed")
    print("Processing transaction...")
else:
    print("Insufficient funds")
    print("Transaction rejected")

print("\n" + "="*50 + "\n")

# 2. If-Else Statements
print("=== If-Else Statements ===")

# Check transaction validity
wallet_balance = 1000
transaction_amount = 1500

if wallet_balance >= transaction_amount:
    print("Transaction approved")
    print("Processing transaction...")
else:
    print("Insufficient funds")
    print("Transaction rejected")

print("\n" + "="*50 + "\n")

# 3. If-Elif-Else Statements
print("=== If-Elif-Else Statements ===")

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

print(f"Fee rate: {fee_rate}")

print("\n" + "="*50 + "\n")

# 4. Comparison Operators
print("=== Comparison Operators ===")

# Equality operators
user_address = "ABCD1234"
if user_address == "ABCD1234":
    print("Address matches")

# Not equal to
transaction_status = "pending"
if transaction_status != "confirmed":
    print("Transaction not confirmed yet")

# Numeric comparisons
wallet_balance = 1000
transaction_amount = 500

# Greater than
if wallet_balance > transaction_amount:
    print("Sufficient balance")

# Less than
if transaction_amount < 1000:
    print("Small transaction")

# Greater than or equal to
if wallet_balance >= transaction_amount:
    print("Can afford transaction")

# Less than or equal to
if transaction_amount <= 1000:
    print("Transaction within limits")

print("\n" + "="*50 + "\n")

# 5. Logical Operators
print("=== Logical Operators ===")

# AND operator
wallet_balance = 1000
user_verified = True
transaction_amount = 500

if wallet_balance >= transaction_amount and user_verified:
    print("Transaction approved")
else:
    print("Transaction rejected")

# OR operator
user_role = "admin"
is_owner = True

if user_role == "admin" or is_owner:
    print("Access granted")
else:
    print("Access denied")

# NOT operator
account_frozen = False

if not account_frozen:
    print("Account is active")
else:
    print("Account is frozen")

print("\n" + "="*50 + "\n")

# 6. Complex Conditions
print("=== Complex Conditions ===")

# Multiple conditions
wallet_balance = 1000
user_verified = True
transaction_amount = 500
is_business_hours = True
user_role = "admin"

if (wallet_balance >= transaction_amount and 
    user_verified and 
    (is_business_hours or user_role == "admin")):
    print("Transaction approved")
else:
    print("Transaction rejected")

print("\n" + "="*50 + "\n")

# 7. Nested Conditions
print("=== Nested Conditions ===")

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

print("\n" + "="*50 + "\n")

