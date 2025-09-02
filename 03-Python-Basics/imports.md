# Imports in Python

Imports allow you to use code from other modules, libraries, and packages. In blockchain development, imports are essential for accessing Algorand's Python SDK, PyTeal, and other blockchain-specific libraries.

## What are Imports?

Think of imports as **borrowing tools** from a toolbox:

```
Your Code: "I need a hammer"
Toolbox: "Here's a hammer from the tools module"
Your Code: "Thanks! Now I can build something"
```

Imports work the same way:
- **Your code** needs functionality
- **Import statement** gets the code from another module
- **Your code** can now use that functionality

## Basic Import Syntax

### 1. **Import Entire Module**

```python
# Import the entire math module
import math

# Use functions from the module
result = math.sqrt(16)  # 4.0
pi_value = math.pi      # 3.14159...
```

### 2. **Import Specific Functions**

```python
# Import only the functions you need
from math import sqrt, pi

# Use functions directly (no module name needed)
result = sqrt(16)  # 4.0
pi_value = pi      # 3.14159...
```

### 3. **Import with Alias**

```python
# Import with a shorter name
import math as m

# Use with the alias
result = m.sqrt(16)  # 4.0
pi_value = m.pi      # 3.14159...
```

### 4. **Import Everything (Not Recommended)**

```python
# Import all functions (use with caution)
from math import *

# Use functions directly
result = sqrt(16)  # 4.0
pi_value = pi      # 3.14159...
```

## Algorand-Specific Imports

### 1. **Algorand Python SDK**

```python
# Import Algorand SDK
from algosdk import account, mnemonic
from algosdk.v2client import algod
from algosdk.future.transaction import PaymentTxn

# Create a new account
private_key, address = account.generate_account()
print(f"New address: {address}")

# Connect to Algorand network
algod_client = algod.AlgodClient(
    algod_token="",
    algod_address="https://testnet-api.algonode.cloud"
)

# Get account information
account_info = algod_client.account_info(address)
print(f"Balance: {account_info['amount']} microAlgos")
```

### 2. **PyTeal (Smart Contracts)**

```python
# Import PyTeal for smart contract development
from pyteal import *

# Create a simple smart contract
def approval_program():
    return Return(Int(1))

def clear_state_program():
    return Return(Int(1))

# Compile the contract
if __name__ == "__main__":
    print(compileTeal(approval_program(), Mode.Application))
```

### 3. **Algorand Python (Puya)**

```python
# Import Algorand Python (Puya) - Modern smart contracts
from algopy import UInt64, Account, Asset, Global, Txn, gtxn

# Example Puya smart contract
def approval_program() -> UInt64:
    # Check if transaction is valid
    if Txn.sender == Global.creator_address:
        return UInt64(1)  # Approve
    else:
        return UInt64(0)  # Reject
```

## Common Python Standard Library Imports

### 1. **Math Operations**

```python
import math

# Mathematical functions
result = math.sqrt(25)        # 5.0
result = math.pow(2, 3)       # 8.0
result = math.ceil(4.2)       # 5
result = math.floor(4.8)      # 4
result = math.abs(-5)         # 5
```

### 2. **Random Numbers**

```python
import random

# Generate random numbers
random_int = random.randint(1, 100)      # Random integer between 1 and 100
random_float = random.random()           # Random float between 0 and 1
random_choice = random.choice([1, 2, 3]) # Random choice from list
```

### 3. **Date and Time**

```python
import datetime

# Get current time
now = datetime.datetime.now()
print(f"Current time: {now}")

# Format time
formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"Formatted time: {formatted_time}")

# Calculate time differences
future_time = now + datetime.timedelta(days=30)
print(f"30 days from now: {future_time}")
```

### 4. **JSON Handling**

```python
import json

# Convert Python object to JSON
data = {
    "address": "ABCD1234567890EFGH",
    "balance": 1000,
    "status": "active"
}

json_string = json.dumps(data)
print(f"JSON: {json_string}")

# Convert JSON to Python object
parsed_data = json.loads(json_string)
print(f"Parsed: {parsed_data}")
```

### 5. **File Operations**

```python
import os

# Check if file exists
if os.path.exists("config.txt"):
    print("Config file exists")
else:
    print("Config file not found")

# Get current directory
current_dir = os.getcwd()
print(f"Current directory: {current_dir}")

# List files in directory
files = os.listdir(".")
print(f"Files: {files}")
```

## Blockchain Development Imports

### 1. **Complete Algorand Setup**

```python
# Standard library imports
import json
import time
from datetime import datetime

# Algorand SDK imports
from algosdk import account, mnemonic, encoding
from algosdk.v2client import algod, indexer
from algosdk.future.transaction import (
    PaymentTxn, 
    AssetTransferTxn, 
    ApplicationCreateTxn,
    ApplicationCallTxn
)

# PyTeal imports
from pyteal import *

# Example: Complete blockchain interaction
def setup_algorand_client():
    """Setup Algorand client for testnet"""
    algod_token = ""
    algod_address = "https://testnet-api.algonode.cloud"
    
    client = algod.AlgodClient(algod_token, algod_address)
    return client

def create_and_fund_account():
    """Create a new account and get testnet funds"""
    # Generate new account
    private_key, address = account.generate_account()
    
    # Connect to client
    client = setup_algorand_client()
    
    # Get account info
    account_info = client.account_info(address)
    balance = account_info['amount']
    
    return private_key, address, balance
```

