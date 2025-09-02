# Variables Examples for Blockchain Development

# 1. Basic Variable Types
print("=== Basic Variable Types ===")

# Numbers
wallet_balance = 1000000  # 1 ALGO in microAlgos
transaction_count = 5
block_number = 12345
fee_rate = 0.001  # 0.1%

print(f"Wallet balance: {wallet_balance} microAlgos")
print(f"Transaction count: {transaction_count}")
print(f"Block number: {block_number}")
print(f"Fee rate: {fee_rate}")

# Strings
wallet_address = "ABCD1234567890EFGH"
tx_hash = "0x1234567890abcdef"
username = "alice"
contract_name = "VotingContract"

print(f"Wallet address: {wallet_address}")
print(f"Transaction hash: {tx_hash}")
print(f"Username: {username}")
print(f"Contract name: {contract_name}")

# Booleans
is_confirmed = True
is_pending = False
account_active = True

print(f"Transaction confirmed: {is_confirmed}")
print(f"Transaction pending: {is_pending}")
print(f"Account active: {account_active}")

# Lists
transaction_history = [100, 200, 150, 300, 250]
user_addresses = [
    "ABCD1234567890EFGH",
    "IJKL0987654321MNOP",
    "QRST1357924680UVWX"
]

print(f"Transaction history: {transaction_history}")
print(f"User addresses: {user_addresses}")

# Dictionaries
account_info = {
    "address": "ABCD1234567890EFGH",
    "balance": 1000000,
    "status": "active",
    "created_at": "2024-01-01"
}

transaction_details = {
    "from": "ABCD1234567890EFGH",
    "to": "IJKL0987654321MNOP",
    "amount": 500000,
    "fee": 1000,
    "timestamp": 1640995200
}

print(f"Account info: {account_info}")
print(f"Transaction details: {transaction_details}")

print("\n" + "="*50 + "\n")

# 2. Variable Operations
print("=== Variable Operations ===")

# Arithmetic operations
wallet_balance = 1000
transaction_amount = 100
fee = 1

# Addition
new_balance = wallet_balance + transaction_amount
print(f"New balance after deposit: {new_balance}")

# Subtraction
remaining_balance = wallet_balance - transaction_amount - fee
print(f"Remaining balance after transaction: {remaining_balance}")

# Multiplication
total_fee = transaction_amount * 0.01
print(f"Total fee (1%): {total_fee}")

# Division
average_transaction = wallet_balance / 10
print(f"Average transaction: {average_transaction}")

# Modulo (remainder)
remainder = wallet_balance % 3
print(f"Remainder when dividing by 3: {remainder}")

print("\n" + "="*50 + "\n")

# 3. String Operations
print("=== String Operations ===")

# String concatenation
first_name = "Alice"
last_name = "Smith"
full_name = first_name + " " + last_name
print(f"Full name: {full_name}")

# String formatting
wallet_address = "ABCD1234"
balance = 1000
message = f"Wallet {wallet_address} has {balance} ALGO"
print(f"Message: {message}")

# String methods
address = "ABCD1234567890EFGH"
print(f"Original address: {address}")
print(f"Lowercase: {address.lower()}")
print(f"Uppercase: {address.upper()}")
print(f"Length: {len(address)}")

print("\n" + "="*50 + "\n")

# 4. List Operations
print("=== List Operations ===")

# Create list
transactions = [100, 200, 150]
print(f"Initial transactions: {transactions}")

# Add to list
transactions.append(300)
print(f"After adding 300: {transactions}")

# Remove from list
transactions.remove(200)
print(f"After removing 200: {transactions}")

# Access elements
first_transaction = transactions[0]
last_transaction = transactions[-1]
print(f"First transaction: {first_transaction}")
print(f"Last transaction: {last_transaction}")

# List length
transaction_count = len(transactions)
print(f"Transaction count: {transaction_count}")

# List slicing
recent_transactions = transactions[-2:]
print(f"Recent transactions: {recent_transactions}")

print("\n" + "="*50 + "\n")

