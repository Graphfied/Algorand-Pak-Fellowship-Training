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

# 8. Blockchain-Specific Examples
print("=== Blockchain-Specific Examples ===")

# Transaction validation function
def validate_transaction(sender_balance, amount, recipient_address, sender_address):
    """
    Validate a transaction before processing
    """
    # Check if sender has sufficient balance
    if sender_balance < amount:
        return False, "Insufficient balance"
    
    # Check if amount is positive
    if amount <= 0:
        return False, "Invalid amount"
    
    # Check if recipient address is valid
    if len(recipient_address) < 10:
        return False, "Invalid recipient address"
    
    # Check if sender and recipient are different
    if sender_address == recipient_address:
        return False, "Cannot send to yourself"
    
    # Check if amount is within limits
    if amount > 1000000:  # 1 ALGO limit
        return False, "Amount exceeds limit"
    
    return True, "Transaction valid"

# Example usage
sender_balance = 1000
amount = 500
recipient = "ABCD1234567890EFGH"
sender = "IJKL0987654321MNOP"

is_valid, message = validate_transaction(sender_balance, amount, recipient, sender)
if is_valid:
    print("Processing transaction...")
else:
    print(f"Transaction rejected: {message}")

print("\n" + "="*50 + "\n")

# 9. Smart Contract Access Control
print("=== Smart Contract Access Control ===")

def check_contract_access(user_address, function_name, contract_owner):
    """
    Check if user can access contract function
    """
    # Owner can access all functions
    if user_address == contract_owner:
        return True, "Owner access granted"
    
    # Check function-specific permissions
    if function_name == "deposit":
        return True, "Deposit allowed for all users"
    elif function_name == "withdraw":
        return False, "Withdrawal requires owner permission"
    elif function_name == "admin":
        return False, "Admin functions require owner permission"
    else:
        return False, "Unknown function"

# Example usage
user_address = "ABCD1234567890EFGH"
function_name = "deposit"
contract_owner = "ADMIN1234567890EFGH"

has_access, message = check_contract_access(user_address, function_name, contract_owner)
print(f"Access check: {message}")

print("\n" + "="*50 + "\n")

# 10. Voting System Logic
print("=== Voting System Logic ===")

def process_vote(voter_address, vote_choice, voting_active, has_voted):
    """
    Process a vote in the voting system
    """
    # Check if voting is active
    if not voting_active:
        return False, "Voting is not active"
    
    # Check if user has already voted
    if has_voted:
        return False, "User has already voted"
    
    # Check if vote choice is valid
    valid_choices = ["yes", "no", "abstain"]
    if vote_choice not in valid_choices:
        return False, "Invalid vote choice"
    
    # Process the vote
    return True, f"Vote for {vote_choice} recorded"

# Example usage
voter = "ABCD1234567890EFGH"
choice = "yes"
voting_active = True
has_voted = False

success, message = process_vote(voter, choice, voting_active, has_voted)
if success:
    print("Vote recorded successfully")
else:
    print(f"Vote failed: {message}")

print("\n" + "="*50 + "\n")

# 11. Fee Calculation
print("=== Fee Calculation ===")

def calculate_transaction_fee(amount, user_type, is_priority):
    """
    Calculate transaction fee based on various factors
    """
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
    if is_priority:
        priority_fee = base_fee * 2  # Double base fee
    else:
        priority_fee = 0
    
    total_fee = base_fee + amount_fee + priority_fee
    return total_fee

# Example usage
amount = 500000  # 0.5 ALGO
user_type = "premium"
is_priority = True

fee = calculate_transaction_fee(amount, user_type, is_priority)
print(f"Transaction fee: {fee} microAlgos")

print("\n" + "="*50 + "\n")

# 12. Conditional Expressions (Ternary Operator)
print("=== Conditional Expressions ===")

# Traditional if-else
wallet_balance = 1000
if wallet_balance > 0:
    status = "active"
else:
    status = "empty"

print(f"Status (traditional): {status}")

# Conditional expression (shorter)
status = "active" if wallet_balance > 0 else "empty"
print(f"Status (conditional): {status}")

# Complex conditional
amount = 500000
user_type = "premium"

fee = (amount * 0.001 if user_type == "standard" 
       else amount * 0.0005 if user_type == "premium" 
       else amount * 0.002)

print(f"Fee: {fee} microAlgos")

print("\n" + "="*50 + "\n")

# 13. Membership Testing
print("=== Membership Testing ===")

# Check if user is in whitelist
whitelist = ["ABCD1234", "IJKL0987", "QRST1357"]
user_address = "ABCD1234"

if user_address in whitelist:
    print("User is whitelisted")
else:
    print("User is not whitelisted")

# Check if key is in dictionary
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

print("\n" + "="*50 + "\n")

# 14. Error Handling with Conditions
print("=== Error Handling with Conditions ===")

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

result, message = safe_divide(10, 0)
if result is not None:
    print(f"Result: {result}")
else:
    print(f"Error: {message}")

print("\n" + "="*50 + "\n")

print("Conditions examples completed successfully!")