### 2. **Smart Contract Development**

```python
# PyTeal imports
from pyteal import *

# Algorand Python imports
from algopy import UInt64, Account, Asset, Global, Txn, gtxn

# Example: Voting contract
def voting_contract():
    """Create a voting smart contract"""
    
    # Global state
    total_votes = App.globalGet(Bytes("total_votes"))
    voting_active = App.globalGet(Bytes("voting_active"))
    
    # Local state
    has_voted = App.localGet(Int(0), Bytes("has_voted"))
    
    # Voting logic
    on_vote = Seq([
        Assert(voting_active == Int(1)),  # Voting must be active
        Assert(has_voted == Int(0)),      # User must not have voted
        
        # Record vote
        App.localPut(Int(0), Bytes("has_voted"), Int(1)),
        App.globalPut(Bytes("total_votes"), total_votes + Int(1)),
        
        Return(Int(1))
    ])
    
    return Cond(
        [Txn.application_id() == Int(0), on_creation()],
        [Txn.on_completion() == OnComplete.NoOp, on_vote]
    )

def on_creation():
    """Initialize the voting contract"""
    return Seq([
        App.globalPut(Bytes("total_votes"), Int(0)),
        App.globalPut(Bytes("voting_active"), Int(1)),
        Return(Int(1))
    ])
```

### 3. **Testing and Development**

```python
# Testing imports
import pytest
import unittest
from unittest.mock import Mock, patch

# Development tools
import logging
import os
from pathlib import Path

# Example: Test setup
def setup_test_environment():
    """Setup testing environment"""
    # Configure logging
    logging.basicConfig(level=logging.INFO)
    
    # Set test environment variables
    os.environ['ALGORAND_NETWORK'] = 'testnet'
    os.environ['ALGORAND_API_TOKEN'] = ''
    
    # Create test directory
    test_dir = Path("tests")
    test_dir.mkdir(exist_ok=True)
    
    return test_dir
```

## Import Best Practices

### 1. **Import Order**
```python
# Standard library imports
import os
import sys
import json
from datetime import datetime

# Third-party imports
import requests
import numpy as np

# Local imports
from my_module import my_function
from utils.helpers import helper_function
```

### 2. **Specific Imports**
```python
# Good: Import only what you need
from algosdk import account, mnemonic
from pyteal import Return, Int

# Bad: Import everything
from algosdk import *
from pyteal import *
```

### 3. **Use Aliases for Long Names**
```python
# Good: Use aliases for long module names
import algosdk.future.transaction as txn
import algosdk.v2client.algod as algod_client

# Use with aliases
payment = txn.PaymentTxn(...)
client = algod_client.AlgodClient(...)
```

### 4. **Conditional Imports**
```python
# Import based on environment
try:
    from algopy import UInt64, Account
    HAS_ALGOPY = True
except ImportError:
    HAS_ALGOPY = False
    print("Algorand Python not available, using PyTeal")

# Use conditional logic
if HAS_ALGOPY:
    # Use Algorand Python
    pass
else:
    # Use PyTeal
    pass
```

## Common Import Errors

### 1. **Module Not Found**
```python
# Error: Module not installed
import non_existent_module  # ModuleNotFoundError

# Fix: Install the module
# pip install module_name
```

### 2. **Import Error**
```python
# Error: Function doesn't exist in module
from math import non_existent_function  # ImportError

# Fix: Check module documentation
from math import sqrt  # Correct function name
```

### 3. **Circular Imports**
```python
# Error: Circular import
# file1.py imports file2.py
# file2.py imports file1.py

# Fix: Restructure code to avoid circular dependencies
```

## Virtual Environment and Imports

### 1. **Create Virtual Environment**
```bash
# Create virtual environment
python -m venv algorand-env

# Activate virtual environment
# Windows:
algorand-env\Scripts\activate

# macOS/Linux:
source algorand-env/bin/activate
```

### 2. **Install Required Packages**
```bash
# Install Algorand packages
pip install py-algorand-sdk
pip install pyteal
pip install algorand-python

# Install development tools
pip install pytest
pip install black
pip install flake8
```

### 3. **Create Requirements File**
```bash
# Generate requirements.txt
pip freeze > requirements.txt

# Install from requirements.txt
pip install -r requirements.txt
```

## Key Takeaways

- **Imports allow you** to use code from other modules and libraries
- **Use specific imports** to avoid namespace pollution
- **Import order matters** - standard library, third-party, local
- **Algorand has specific** imports for blockchain development
- **Virtual environments** help manage dependencies
- **Handle import errors** gracefully with try-except blocks
- **Imports are essential** for building complex blockchain applications

## Next Steps

Now that you understand imports, let's explore:
1. **Examples** - Practical examples combining all Python concepts
2. **Algorand Python** - How Python works specifically on Algorand
3. **ARC4** - Algorand's type system

Imports are the gateway to powerful functionality - master them and you'll be able to build sophisticated blockchain applications!