# 5. Dictionary Operations
print("=== Dictionary Operations ===")

# Create dictionary
account = {
    "address": "ABCD1234",
    "balance": 1000,
    "status": "active"
}
print(f"Initial account: {account}")

# Access values
address = account["address"]
balance = account["balance"]
print(f"Address: {address}")
print(f"Balance: {balance}")

# Update values
account["balance"] = 1500
account["last_transaction"] = "2024-01-01"
print(f"Updated account: {account}")

# Add new keys
account["transaction_count"] = 5
print(f"Account with transaction count: {account}")

# Check if key exists
if "status" in account:
    print(f"Account status: {account['status']}")

print("\n" + "="*50 + "\n")

# 6. Blockchain-Specific Examples
print("=== Blockchain-Specific Examples ===")

# Wallet management
wallet_address = "ABCD1234567890EFGH"
wallet_balance = 1000000  # 1 ALGO in microAlgos
wallet_status = "active"
wallet_created = "2024-01-01"

print(f"Wallet Address: {wallet_address}")
print(f"Wallet Balance: {wallet_balance} microAlgos")
print(f"Wallet Status: {wallet_status}")
print(f"Wallet Created: {wallet_created}")

# Transaction history
transaction_history = [
    {"amount": 100000, "to": "IJKL0987654321MNOP", "timestamp": 1640995200},
    {"amount": 200000, "to": "QRST1357924680UVWX", "timestamp": 1640995300},
    {"amount": 50000, "to": "YZAB2468135790CDEF", "timestamp": 1640995400}
]

print(f"Transaction History: {transaction_history}")

# Calculate total sent
total_sent = sum(tx["amount"] for tx in transaction_history)
print(f"Total sent: {total_sent} microAlgos")

# Smart contract state
contract_name = "VotingContract"
total_votes = 0
voting_active = True
contract_owner = "ABCD1234567890EFGH"

print(f"Contract Name: {contract_name}")
print(f"Total Votes: {total_votes}")
print(f"Voting Active: {voting_active}")
print(f"Contract Owner: {contract_owner}")

# Local state (per user)
user_has_voted = False
user_vote_choice = None
user_balance = 1000

print(f"User Has Voted: {user_has_voted}")
print(f"User Vote Choice: {user_vote_choice}")
print(f"User Balance: {user_balance}")

# Contract configuration
max_votes = 1000
voting_duration = 86400  # 24 hours in seconds
minimum_stake = 100000   # 0.1 ALGO

print(f"Max Votes: {max_votes}")
print(f"Voting Duration: {voting_duration} seconds")
print(f"Minimum Stake: {minimum_stake} microAlgos")

print("\n" + "="*50 + "\n")

# 7. Constants
print("=== Constants ===")

# Constants (usually in UPPER_CASE)
ALGO_TO_MICROALGO = 1000000
MAX_TRANSACTION_SIZE = 1000
DEFAULT_FEE = 1000
CONTRACT_VERSION = "1.0"

print(f"ALGO to MicroALGO: {ALGO_TO_MICROALGO}")
print(f"Max Transaction Size: {MAX_TRANSACTION_SIZE}")
print(f"Default Fee: {DEFAULT_FEE}")
print(f"Contract Version: {CONTRACT_VERSION}")

# Use constants instead of magic numbers
def convert_to_microalgo(algo_amount):
    return algo_amount * ALGO_TO_MICROALGO

algo_amount = 1.5
microalgo_amount = convert_to_microalgo(algo_amount)
print(f"{algo_amount} ALGO = {microalgo_amount} microAlgos")

print("\n" + "="*50 + "\n")

# 8. Type Hints (Optional)
print("=== Type Hints ===")

# Type hints for better code documentation
wallet_balance: int = 1000
user_address: str = "ABCD1234"
is_active: bool = True

print(f"Wallet Balance (int): {wallet_balance}")
print(f"User Address (str): {user_address}")
print(f"Is Active (bool): {is_active}")

print("\n" + "="*50 + "\n")

print("Variables examples completed successfully!")
