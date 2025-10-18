# Smart Contracts I

## Table of Contents
1. [Introduction to Algorand Virtual Machine](#introduction-to-algorand-virtual-machine)
2. [Smart Contracts in Python](#smart-contracts-in-python)
3. [Stateless vs Stateful Contracts](#stateless-vs-stateful-contracts)
4. [Approval Program Logic](#approval-program-logic)
5. [Global State vs Local State](#global-state-vs-local-state)
6. [Writing Basic Approval Logic](#writing-basic-approval-logic)
7. [Practical Examples](#practical-examples)
8. [Best Practices](#best-practices)

## Introduction to Algorand Virtual Machine

### What is the AVM?

The Algorand Virtual Machine (AVM) is the **execution environment** for smart contracts on the Algorand blockchain. It provides:

- **Deterministic execution** of smart contract code
- **Sandboxed environment** for security
- **High performance** with low latency
- **Support for multiple** programming languages

### Key Features of AVM

#### 1. **Performance**
- **Fast execution** (typically < 1 second)
- **Low transaction fees** (0.001 ALGO minimum)
- **High throughput** (1000+ TPS)
- **Predictable costs** for operations

#### 2. **Security**
- **Sandboxed execution** environment
- **No external dependencies** or network calls
- **Deterministic behavior** across all nodes
- **Formal verification** support

#### 3. **Flexibility**
- **Multiple languages** (Python, TypeScript, Go)
- **Rich instruction set** for complex logic
- **State management** capabilities
- **Cross-contract** communication

### AVM Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    AVM Execution Layer                  │
├─────────────────────────────────────────────────────────┤
│  Application Logic  │  State Management  │  Validation  │
│  (Approval Program) │  (Global/Local)    │  (Clear Prog)│
├─────────────────────────────────────────────────────────┤
│                    Algorand Protocol                    │
│  (Consensus, Transactions, Block Production)           │
└─────────────────────────────────────────────────────────┘
```

### Execution Model

#### 1. **Transaction Processing**
- **Transaction arrives** at the network
- **AVM validates** the transaction
- **Approval program** executes if valid
- **State updates** are applied
- **Transaction is confirmed**

#### 2. **State Management**
- **Global state**: Shared across all users
- **Local state**: Per-user application state
- **Box storage**: Key-value storage for contracts
- **Scratch space**: Temporary storage during execution

#### 3. **Error Handling**
- **Validation failures** reject transactions
- **Logic errors** cause transaction failure
- **Resource limits** prevent infinite loops
- **Clear program** handles cleanup

## Smart Contracts in Python

### Introduction to PyTeal

PyTeal is the **Python framework** for writing Algorand smart contracts. It provides:

- **Python syntax** for contract development
- **Type safety** and validation
- **Rich library** of built-in functions
- **Easy testing** and debugging

### PyTeal vs Raw TEAL

#### PyTeal Advantages
- **Readable code** with Python syntax
- **Type checking** and validation
- **Reusable components** and functions
- **Better debugging** capabilities

#### Raw TEAL Advantages
- **Direct control** over bytecode
- **Smaller contract** size
- **Maximum performance** optimization
- **Full AVM** feature access

### Basic PyTeal Structure

```python
from pyteal import *

def approval_program():
    """Main approval program logic"""
    
    # Contract logic goes here
    return Approve()

def clear_program():
    """Clear program for cleanup"""
    
    return Approve()

# Compile the programs
if __name__ == "__main__":
    approval_teal = compileTeal(approval_program(), mode=Mode.Application)
    clear_teal = compileTeal(clear_program(), mode=Mode.Application)
    
    print("Approval Program:")
    print(approval_teal)
    print("\nClear Program:")
    print(clear_teal)
```

### PyTeal Data Types

#### 1. **Basic Types**
- **Int**: 64-bit signed integers
- **Bytes**: Byte strings (up to 64KB)
- **Bool**: Boolean values (True/False)
- **Expr**: Expression objects

#### 2. **Composite Types**
- **Seq**: Sequence of expressions
- **Cond**: Conditional expressions
- **For**: Loop expressions
- **While**: While loop expressions

#### 3. **State Types**
- **GlobalState**: Global application state
- **LocalState**: Local user state
- **Box**: Key-value storage

### PyTeal Operators

#### Arithmetic Operators
```python
# Addition
result = a + b

# Subtraction
result = a - b

# Multiplication
result = a * b

# Division
result = a / b

# Modulo
result = a % b
```

#### Comparison Operators
```python
# Equality
is_equal = a == b

# Inequality
not_equal = a != b

# Greater than
greater = a > b

# Less than
less = a < b

# Greater than or equal
greater_equal = a >= b

# Less than or equal
less_equal = a <= b
```

#### Logical Operators
```python
# Logical AND
and_result = a & b

# Logical OR
or_result = a | b

# Logical NOT
not_result = ~a

# Conditional
if_then_else = If(condition).Then(true_expr).Else(false_expr)
```

## Stateless vs Stateful Contracts

### Stateless Contracts

#### Definition
Stateless contracts **don't maintain state** between transactions. Each transaction is processed independently.

#### Characteristics
- **No persistent storage**
- **Faster execution**
- **Lower costs**
- **Simpler logic**

#### Use Cases
- **Signature verification**
- **Multi-signature wallets**
- **Escrow services**
- **Atomic swaps**

#### Example: Multi-signature Wallet
```python
def multisig_wallet():
    """Stateless multi-signature wallet"""
    
    # Check if transaction is signed by required number of signers
    required_signatures = Int(2)  # Require 2 signatures
    actual_signatures = Txn.sender()
    
    # Verify signatures (simplified)
    return Approve()
```

### Stateful Contracts

#### Definition
Stateful contracts **maintain state** between transactions. They can store and retrieve data.

#### Characteristics
- **Persistent storage**
- **Complex logic**
- **Higher costs**
- **Rich functionality**

#### Use Cases
- **Token contracts**
- **Governance systems**
- **Marketplaces**
- **Gaming applications**

#### Example: Simple Counter
```python
def counter_contract():
    """Stateful counter contract"""
    
    # Get current counter value
    current_count = App.globalGet(Bytes("count"))
    
    # Increment counter
    new_count = current_count + Int(1)
    
    # Store new value
    return Seq([
        App.globalPut(Bytes("count"), new_count),
        Approve()
    ])
```

### Choosing Between Stateless and Stateful

#### Use Stateless When:
- **Simple validation** is needed
- **No data storage** required
- **Maximum performance** is critical
- **Cost optimization** is important

#### Use Stateful When:
- **Data persistence** is needed
- **Complex business logic** required
- **User interactions** need tracking
- **Rich functionality** is desired

## Approval Program Logic

### What is an Approval Program?

An approval program is the **main logic** of a smart contract that:
- **Validates transactions** before execution
- **Implements business rules** and constraints
- **Manages state changes**
- **Handles different** transaction types

### Approval Program Structure

```python
def approval_program():
    """Main approval program"""
    
    # Handle different transaction types
    return Cond(
        [Txn.application_id() == Int(0), handle_creation()],
        [Txn.on_completion() == OnComplete.OptIn, handle_opt_in()],
        [Txn.on_completion() == OnComplete.CloseOut, handle_close_out()],
        [Txn.on_completion() == OnComplete.UpdateApplication, handle_update()],
        [Txn.on_completion() == OnComplete.DeleteApplication, handle_delete()],
        [Txn.on_completion() == OnComplete.NoOp, handle_no_op()]
    )
```

### Transaction Type Handlers

#### 1. **Application Creation**
```python
def handle_creation():
    """Handle application creation"""
    
    return Seq([
        # Initialize global state
        App.globalPut(Bytes("creator"), Txn.sender()),
        App.globalPut(Bytes("total_supply"), Int(1000000)),
        App.globalPut(Bytes("decimals"), Int(6)),
        
        # Approve creation
        Approve()
    ])
```

#### 2. **Opt-in Handling**
```python
def handle_opt_in():
    """Handle user opt-in"""
    
    return Seq([
        # Initialize local state for user
        App.localPut(Txn.sender(), Bytes("balance"), Int(0)),
        App.localPut(Txn.sender(), Bytes("opted_in"), Int(1)),
        
        # Approve opt-in
        Approve()
    ])
```

#### 3. **No-Op Handling**
```python
def handle_no_op():
    """Handle regular transactions"""
    
    # Get transaction arguments
    method = Txn.application_args[0]
    
    return Cond(
        [method == Bytes("transfer"), handle_transfer()],
        [method == Bytes("mint"), handle_mint()],
        [method == Bytes("burn"), handle_burn()],
        [method == Bytes("get_balance"), handle_get_balance()]
    )
```

### Common Approval Patterns

#### 1. **Authorization Checks**
```python
def check_authorization():
    """Check if sender is authorized"""
    
    # Check if sender is the creator
    is_creator = Txn.sender() == App.globalGet(Bytes("creator"))
    
    # Check if sender is opted in
    is_opted_in = App.localGet(Txn.sender(), Bytes("opted_in")) == Int(1)
    
    return And(is_creator, is_opted_in)
```

#### 2. **Balance Validation**
```python
def check_sufficient_balance(amount):
    """Check if account has sufficient balance"""
    
    current_balance = App.localGet(Txn.sender(), Bytes("balance"))
    return current_balance >= amount
```

#### 3. **Supply Validation**
```python
def check_supply_limit(amount):
    """Check if minting exceeds supply limit"""
    
    current_supply = App.globalGet(Bytes("total_supply"))
    return amount <= current_supply
```

## Global State vs Local State

### Global State

#### Definition
Global state is **shared across all users** of the application. It's accessible by all transactions.

#### Characteristics
- **Shared data** across all users
- **Limited storage** (64 key-value pairs)
- **Higher cost** for operations
- **Global visibility**

#### Use Cases
- **Total supply** of tokens
- **Application settings**
- **Global counters**
- **System parameters**

#### Global State Operations
```python
# Set global state
App.globalPut(Bytes("key"), Int(100))

# Get global state
value = App.globalGet(Bytes("key"))

# Delete global state
App.globalDel(Bytes("key"))

# Check if key exists
exists = App.globalGet(Bytes("key")) != Int(0)
```

#### Example: Token Contract Global State
```python
def initialize_global_state():
    """Initialize global state for token contract"""
    
    return Seq([
        # Token information
        App.globalPut(Bytes("name"), Bytes("My Token")),
        App.globalPut(Bytes("symbol"), Bytes("MTK")),
        App.globalPut(Bytes("decimals"), Int(6)),
        App.globalPut(Bytes("total_supply"), Int(1000000)),
        
        # Contract state
        App.globalPut(Bytes("creator"), Txn.sender()),
        App.globalPut(Bytes("paused"), Int(0)),
        App.globalPut(Bytes("mintable"), Int(1))
    ])
```

### Local State

#### Definition
Local state is **per-user data** that each user maintains independently. It's only accessible by that user.

#### Characteristics
- **User-specific data**
- **Limited storage** (16 key-value pairs per user)
- **Lower cost** for operations
- **Private to user**

#### Use Cases
- **User balances**
- **User preferences**
- **User-specific counters**
- **Personal data**

#### Local State Operations
```python
# Set local state
App.localPut(Txn.sender(), Bytes("key"), Int(100))

# Get local state
value = App.localGet(Txn.sender(), Bytes("key"))

# Delete local state
App.localDel(Txn.sender(), Bytes("key"))

# Check if key exists
exists = App.localGet(Txn.sender(), Bytes("key")) != Int(0)
```

#### Example: User Balance Management
```python
def initialize_user_state():
    """Initialize local state for new user"""
    
    return Seq([
        # User balance
        App.localPut(Txn.sender(), Bytes("balance"), Int(0)),
        
        # User status
        App.localPut(Txn.sender(), Bytes("opted_in"), Int(1)),
        App.localPut(Txn.sender(), Bytes("frozen"), Int(0)),
        
        # User preferences
        App.localPut(Txn.sender(), Bytes("notifications"), Int(1))
    ])
```

### State Management Best Practices

#### 1. **Key Naming**
```python
# Use descriptive, consistent names
BALANCE_KEY = Bytes("balance")
CREATOR_KEY = Bytes("creator")
TOTAL_SUPPLY_KEY = Bytes("total_supply")
```

#### 2. **State Validation**
```python
def validate_state_change():
    """Validate state changes before applying"""
    
    # Check if user is opted in
    is_opted_in = App.localGet(Txn.sender(), Bytes("opted_in")) == Int(1)
    
    # Check if contract is not paused
    is_not_paused = App.globalGet(Bytes("paused")) == Int(0)
    
    return And(is_opted_in, is_not_paused)
```

#### 3. **State Cleanup**
```python
def cleanup_user_state():
    """Clean up user state on opt-out"""
    
    return Seq([
        # Delete all local state
        App.localDel(Txn.sender(), Bytes("balance")),
        App.localDel(Txn.sender(), Bytes("opted_in")),
        App.localDel(Txn.sender(), Bytes("frozen")),
        
        # Approve cleanup
        Approve()
    ])
```

## Writing Basic Approval Logic

### Example 1: Simple Counter Contract

```python
from pyteal import *

def counter_contract():
    """Simple counter contract"""
    
    # Handle different transaction types
    return Cond(
        [Txn.application_id() == Int(0), handle_creation()],
        [Txn.on_completion() == OnComplete.OptIn, handle_opt_in()],
        [Txn.on_completion() == OnComplete.CloseOut, handle_close_out()],
        [Txn.on_completion() == OnComplete.NoOp, handle_no_op()]
    )

def handle_creation():
    """Handle contract creation"""
    
    return Seq([
        # Initialize global state
        App.globalPut(Bytes("count"), Int(0)),
        App.globalPut(Bytes("creator"), Txn.sender()),
        
        # Approve creation
        Approve()
    ])

def handle_opt_in():
    """Handle user opt-in"""
    
    return Seq([
        # Initialize user state
        App.localPut(Txn.sender(), Bytes("user_count"), Int(0)),
        
        # Approve opt-in
        Approve()
    ])

def handle_close_out():
    """Handle user opt-out"""
    
    return Seq([
        # Clean up user state
        App.localDel(Txn.sender(), Bytes("user_count")),
        
        # Approve opt-out
        Approve()
    ])

def handle_no_op():
    """Handle regular transactions"""
    
    # Get method from transaction arguments
    method = Txn.application_args[0]
    
    return Cond(
        [method == Bytes("increment"), handle_increment()],
        [method == Bytes("decrement"), handle_decrement()],
        [method == Bytes("reset"), handle_reset()],
        [method == Bytes("get_count"), handle_get_count()]
    )

def handle_increment():
    """Increment the counter"""
    
    return Seq([
        # Get current count
        current_count = App.globalGet(Bytes("count")),
        
        # Increment count
        new_count = current_count + Int(1),
        
        # Update global state
        App.globalPut(Bytes("count"), new_count),
        
        # Update user's local count
        user_count = App.localGet(Txn.sender(), Bytes("user_count")),
        App.localPut(Txn.sender(), Bytes("user_count"), user_count + Int(1)),
        
        # Approve transaction
        Approve()
    ])

def handle_decrement():
    """Decrement the counter"""
    
    return Seq([
        # Get current count
        current_count = App.globalGet(Bytes("count")),
        
        # Check if count > 0
        Assert(current_count > Int(0)),
        
        # Decrement count
        new_count = current_count - Int(1),
        
        # Update global state
        App.globalPut(Bytes("count"), new_count),
        
        # Update user's local count
        user_count = App.localGet(Txn.sender(), Bytes("user_count")),
        App.localPut(Txn.sender(), Bytes("user_count"), user_count + Int(1)),
        
        # Approve transaction
        Approve()
    ])

def handle_reset():
    """Reset the counter (only creator)"""
    
    return Seq([
        # Check if sender is creator
        Assert(Txn.sender() == App.globalGet(Bytes("creator"))),
        
        # Reset global count
        App.globalPut(Bytes("count"), Int(0)),
        
        # Approve transaction
        Approve()
    ])

def handle_get_count():
    """Get current count (read-only)"""
    
    return Seq([
        # Get current count
        current_count = App.globalGet(Bytes("count")),
        
        # Log the count
        Log(Bytes("Current count: "), current_count),
        
        # Approve transaction
        Approve()
    ])

# Compile the contract
if __name__ == "__main__":
    approval_teal = compileTeal(counter_contract(), mode=Mode.Application)
    print("Counter Contract Approval Program:")
    print(approval_teal)
```

### Example 2: Minimum Payment Rule

```python
def minimum_payment_rule():
    """Contract that enforces minimum payment"""
    
    MINIMUM_PAYMENT = Int(1000000)  # 1 ALGO in microALGOs
    
    return Seq([
        # Check if this is a payment transaction
        Assert(Txn.type_enum() == TxnType.Payment),
        
        # Check if payment amount meets minimum
        Assert(Txn.amount() >= MINIMUM_PAYMENT),
        
        # Approve transaction
        Approve()
    ])
```

### Example 3: Multi-signature Logic

```python
def multisig_logic():
    """Multi-signature transaction logic"""
    
    # Define required signers
    SIGNER_1 = Bytes("SIGNER_1_ADDRESS")
    SIGNER_2 = Bytes("SIGNER_2_ADDRESS")
    SIGNER_3 = Bytes("SIGNER_3_ADDRESS")
    
    # Check if sender is one of the required signers
    is_signer_1 = Txn.sender() == SIGNER_1
    is_signer_2 = Txn.sender() == SIGNER_2
    is_signer_3 = Txn.sender() == SIGNER_3
    
    # At least one signer must be present
    has_valid_signer = Or(is_signer_1, is_signer_2, is_signer_3)
    
    return Seq([
        # Check for valid signer
        Assert(has_valid_signer),
        
        # Additional validation logic can go here
        # (e.g., check transaction amount, destination, etc.)
        
        # Approve transaction
        Approve()
    ])
```

## Practical Examples

### Example 1: Simple Token Contract

```python
def simple_token_contract():
    """Simple token contract with basic functionality"""
    
    return Cond(
        [Txn.application_id() == Int(0), handle_creation()],
        [Txn.on_completion() == OnComplete.OptIn, handle_opt_in()],
        [Txn.on_completion() == OnComplete.CloseOut, handle_close_out()],
        [Txn.on_completion() == OnComplete.NoOp, handle_no_op()]
    )

def handle_creation():
    """Initialize token contract"""
    
    return Seq([
        # Set token parameters
        App.globalPut(Bytes("name"), Bytes("Simple Token")),
        App.globalPut(Bytes("symbol"), Bytes("STK")),
        App.globalPut(Bytes("decimals"), Int(6)),
        App.globalPut(Bytes("total_supply"), Int(1000000)),
        App.globalPut(Bytes("creator"), Txn.sender()),
        
        # Initialize supply tracking
        App.globalPut(Bytes("current_supply"), Int(0)),
        
        # Approve creation
        Approve()
    ])

def handle_opt_in():
    """Handle user opt-in to token"""
    
    return Seq([
        # Initialize user balance
        App.localPut(Txn.sender(), Bytes("balance"), Int(0)),
        App.localPut(Txn.sender(), Bytes("opted_in"), Int(1)),
        
        # Approve opt-in
        Approve()
    ])

def handle_close_out():
    """Handle user opt-out from token"""
    
    return Seq([
        # Check if user has zero balance
        user_balance = App.localGet(Txn.sender(), Bytes("balance")),
        Assert(user_balance == Int(0)),
        
        # Clean up user state
        App.localDel(Txn.sender(), Bytes("balance")),
        App.localDel(Txn.sender(), Bytes("opted_in")),
        
        # Approve opt-out
        Approve()
    ])

def handle_no_op():
    """Handle token operations"""
    
    method = Txn.application_args[0]
    
    return Cond(
        [method == Bytes("mint"), handle_mint()],
        [method == Bytes("transfer"), handle_transfer()],
        [method == Bytes("get_balance"), handle_get_balance()]
    )

def handle_mint():
    """Mint new tokens"""
    
    # Get mint amount from transaction arguments
    mint_amount = Btoi(Txn.application_args[1])
    
    return Seq([
        # Check if sender is creator
        Assert(Txn.sender() == App.globalGet(Bytes("creator"))),
        
        # Check if minting exceeds total supply
        current_supply = App.globalGet(Bytes("current_supply")),
        total_supply = App.globalGet(Bytes("total_supply")),
        Assert(current_supply + mint_amount <= total_supply),
        
        # Update supply
        App.globalPut(Bytes("current_supply"), current_supply + mint_amount),
        
        # Add to creator's balance
        creator_balance = App.localGet(Txn.sender(), Bytes("balance")),
        App.localPut(Txn.sender(), Bytes("balance"), creator_balance + mint_amount),
        
        # Approve minting
        Approve()
    ])

def handle_transfer():
    """Transfer tokens between users"""
    
    # Get transfer parameters
    receiver = Txn.accounts[1]  # First account in accounts array
    amount = Btoi(Txn.application_args[1])
    
    return Seq([
        # Check if sender has sufficient balance
        sender_balance = App.localGet(Txn.sender(), Bytes("balance")),
        Assert(sender_balance >= amount),
        
        # Check if receiver is opted in
        receiver_opted_in = App.localGet(receiver, Bytes("opted_in")) == Int(1),
        Assert(receiver_opted_in),
        
        # Update balances
        App.localPut(Txn.sender(), Bytes("balance"), sender_balance - amount),
        receiver_balance = App.localGet(receiver, Bytes("balance")),
        App.localPut(receiver, Bytes("balance"), receiver_balance + amount),
        
        # Approve transfer
        Approve()
    ])

def handle_get_balance():
    """Get user balance"""
    
    return Seq([
        # Get user balance
        user_balance = App.localGet(Txn.sender(), Bytes("balance")),
        
        # Log balance
        Log(Bytes("User balance: "), user_balance),
        
        # Approve transaction
        Approve()
    ])
```

### Example 2: Escrow Contract

```python
def escrow_contract():
    """Simple escrow contract"""
    
    return Cond(
        [Txn.application_id() == Int(0), handle_creation()],
        [Txn.on_completion() == OnComplete.OptIn, handle_opt_in()],
        [Txn.on_completion() == OnComplete.NoOp, handle_no_op()]
    )

def handle_creation():
    """Initialize escrow contract"""
    
    return Seq([
        # Set escrow parameters
        App.globalPut(Bytes("buyer"), Txn.accounts[0]),
        App.globalPut(Bytes("seller"), Txn.accounts[1]),
        App.globalPut(Bytes("arbitrator"), Txn.accounts[2]),
        App.globalPut(Bytes("amount"), Int(1000000)),  # 1 ALGO
        App.globalPut(Bytes("status"), Bytes("pending")),
        
        # Approve creation
        Approve()
    ])

def handle_opt_in():
    """Handle user opt-in"""
    
    return Seq([
        # Initialize user state
        App.localPut(Txn.sender(), Bytes("role"), Bytes("unknown")),
        App.localPut(Txn.sender(), Bytes("voted"), Int(0)),
        
        # Approve opt-in
        Approve()
    ])

def handle_no_op():
    """Handle escrow operations"""
    
    method = Txn.application_args[0]
    
    return Cond(
        [method == Bytes("deposit"), handle_deposit()],
        [method == Bytes("release"), handle_release()],
        [method == Bytes("dispute"), handle_dispute()],
        [method == Bytes("resolve"), handle_resolve()]
    )

def handle_deposit():
    """Handle deposit to escrow"""
    
    return Seq([
        # Check if sender is buyer
        Assert(Txn.sender() == App.globalGet(Bytes("buyer"))),
        
        # Check if status is pending
        Assert(App.globalGet(Bytes("status")) == Bytes("pending")),
        
        # Check if payment amount is correct
        Assert(Txn.amount() == App.globalGet(Bytes("amount"))),
        
        # Update status
        App.globalPut(Bytes("status"), Bytes("deposited")),
        
        # Approve deposit
        Approve()
    ])

def handle_release():
    """Handle release of funds to seller"""
    
    return Seq([
        # Check if sender is buyer or arbitrator
        is_buyer = Txn.sender() == App.globalGet(Bytes("buyer")),
        is_arbitrator = Txn.sender() == App.globalGet(Bytes("arbitrator")),
        Assert(Or(is_buyer, is_arbitrator)),
        
        # Check if status is deposited
        Assert(App.globalGet(Bytes("status")) == Bytes("deposited")),
        
        # Update status
        App.globalPut(Bytes("status"), Bytes("released")),
        
        # Approve release
        Approve()
    ])

def handle_dispute():
    """Handle dispute initiation"""
    
    return Seq([
        # Check if sender is buyer or seller
        is_buyer = Txn.sender() == App.globalGet(Bytes("buyer")),
        is_seller = Txn.sender() == App.globalGet(Bytes("seller")),
        Assert(Or(is_buyer, is_seller)),
        
        # Check if status is deposited
        Assert(App.globalGet(Bytes("status")) == Bytes("deposited")),
        
        # Update status
        App.globalPut(Bytes("status"), Bytes("disputed")),
        
        # Approve dispute
        Approve()
    ])

def handle_resolve():
    """Handle dispute resolution by arbitrator"""
    
    return Seq([
        # Check if sender is arbitrator
        Assert(Txn.sender() == App.globalGet(Bytes("arbitrator"))),
        
        # Check if status is disputed
        Assert(App.globalGet(Bytes("status")) == Bytes("disputed")),
        
        # Get resolution from transaction arguments
        resolution = Txn.application_args[1]
        
        # Update status based on resolution
        If(resolution == Bytes("buyer_wins"),
            App.globalPut(Bytes("status"), Bytes("buyer_wins")),
            If(resolution == Bytes("seller_wins"),
                App.globalPut(Bytes("status"), Bytes("seller_wins")),
                Reject()
            )
        ),
        
        # Approve resolution
        Approve()
    ])
```

## Best Practices

### 1. **Code Organization**

#### Use Functions
```python
def validate_sender():
    """Validate transaction sender"""
    return Txn.sender() == App.globalGet(Bytes("creator"))

def check_balance(amount):
    """Check if user has sufficient balance"""
    user_balance = App.localGet(Txn.sender(), Bytes("balance"))
    return user_balance >= amount
```

#### Use Constants
```python
# Define constants at the top
CREATOR_KEY = Bytes("creator")
BALANCE_KEY = Bytes("balance")
TOTAL_SUPPLY_KEY = Bytes("total_supply")
```

#### Use Comments
```python
def handle_transfer():
    """Transfer tokens between users"""
    
    # Get transfer parameters from transaction
    receiver = Txn.accounts[1]
    amount = Btoi(Txn.application_args[1])
    
    # Validate sender has sufficient balance
    sender_balance = App.localGet(Txn.sender(), BALANCE_KEY)
    Assert(sender_balance >= amount)
    
    # Update balances
    App.localPut(Txn.sender(), BALANCE_KEY, sender_balance - amount)
    receiver_balance = App.localGet(receiver, BALANCE_KEY)
    App.localPut(receiver, BALANCE_KEY, receiver_balance + amount)
    
    return Approve()
```

### 2. **Error Handling**

#### Use Assertions
```python
# Check preconditions
Assert(Txn.sender() == App.globalGet(Bytes("creator")))
Assert(amount > Int(0))
Assert(user_balance >= amount)
```

#### Use Conditional Logic
```python
# Handle different cases
return If(condition,
    Approve(),
    Reject()
)
```

#### Use Reject for Errors
```python
# Reject invalid transactions
return Reject()
```

### 3. **State Management**

#### Initialize State Properly
```python
def handle_creation():
    """Initialize all required state"""
    
    return Seq([
        # Global state
        App.globalPut(Bytes("creator"), Txn.sender()),
        App.globalPut(Bytes("total_supply"), Int(1000000)),
        
        # Approve creation
        Approve()
    ])
```

#### Clean Up State
```python
def handle_close_out():
    """Clean up user state on opt-out"""
    
    return Seq([
        # Check if user can opt out
        user_balance = App.localGet(Txn.sender(), Bytes("balance")),
        Assert(user_balance == Int(0)),
        
        # Clean up state
        App.localDel(Txn.sender(), Bytes("balance")),
        App.localDel(Txn.sender(), Bytes("opted_in")),
        
        # Approve opt-out
        Approve()
    ])
```

### 4. **Testing**

#### Test All Paths
```python
def test_contract():
    """Test contract functionality"""
    
    # Test creation
    # Test opt-in
    # Test operations
    # Test error cases
    pass
```

#### Use Logging
```python
# Log important values
Log(Bytes("Transfer amount: "), amount)
Log(Bytes("Sender balance: "), sender_balance)
Log(Bytes("Receiver balance: "), receiver_balance)
```

### 5. **Security**

#### Validate Inputs
```python
# Check transaction arguments
Assert(Txn.application_args.length() >= Int(2))
amount = Btoi(Txn.application_args[1])
Assert(amount > Int(0))
```

#### Check Authorization
```python
# Verify sender permissions
is_authorized = Or(
    Txn.sender() == App.globalGet(Bytes("creator")),
    Txn.sender() == App.globalGet(Bytes("manager"))
)
Assert(is_authorized)
```

#### Prevent Integer Overflow
```python
# Check for overflow
new_balance = current_balance + amount
Assert(new_balance >= current_balance)  # Check for overflow
```

## Summary

This session covered the fundamentals of smart contracts on Algorand:

- **AVM architecture** and execution model
- **PyTeal framework** for Python development
- **Stateless vs Stateful** contract concepts
- **Approval program logic** and structure
- **Global vs Local state** management
- **Practical examples** of common contract patterns
- **Best practices** for development and security

Key takeaways:
- **Smart contracts** provide programmable logic on the blockchain
- **PyTeal** makes contract development accessible with Python
- **State management** is crucial for complex applications
- **Security** and testing are essential for production contracts
- **Start simple** and gradually add complexity

In the next session, we'll explore Smart Contracts II, diving deeper into advanced AVM concepts, multi-signature transactions, contract inheritance, and security considerations.
