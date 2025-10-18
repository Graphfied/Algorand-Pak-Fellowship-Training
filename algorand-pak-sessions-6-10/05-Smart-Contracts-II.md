# Smart Contracts II

## Table of Contents
1. [Advanced AVM Concepts](#advanced-avm-concepts)
2. [Multi-signature Transactions](#multi-signature-transactions)
3. [Contract Inheritance Basics](#contract-inheritance-basics)
4. [Group Transactions](#group-transactions)
5. [Logic Combination](#logic-combination)
6. [Security Considerations](#security-considerations)
7. [Advanced Examples](#advanced-examples)
8. [Best Practices](#best-practices)

## Advanced AVM Concepts

### Box Storage

#### What is Box Storage?
Box storage is a **key-value storage system** introduced in Algorand that allows smart contracts to store arbitrary data with:
- **Large storage capacity** (up to 32KB per box)
- **Persistent storage** across transactions
- **Efficient access** patterns
- **Cost-effective** for large data

#### Box Storage Operations
```python
from pyteal import *

def box_storage_example():
    """Example of box storage usage"""
    
    # Create a box
    box_name = Bytes("user_data")
    box_size = Int(1000)  # 1000 bytes
    
    # Store data in box
    data = Bytes("Hello, World!")
    return Seq([
        # Create box if it doesn't exist
        If(App.box_length(box_name) == Int(0),
            App.box_create(box_name, box_size)
        ),
        
        # Store data in box
        App.box_put(box_name, Int(0), data),
        
        # Read data from box
        stored_data = App.box_get(box_name, Int(0)),
        
        # Log the data
        Log(stored_data),
        
        Approve()
    ])
```

#### Box Storage Use Cases
- **User profiles** and preferences
- **Large datasets** and configurations
- **File storage** and metadata
- **Caching** frequently accessed data

### Scratch Space

#### What is Scratch Space?
Scratch space is **temporary storage** during transaction execution that:
- **Stores intermediate** calculations
- **Available during** transaction execution
- **Cleared after** transaction completion
- **256 slots** available

#### Scratch Space Operations
```python
def scratch_space_example():
    """Example of scratch space usage"""
    
    # Store values in scratch space
    return Seq([
        # Store intermediate calculations
        ScratchSlot(0).store(Int(100)),
        ScratchSlot(1).store(Int(200)),
        
        # Perform calculations
        sum_result = ScratchSlot(0).load() + ScratchSlot(1).load(),
        ScratchSlot(2).store(sum_result),
        
        # Use the result
        Log(Itob(ScratchSlot(2).load())),
        
        Approve()
    ])
```

### Cross-Contract Communication

#### Contract-to-Contract Calls
```python
def call_other_contract():
    """Call another smart contract"""
    
    # Get the other contract's app ID
    other_app_id = Btoi(Txn.application_args[0])
    
    # Call the other contract
    return Seq([
        # Create inner transaction to call other contract
        InnerTxnBuilder.Begin(),
        InnerTxnBuilder.SetFields({
            TxnField.type_enum: TxnType.ApplicationCall,
            TxnField.application_id: other_app_id,
            TxnField.application_args: [Bytes("method_name")],
            TxnField.sender: Txn.sender(),
        }),
        InnerTxnBuilder.Submit(),
        
        # Continue with current contract logic
        Approve()
    ])
```

#### Contract State Sharing
```python
def share_state_between_contracts():
    """Share state between multiple contracts"""
    
    # Read state from another contract
    other_app_id = Btoi(Txn.application_args[0])
    shared_value = App.globalGetEx(other_app_id, Bytes("shared_key"))
    
    return Seq([
        # Check if the value exists
        If(shared_value.hasValue(),
            # Use the shared value
            Log(Bytes("Shared value: "), shared_value.value()),
            # Handle missing value
            Log(Bytes("No shared value found"))
        ),
        
        Approve()
    ])
```

## Multi-signature Transactions

### What are Multi-signature Transactions?

Multi-signature (multisig) transactions require **multiple signatures** to be valid. They provide:
- **Enhanced security** through multiple approvals
- **Shared control** over assets
- **Flexible authorization** schemes
- **Risk distribution** across multiple parties

### Multi-signature Concepts

#### 1. **Threshold Signatures**
- **M-of-N** signature scheme
- **M signatures** required out of N possible signers
- **Flexible authorization** levels
- **Common examples**: 2-of-3, 3-of-5, 5-of-7

#### 2. **Signature Validation**
- **Cryptographic verification** of each signature
- **Order-independent** validation
- **Duplicate signature** prevention
- **Invalid signature** rejection

#### 3. **Authorization Levels**
- **Single signature**: 1-of-1 (standard)
- **Multi-signature**: M-of-N (shared control)
- **Hierarchical**: Different levels for different operations
- **Time-based**: Signatures expire after certain time

### Multi-signature Implementation

#### Basic Multi-signature Logic
```python
def multisig_validation():
    """Validate multi-signature transaction"""
    
    # Define required signers
    SIGNER_1 = Bytes("SIGNER_1_ADDRESS")
    SIGNER_2 = Bytes("SIGNER_2_ADDRESS")
    SIGNER_3 = Bytes("SIGNER_3_ADDRESS")
    
    # Check if sender is one of the valid signers
    is_signer_1 = Txn.sender() == SIGNER_1
    is_signer_2 = Txn.sender() == SIGNER_2
    is_signer_3 = Txn.sender() == SIGNER_3
    
    # At least one valid signer must be present
    has_valid_signer = Or(is_signer_1, is_signer_2, is_signer_3)
    
    return Seq([
        # Validate sender
        Assert(has_valid_signer),
        
        # Additional validation logic
        # (e.g., check transaction amount, destination, etc.)
        
        # Approve transaction
        Approve()
    ])
```

#### Threshold Multi-signature
```python
def threshold_multisig():
    """Threshold multi-signature validation"""
    
    # Define signers and threshold
    SIGNERS = [Bytes("SIGNER_1"), Bytes("SIGNER_2"), Bytes("SIGNER_3")]
    THRESHOLD = Int(2)  # Require 2 out of 3 signatures
    
    # Check if sender is a valid signer
    is_valid_signer = Or(
        Txn.sender() == SIGNERS[0],
        Txn.sender() == SIGNERS[1],
        Txn.sender() == SIGNERS[2]
    )
    
    return Seq([
        # Validate sender
        Assert(is_valid_signer),
        
        # Additional validation
        # (e.g., check transaction parameters)
        
        # Approve transaction
        Approve()
    ])
```

### Multi-signature Use Cases

#### 1. **Treasury Management**
- **Corporate treasuries** with multiple approvers
- **DAO funds** requiring community approval
- **Escrow services** with multiple stakeholders
- **Charity funds** with oversight

#### 2. **Asset Security**
- **High-value assets** requiring multiple approvals
- **NFT collections** with shared ownership
- **Real estate** with multiple owners
- **Investment funds** with multiple managers

#### 3. **Operational Control**
- **System administration** with multiple admins
- **Contract upgrades** requiring approval
- **Emergency procedures** with multiple validators
- **Compliance** with regulatory requirements

## Contract Inheritance Basics

### What is Contract Inheritance?

Contract inheritance allows **reusing and extending** existing contract logic by:
- **Inheriting** base contract functionality
- **Overriding** specific methods
- **Adding** new functionality
- **Maintaining** code reusability

### ARC-4 Contract Standard

#### ARC-4 Overview
ARC-4 is a **standard for typed methods** in Algorand smart contracts that provides:
- **Type safety** for method calls
- **Standardized** method signatures
- **Better developer** experience
- **Interoperability** between contracts

#### ARC-4 Method Structure
```python
def arc4_method():
    """ARC-4 compliant method"""
    
    # Method signature
    method_name = Bytes("method_name")
    method_args = Txn.application_args
    
    # Validate method call
    return Seq([
        # Check method name
        Assert(method_args[0] == method_name),
        
        # Validate argument count
        Assert(method_args.length() == Int(2)),
        
        # Extract arguments
        arg1 = method_args[1],
        
        # Method logic
        # ...
        
        # Return result
        Approve()
    ])
```

### Inheritance Patterns

#### 1. **Base Contract Pattern**
```python
def base_contract():
    """Base contract with common functionality"""
    
    def validate_sender():
        """Validate transaction sender"""
        return Txn.sender() == App.globalGet(Bytes("creator"))
    
    def check_balance(amount):
        """Check user balance"""
        user_balance = App.localGet(Txn.sender(), Bytes("balance"))
        return user_balance >= amount
    
    def update_balance(amount):
        """Update user balance"""
        current_balance = App.localGet(Txn.sender(), Bytes("balance"))
        new_balance = current_balance + amount
        return App.localPut(Txn.sender(), Bytes("balance"), new_balance)
    
    return {
        "validate_sender": validate_sender,
        "check_balance": check_balance,
        "update_balance": update_balance
    }
```

#### 2. **Inherited Contract Pattern**
```python
def inherited_contract():
    """Contract that inherits from base"""
    
    # Import base contract functions
    base = base_contract()
    
    def transfer_tokens():
        """Transfer tokens using inherited functions"""
        
        # Get transfer parameters
        receiver = Txn.accounts[1]
        amount = Btoi(Txn.application_args[1])
        
        return Seq([
            # Use inherited validation
            Assert(base["validate_sender"]()),
            Assert(base["check_balance"](amount)),
            
            # Update balances
            base["update_balance"](-amount),
            App.localPut(receiver, Bytes("balance"), 
                        App.localGet(receiver, Bytes("balance")) + amount),
            
            # Approve transfer
            Approve()
        ])
    
    return transfer_tokens
```

### Contract Composition

#### 1. **Mixin Pattern**
```python
def security_mixin():
    """Security-related functionality mixin"""
    
    def check_pause_status():
        """Check if contract is paused"""
        return App.globalGet(Bytes("paused")) == Int(0)
    
    def check_blacklist():
        """Check if sender is blacklisted"""
        return App.localGet(Txn.sender(), Bytes("blacklisted")) == Int(0)
    
    return {
        "check_pause_status": check_pause_status,
        "check_blacklist": check_blacklist
    }

def token_contract_with_security():
    """Token contract with security mixin"""
    
    # Import security mixin
    security = security_mixin()
    
    def secure_transfer():
        """Secure token transfer"""
        
        return Seq([
            # Apply security checks
            Assert(security["check_pause_status"]()),
            Assert(security["check_blacklist"]()),
            
            # Transfer logic
            # ...
            
            Approve()
        ])
    
    return secure_transfer
```

#### 2. **Interface Pattern**
```python
def token_interface():
    """Standard token interface"""
    
    def transfer():
        """Transfer tokens"""
        pass
    
    def mint():
        """Mint new tokens"""
        pass
    
    def burn():
        """Burn tokens"""
        pass
    
    return {
        "transfer": transfer,
        "mint": mint,
        "burn": burn
    }

def erc20_like_token():
    """ERC-20 like token implementation"""
    
    # Implement token interface
    interface = token_interface()
    
    def transfer():
        """Implement transfer method"""
        # Transfer logic
        return Approve()
    
    def mint():
        """Implement mint method"""
        # Mint logic
        return Approve()
    
    def burn():
        """Implement burn method"""
        # Burn logic
        return Approve()
    
    return {
        "transfer": transfer,
        "mint": mint,
        "burn": burn
    }
```

## Group Transactions

### What are Group Transactions?

Group transactions are **multiple transactions** that are executed together as a single unit. They provide:
- **Atomic execution** (all succeed or all fail)
- **Complex operations** across multiple contracts
- **Efficient batching** of operations
- **Cross-contract** interactions

### Group Transaction Concepts

#### 1. **Atomicity**
- **All transactions** in group must succeed
- **If any fails**, entire group fails
- **No partial** execution
- **Consistent state** across all operations

#### 2. **Ordering**
- **Transactions** execute in order
- **State changes** are sequential
- **Dependencies** can be managed
- **Predictable** execution flow

#### 3. **Validation**
- **Each transaction** is validated independently
- **Group constraints** are checked
- **Resource limits** apply to entire group
- **Fee calculation** for entire group

### Group Transaction Implementation

#### Basic Group Transaction
```python
def group_transaction_example():
    """Example of group transaction"""
    
    # First transaction: Transfer tokens
    transfer_txn = Seq([
        # Transfer logic
        # ...
        Approve()
    ])
    
    # Second transaction: Update state
    update_txn = Seq([
        # State update logic
        # ...
        Approve()
    ])
    
    # Third transaction: Log event
    log_txn = Seq([
        # Logging logic
        # ...
        Approve()
    ])
    
    return Seq([
        transfer_txn,
        update_txn,
        log_txn
    ])
```

#### Cross-Contract Group Transaction
```python
def cross_contract_group():
    """Group transaction across multiple contracts"""
    
    # Get other contract IDs
    token_contract = Btoi(Txn.application_args[0])
    nft_contract = Btoi(Txn.application_args[1])
    
    return Seq([
        # First transaction: Call token contract
        InnerTxnBuilder.Begin(),
        InnerTxnBuilder.SetFields({
            TxnField.type_enum: TxnType.ApplicationCall,
            TxnField.application_id: token_contract,
            TxnField.application_args: [Bytes("transfer")],
        }),
        InnerTxnBuilder.Submit(),
        
        # Second transaction: Call NFT contract
        InnerTxnBuilder.Begin(),
        InnerTxnBuilder.SetFields({
            TxnField.type_enum: TxnType.ApplicationCall,
            TxnField.application_id: nft_contract,
            TxnField.application_args: [Bytes("mint")],
        }),
        InnerTxnBuilder.Submit(),
        
        # Approve group transaction
        Approve()
    ])
```

### Group Transaction Use Cases

#### 1. **Atomic Swaps**
- **Exchange tokens** between different contracts
- **Ensure both** sides complete
- **Prevent partial** executions
- **Cross-chain** compatibility

#### 2. **Complex DeFi Operations**
- **Lending and borrowing** in single transaction
- **Liquidity provision** with multiple steps
- **Yield farming** with multiple contracts
- **Arbitrage** opportunities

#### 3. **Multi-step Workflows**
- **User onboarding** with multiple steps
- **Asset management** with multiple operations
- **Governance** with multiple approvals
- **Compliance** with multiple validations

## Logic Combination

### What is Logic Combination?

Logic combination allows **combining multiple** contract logics into a single transaction by:
- **Merging** different contract functionalities
- **Creating** complex business logic
- **Reusing** existing contract code
- **Building** modular systems

### Logic Combination Patterns

#### 1. **Sequential Logic**
```python
def sequential_logic():
    """Execute logic in sequence"""
    
    return Seq([
        # Step 1: Validate input
        Assert(Txn.application_args.length() >= Int(2)),
        
        # Step 2: Check permissions
        Assert(Txn.sender() == App.globalGet(Bytes("creator"))),
        
        # Step 3: Process data
        amount = Btoi(Txn.application_args[1]),
        new_balance = App.globalGet(Bytes("balance")) + amount,
        
        # Step 4: Update state
        App.globalPut(Bytes("balance"), new_balance),
        
        # Step 5: Log result
        Log(Bytes("Balance updated: "), Itob(new_balance)),
        
        # Step 6: Approve
        Approve()
    ])
```

#### 2. **Conditional Logic**
```python
def conditional_logic():
    """Execute logic based on conditions"""
    
    # Get operation type
    operation = Txn.application_args[0]
    
    return Cond(
        [operation == Bytes("mint"), handle_mint()],
        [operation == Bytes("burn"), handle_burn()],
        [operation == Bytes("transfer"), handle_transfer()],
        [operation == Bytes("freeze"), handle_freeze()],
        [operation == Bytes("unfreeze"), handle_unfreeze()],
        [operation == Bytes("pause"), handle_pause()],
        [operation == Bytes("unpause"), handle_unpause()]
    )
```

#### 3. **Parallel Logic**
```python
def parallel_logic():
    """Execute multiple logic branches in parallel"""
    
    # Get multiple operations
    operations = Txn.application_args
    
    return Seq([
        # Process each operation
        For(Int(0), Int(operations.length()), Int(1), 
            lambda i: process_operation(operations[i])
        ),
        
        # Approve all operations
        Approve()
    ])
```

### Advanced Logic Patterns

#### 1. **State Machine Pattern**
```python
def state_machine():
    """State machine pattern for complex logic"""
    
    # Get current state
    current_state = App.globalGet(Bytes("state"))
    
    # Get transition
    transition = Txn.application_args[0]
    
    return Cond(
        # State: PENDING
        [current_state == Bytes("pending"),
            Cond(
                [transition == Bytes("approve"), transition_to_approved()],
                [transition == Bytes("reject"), transition_to_rejected()],
                [transition == Bytes("cancel"), transition_to_cancelled()]
            )
        ],
        
        # State: APPROVED
        [current_state == Bytes("approved"),
            Cond(
                [transition == Bytes("execute"), transition_to_executed()],
                [transition == Bytes("cancel"), transition_to_cancelled()]
            )
        ],
        
        # State: EXECUTED
        [current_state == Bytes("executed"),
            # No transitions allowed
            Reject()
        ]
    )
```

#### 2. **Plugin Pattern**
```python
def plugin_system():
    """Plugin system for extensible logic"""
    
    # Get plugin type
    plugin_type = Txn.application_args[0]
    
    return Cond(
        [plugin_type == Bytes("payment"), payment_plugin()],
        [plugin_type == Bytes("nft"), nft_plugin()],
        [plugin_type == Bytes("governance"), governance_plugin()],
        [plugin_type == Bytes("staking"), staking_plugin()]
    )

def payment_plugin():
    """Payment processing plugin"""
    
    return Seq([
        # Payment logic
        # ...
        Approve()
    ])

def nft_plugin():
    """NFT processing plugin"""
    
    return Seq([
        # NFT logic
        # ...
        Approve()
    ])
```

## Security Considerations

### Common Security Vulnerabilities

#### 1. **Integer Overflow/Underflow**
```python
def safe_arithmetic():
    """Safe arithmetic operations"""
    
    # Get values
    a = Btoi(Txn.application_args[0])
    b = Btoi(Txn.application_args[1])
    
    # Check for overflow before addition
    return Seq([
        # Check if addition will overflow
        If(a > Int(0),
            Assert(b <= Int(9223372036854775807) - a),  # Max int64 - a
            # Handle negative case
            Assert(b >= Int(-9223372036854775808) - a)   # Min int64 - a
        ),
        
        # Perform safe addition
        result = a + b,
        
        # Use result
        Log(Itob(result)),
        
        Approve()
    ])
```

#### 2. **Reentrancy Attacks**
```python
def reentrancy_protection():
    """Protect against reentrancy attacks"""
    
    # Set reentrancy flag
    return Seq([
        # Check if already processing
        processing = App.globalGet(Bytes("processing")),
        Assert(processing == Int(0)),
        
        # Set processing flag
        App.globalPut(Bytes("processing"), Int(1)),
        
        # Perform operations
        # ...
        
        # Clear processing flag
        App.globalPut(Bytes("processing"), Int(0)),
        
        # Approve transaction
        Approve()
    ])
```

#### 3. **Access Control**
```python
def access_control():
    """Implement proper access control"""
    
    # Define roles
    ADMIN_ROLE = Bytes("admin")
    USER_ROLE = Bytes("user")
    
    # Check user role
    user_role = App.localGet(Txn.sender(), Bytes("role"))
    
    # Validate access
    return Seq([
        # Check if user has required role
        Assert(Or(
            user_role == ADMIN_ROLE,
            user_role == USER_ROLE
        )),
        
        # Additional role-based checks
        If(user_role == USER_ROLE,
            # User-specific restrictions
            Assert(Txn.amount() <= Int(1000000)),  # Max 1 ALGO
            # Admin has no restrictions
        ),
        
        # Approve transaction
        Approve()
    ])
```

### Security Best Practices

#### 1. **Input Validation**
```python
def validate_inputs():
    """Validate all inputs thoroughly"""
    
    return Seq([
        # Check argument count
        Assert(Txn.application_args.length() >= Int(2)),
        
        # Validate argument types
        amount = Btoi(Txn.application_args[1]),
        Assert(amount > Int(0)),
        Assert(amount <= Int(1000000000)),  # Max 1000 ALGO
        
        # Validate account references
        Assert(Txn.accounts.length() >= Int(1)),
        
        # Additional validations
        # ...
        
        Approve()
    ])
```

#### 2. **State Validation**
```python
def validate_state():
    """Validate state before and after operations"""
    
    return Seq([
        # Get current state
        current_balance = App.globalGet(Bytes("balance")),
        
        # Validate state consistency
        Assert(current_balance >= Int(0)),
        
        # Perform operation
        # ...
        
        # Validate state after operation
        new_balance = App.globalGet(Bytes("balance")),
        Assert(new_balance >= Int(0)),
        
        # Approve transaction
        Approve()
    ])
```

#### 3. **Error Handling**
```python
def error_handling():
    """Implement proper error handling"""
    
    return Seq([
        # Try to perform operation
        If(operation_succeeds(),
            # Success path
            Seq([
                # Update state
                # ...
                Approve()
            ]),
            # Error path
            Seq([
                # Log error
                Log(Bytes("Operation failed")),
                
                # Revert state if needed
                # ...
                
                # Reject transaction
                Reject()
            ])
        )
    ])
```

## Advanced Examples

### Example 1: Decentralized Exchange

```python
def decentralized_exchange():
    """Decentralized exchange contract"""
    
    return Cond(
        [Txn.application_id() == Int(0), handle_creation()],
        [Txn.on_completion() == OnComplete.OptIn, handle_opt_in()],
        [Txn.on_completion() == OnComplete.NoOp, handle_no_op()]
    )

def handle_creation():
    """Initialize DEX contract"""
    
    return Seq([
        # Set DEX parameters
        App.globalPut(Bytes("token_a"), Int(0)),
        App.globalPut(Bytes("token_b"), Int(0)),
        App.globalPut(Bytes("reserve_a"), Int(0)),
        App.globalPut(Bytes("reserve_b"), Int(0)),
        App.globalPut(Bytes("fee_rate"), Int(30)),  # 0.3%
        App.globalPut(Bytes("creator"), Txn.sender()),
        
        # Approve creation
        Approve()
    ])

def handle_opt_in():
    """Handle user opt-in"""
    
    return Seq([
        # Initialize user state
        App.localPut(Txn.sender(), Bytes("liquidity"), Int(0)),
        App.localPut(Txn.sender(), Bytes("opted_in"), Int(1)),
        
        # Approve opt-in
        Approve()
    ])

def handle_no_op():
    """Handle DEX operations"""
    
    method = Txn.application_args[0]
    
    return Cond(
        [method == Bytes("add_liquidity"), handle_add_liquidity()],
        [method == Bytes("remove_liquidity"), handle_remove_liquidity()],
        [method == Bytes("swap"), handle_swap()],
        [method == Bytes("get_price"), handle_get_price()]
    )

def handle_add_liquidity():
    """Add liquidity to the pool"""
    
    # Get liquidity amounts
    amount_a = Btoi(Txn.application_args[1])
    amount_b = Btoi(Txn.application_args[2])
    
    return Seq([
        # Check if pool is empty
        reserve_a = App.globalGet(Bytes("reserve_a")),
        reserve_b = App.globalGet(Bytes("reserve_b")),
        
        If(And(reserve_a == Int(0), reserve_b == Int(0)),
            # First liquidity provision
            Seq([
                # Set initial reserves
                App.globalPut(Bytes("reserve_a"), amount_a),
                App.globalPut(Bytes("reserve_b"), amount_b),
                
                # Mint initial liquidity tokens
                liquidity_tokens = amount_a,  # Simplified
                App.localPut(Txn.sender(), Bytes("liquidity"), liquidity_tokens),
            ]),
            # Subsequent liquidity provision
            Seq([
                # Calculate required amounts based on current ratio
                required_b = (reserve_b * amount_a) / reserve_a,
                Assert(amount_b >= required_b),
                
                # Update reserves
                App.globalPut(Bytes("reserve_a"), reserve_a + amount_a),
                App.globalPut(Bytes("reserve_b"), reserve_b + amount_b),
                
                # Calculate and mint liquidity tokens
                liquidity_tokens = (amount_a * App.localGet(Txn.sender(), Bytes("liquidity"))) / reserve_a,
                App.localPut(Txn.sender(), Bytes("liquidity"), 
                           App.localGet(Txn.sender(), Bytes("liquidity")) + liquidity_tokens),
            ])
        ),
        
        # Approve transaction
        Approve()
    ])

def handle_swap():
    """Execute a token swap"""
    
    # Get swap parameters
    token_in = Btoi(Txn.application_args[1])
    amount_in = Btoi(Txn.application_args[2])
    min_amount_out = Btoi(Txn.application_args[3])
    
    return Seq([
        # Get current reserves
        reserve_a = App.globalGet(Bytes("reserve_a")),
        reserve_b = App.globalGet(Bytes("reserve_b")),
        
        # Calculate output amount using constant product formula
        fee_rate = App.globalGet(Bytes("fee_rate")),
        amount_in_with_fee = amount_in * (Int(10000) - fee_rate) / Int(10000),
        
        # Calculate output amount
        amount_out = (amount_in_with_fee * reserve_b) / (reserve_a + amount_in_with_fee),
        
        # Check minimum output
        Assert(amount_out >= min_amount_out),
        
        # Update reserves
        If(token_in == App.globalGet(Bytes("token_a")),
            Seq([
                App.globalPut(Bytes("reserve_a"), reserve_a + amount_in),
                App.globalPut(Bytes("reserve_b"), reserve_b - amount_out),
            ]),
            Seq([
                App.globalPut(Bytes("reserve_a"), reserve_a - amount_out),
                App.globalPut(Bytes("reserve_b"), reserve_b + amount_in),
            ])
        ),
        
        # Approve transaction
        Approve()
    ])
```

### Example 2: Governance Contract

```python
def governance_contract():
    """Governance contract for DAO"""
    
    return Cond(
        [Txn.application_id() == Int(0), handle_creation()],
        [Txn.on_completion() == OnComplete.OptIn, handle_opt_in()],
        [Txn.on_completion() == OnComplete.NoOp, handle_no_op()]
    )

def handle_creation():
    """Initialize governance contract"""
    
    return Seq([
        # Set governance parameters
        App.globalPut(Bytes("proposal_count"), Int(0)),
        App.globalPut(Bytes("voting_period"), Int(7)),  # 7 days
        App.globalPut(Bytes("quorum"), Int(1000)),  # 1000 tokens
        App.globalPut(Bytes("creator"), Txn.sender()),
        
        # Approve creation
        Approve()
    ])

def handle_opt_in():
    """Handle user opt-in"""
    
    return Seq([
        # Initialize user state
        App.localPut(Txn.sender(), Bytes("voting_power"), Int(0)),
        App.localPut(Txn.sender(), Bytes("opted_in"), Int(1)),
        
        # Approve opt-in
        Approve()
    ])

def handle_no_op():
    """Handle governance operations"""
    
    method = Txn.application_args[0]
    
    return Cond(
        [method == Bytes("create_proposal"), handle_create_proposal()],
        [method == Bytes("vote"), handle_vote()],
        [method == Bytes("execute_proposal"), handle_execute_proposal()],
        [method == Bytes("get_proposal"), handle_get_proposal()]
    )

def handle_create_proposal():
    """Create a new governance proposal"""
    
    # Get proposal details
    proposal_id = App.globalGet(Bytes("proposal_count")) + Int(1)
    description = Txn.application_args[1]
    execution_data = Txn.application_args[2]
    
    return Seq([
        # Check if sender has voting power
        voting_power = App.localGet(Txn.sender(), Bytes("voting_power")),
        Assert(voting_power > Int(0)),
        
        # Create proposal
        App.globalPut(Bytes("proposal_count"), proposal_id),
        App.globalPut(Concat(Bytes("proposal_"), Itob(proposal_id), Bytes("_description")), description),
        App.globalPut(Concat(Bytes("proposal_"), Itob(proposal_id), Bytes("_execution_data")), execution_data),
        App.globalPut(Concat(Bytes("proposal_"), Itob(proposal_id), Bytes("_creator")), Txn.sender()),
        App.globalPut(Concat(Bytes("proposal_"), Itob(proposal_id), Bytes("_start_time")), Global.latest_timestamp()),
        App.globalPut(Concat(Bytes("proposal_"), Itob(proposal_id), Bytes("_yes_votes")), Int(0)),
        App.globalPut(Concat(Bytes("proposal_"), Itob(proposal_id), Bytes("_no_votes")), Int(0)),
        App.globalPut(Concat(Bytes("proposal_"), Itob(proposal_id), Bytes("_status")), Bytes("active")),
        
        # Log proposal creation
        Log(Concat(Bytes("Proposal created: "), Itob(proposal_id))),
        
        # Approve transaction
        Approve()
    ])

def handle_vote():
    """Vote on a governance proposal"""
    
    # Get vote parameters
    proposal_id = Btoi(Txn.application_args[1])
    vote_choice = Txn.application_args[2]  # "yes" or "no"
    
    return Seq([
        # Check if proposal exists and is active
        proposal_status = App.globalGet(Concat(Bytes("proposal_"), Itob(proposal_id), Bytes("_status"))),
        Assert(proposal_status == Bytes("active")),
        
        # Check if voting period is still active
        start_time = App.globalGet(Concat(Bytes("proposal_"), Itob(proposal_id), Bytes("_start_time"))),
        voting_period = App.globalGet(Bytes("voting_period")),
        current_time = Global.latest_timestamp(),
        Assert(current_time <= start_time + voting_period),
        
        # Check if user has voting power
        voting_power = App.localGet(Txn.sender(), Bytes("voting_power")),
        Assert(voting_power > Int(0)),
        
        # Check if user hasn't already voted
        user_vote = App.localGet(Txn.sender(), Concat(Bytes("vote_"), Itob(proposal_id))),
        Assert(user_vote == Int(0)),
        
        # Record vote
        App.localPut(Txn.sender(), Concat(Bytes("vote_"), Itob(proposal_id)), Int(1)),
        
        # Update vote counts
        If(vote_choice == Bytes("yes"),
            Seq([
                yes_votes = App.globalGet(Concat(Bytes("proposal_"), Itob(proposal_id), Bytes("_yes_votes"))),
                App.globalPut(Concat(Bytes("proposal_"), Itob(proposal_id), Bytes("_yes_votes")), yes_votes + voting_power),
            ]),
            Seq([
                no_votes = App.globalGet(Concat(Bytes("proposal_"), Itob(proposal_id), Bytes("_no_votes"))),
                App.globalPut(Concat(Bytes("proposal_"), Itob(proposal_id), Bytes("_no_votes")), no_votes + voting_power),
            ])
        ),
        
        # Log vote
        Log(Concat(Bytes("Vote recorded for proposal "), Itob(proposal_id))),
        
        # Approve transaction
        Approve()
    ])
```

## Best Practices

### 1. **Code Organization**

#### Modular Design
```python
def modular_contract():
    """Modular contract design"""
    
    # Separate concerns into different functions
    def validation_logic():
        """Handle input validation"""
        pass
    
    def business_logic():
        """Handle business operations"""
        pass
    
    def state_management():
        """Handle state updates"""
        pass
    
    def event_logging():
        """Handle event logging"""
        pass
    
    # Combine all logic
    return Seq([
        validation_logic(),
        business_logic(),
        state_management(),
        event_logging(),
        Approve()
    ])
```

#### Error Handling
```python
def robust_error_handling():
    """Robust error handling"""
    
    return Seq([
        # Try to perform operation
        If(operation_succeeds(),
            # Success path
            Seq([
                # Update state
                # ...
                Log(Bytes("Operation successful")),
                Approve()
            ]),
            # Error path
            Seq([
                # Log error details
                Log(Bytes("Operation failed: "), Txn.application_args[0]),
                
                # Revert state if needed
                # ...
                
                # Reject transaction
                Reject()
            ])
        )
    ])
```

### 2. **Performance Optimization**

#### Efficient State Access
```python
def efficient_state_access():
    """Efficient state access patterns"""
    
    # Cache frequently accessed values
    return Seq([
        # Get values once
        creator = App.globalGet(Bytes("creator")),
        total_supply = App.globalGet(Bytes("total_supply")),
        
        # Use cached values
        If(Txn.sender() == creator,
            # Creator operations
            Seq([
                # Use total_supply
                # ...
            ]),
            # User operations
            Seq([
                # Use total_supply
                # ...
            ])
        ),
        
        Approve()
    ])
```

#### Resource Management
```python
def resource_management():
    """Manage contract resources efficiently"""
    
    return Seq([
        # Check resource limits
        # ...
        
        # Use scratch space for temporary calculations
        ScratchSlot(0).store(Int(100)),
        ScratchSlot(1).store(Int(200)),
        result = ScratchSlot(0).load() + ScratchSlot(1).load(),
        
        # Use result
        Log(Itob(result)),
        
        Approve()
    ])
```

### 3. **Testing and Debugging**

#### Comprehensive Testing
```python
def test_contract():
    """Test contract functionality"""
    
    # Test all code paths
    # Test edge cases
    # Test error conditions
    # Test state transitions
    pass
```

#### Debug Logging
```python
def debug_logging():
    """Add debug logging for troubleshooting"""
    
    return Seq([
        # Log important values
        Log(Bytes("Debug: Sender = "), Txn.sender()),
        Log(Bytes("Debug: Amount = "), Itob(Txn.amount())),
        Log(Bytes("Debug: Args = "), Txn.application_args[0]),
        
        # Continue with logic
        # ...
        
        Approve()
    ])
```

## Summary

This session covered advanced smart contract concepts on Algorand:

- **Advanced AVM features** including box storage and cross-contract communication
- **Multi-signature transactions** for enhanced security
- **Contract inheritance** and ARC-4 standards
- **Group transactions** for complex operations
- **Logic combination** patterns for modular design
- **Security considerations** and best practices
- **Advanced examples** of real-world applications

Key takeaways:
- **Advanced features** enable complex applications
- **Security** is paramount in smart contract development
- **Modular design** improves maintainability
- **Testing** is essential for production contracts
- **Best practices** prevent common vulnerabilities

This completes our comprehensive coverage of smart contracts on Algorand. You now have the knowledge and tools to build sophisticated decentralized applications using the Algorand blockchain.
