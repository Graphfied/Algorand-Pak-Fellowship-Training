# Smart Contracts in Algorand

Algorand has a unique approach to smart contracts that sets it apart from other blockchains. Let's explore how smart contracts work specifically on Algorand, including the differences between stateless and stateful contracts, and the Approval vs ClearState programs.

## Algorand's Smart Contract Architecture

### Two Types of Smart Contracts

Algorand supports two distinct types of smart contracts:

1. **Stateless Smart Contracts** (Logic Signatures)
2. **Stateful Smart Contracts** (Applications)

### Stateless Smart Contracts (Logic Signatures)

**Think of them as "smart signatures"** - they validate transactions but don't store data.

#### Characteristics:
- **No state storage** - Cannot store data
- **Transaction validation** - Approve or reject transactions
- **Lightweight** - Fast and cheap to execute
- **Account-based** - Attached to specific accounts

#### Use Cases:
- **Multi-signature wallets** - Require multiple signatures
- **Time-locked transactions** - Execute at specific times
- **Conditional payments** - Pay only if conditions are met
- **Atomic swaps** - Exchange assets without intermediaries

#### Example Concept:
**Time-locked Payment**: A contract that only allows withdrawals after a specific date
- **Logic**: Check if current time is after the specified timestamp
- **Validation**: Ensure transaction amount doesn't exceed limit
- **Use Case**: Inheritance, vesting schedules, delayed payments

### Stateful Smart Contracts (Applications)

**Think of them as "smart applications"** - they can store data and maintain state.

#### Characteristics:
- **State storage** - Can store global and local state
- **Complex logic** - Full programming capabilities
- **Persistent data** - Data survives between transactions
- **Application-based** - Independent applications

#### Use Cases:
- **DeFi protocols** - Lending, trading, yield farming
- **NFT marketplaces** - Buy, sell, trade NFTs
- **Gaming** - In-game assets and logic
- **Governance** - Voting and decision making

#### Example Concept:
**Voting System**: A contract that tracks votes and prevents double voting
- **Global State**: Stores total vote count (shared by all users)
- **Local State**: Tracks if each user has voted (private per user)
- **Logic**: Allow voting only if user hasn't voted before
- **Use Case**: Governance, polls, decision making

## Approval vs ClearState Programs

Stateful smart contracts in Algorand have **two separate programs**:

### 1. **Approval Program**
- **Main logic** of the smart contract
- **Handles all transactions** except opt-out
- **Contains business logic** and state updates
- **Most important program**

### 2. **ClearState Program**
- **Handles opt-out transactions** only
- **Cleanup logic** when users leave
- **Simpler program** with limited functionality
- **Optional but recommended**

### Why Two Programs?

```
User Interaction:
├── Normal transactions → Approval Program
├── Opt-in transactions → Approval Program
└── Opt-out transactions → ClearState Program
```

This separation allows for:
- **Better security** - ClearState can't access main logic
- **Cleaner code** - Separation of concerns
- **Easier maintenance** - Different programs for different purposes

## Smart Contract Lifecycle

### 1. **Creation**
```python
# Deploy smart contract
def create_contract():
    # Compile approval program
    approval_program = compile_approval_program()
    
    # Compile clear state program
    clear_state_program = compile_clear_state_program()
    
    # Create application
    app_id = create_application(
        approval_program=approval_program,
        clear_state_program=clear_state_program
    )
    
    return app_id
```

### 2. **Opt-in (User Joins)**
```python
# User opts into the contract
def opt_in(user_address, app_id):
    # User calls the contract
    # Approval program handles opt-in
    # User gets local state storage
    pass
```

### 3. **Interaction (Normal Use)**
```python
# User interacts with contract
def interact_with_contract(user_address, app_id, function_call):
    # User calls specific function
    # Approval program executes logic
    # State is updated
    pass
```

### 4. **Opt-out (User Leaves)**
```python
# User opts out of contract
def opt_out(user_address, app_id):
    # User calls opt-out
    # ClearState program handles cleanup
    # User's local state is cleared
    pass
```

## State Management in Algorand

### Global State
- **Shared by all users** of the contract
- **Limited storage** (expensive)
- **Examples**: Total supply, contract settings, global counters

```python
# Global state operations
def update_global_state():
    # Set global state
    App.globalPut(Bytes("total_supply"), Int(1000000))
    
    # Get global state
    total_supply = App.globalGet(Bytes("total_supply"))
    
    # Delete global state
    App.globalDel(Bytes("old_key"))
```

### Local State
- **Specific to each user** (account)
- **More storage** available per user
- **Examples**: User balance, voting history, preferences

```python
# Local state operations
def update_local_state():
    # Set local state for user
    App.localPut(Int(0), Bytes("balance"), Int(1000))
    
    # Get local state for user
    balance = App.localGet(Int(0), Bytes("balance"))
    
    # Delete local state for user
    App.localDel(Int(0), Bytes("old_key"))
```

## Smart Contract Examples

### Example 1: Simple Counter (Stateful)
### Example 2: Multi-signature Wallet (Stateless)



## Smart Contract Development Tools

### 1. **PyTeal**
- **Python-based** smart contract language
- **Familiar syntax** for Python developers
- **Compiles to TEAL** (Algorand's bytecode)

### 2. **Algorand Python (Puya)**
- **Modern Python** for smart contracts
- **Type safety** and better tooling
- **Future of Algorand development**

### 3. **AlgoKit**
- **Development framework** for Algorand
- **Local development** environment
- **Testing and deployment** tools


## Best Practices

### 1. **Security**
- **Validate all inputs** - Check parameters
- **Check permissions** - Verify caller identity
- **Handle errors** - Graceful error handling
- **Test thoroughly** - Comprehensive testing

### 2. **Gas Optimization**
- **Minimize state operations** - State is expensive
- **Use local state** when possible
- **Optimize loops** - Avoid expensive operations
- **Batch operations** - Combine multiple operations

### 3. **Code Organization**
- **Separate concerns** - Approval vs ClearState
- **Use functions** - Modular code
- **Document code** - Clear comments
- **Version control** - Track changes

### 4. **Testing**
- **Unit tests** - Test individual functions
- **Integration tests** - Test full workflows
- **Edge cases** - Test boundary conditions
- **Security tests** - Test for vulnerabilities

## Common Patterns

### 1. **State Machine Pattern**


### 2. **Factory Pattern**


### 3. **Proxy Pattern**


## Key Takeaways

- **Algorand supports** both stateless and stateful smart contracts
- **Stateless contracts** are lightweight and fast
- **Stateful contracts** can store data and maintain state
- **Approval programs** handle main logic
- **ClearState programs** handle opt-out cleanup
- **Global state** is shared by all users
- **Local state** is specific to each user
- **PyTeal and Algorand Python** are the main development tools

## Next Steps

Now that you understand smart contracts in Algorand, let's explore:
1. **Stateless vs Stateful** - Detailed comparison of the two types
2. **Python Basics** - Essential Python concepts for blockchain development

Understanding these concepts will help you choose the right type of smart contract for your needs!
