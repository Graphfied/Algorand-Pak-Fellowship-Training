# Smart Contracts High Level

Now that you understand what smart contracts are, let's explore how they interact with the blockchain at a high level. This includes understanding the ledger, global/local state, and how new transactions are created.

## The Blockchain Ledger

### What is the Ledger?

The blockchain ledger is like a **giant, shared database** that everyone can see and verify:

```
Block 1: [Transaction 1, Transaction 2, Transaction 3]
Block 2: [Transaction 4, Transaction 5, Transaction 6]
Block 3: [Transaction 7, Transaction 8, Transaction 9]
...
```

Each block contains:
- **Transactions**: The actual data being recorded
- **Hash**: A unique fingerprint of the block
- **Previous Hash**: Link to the previous block
- **Timestamp**: When the block was created

### Ledger Properties

1. **Immutable**: Once written, cannot be changed
2. **Append-only**: New data is added, old data stays
3. **Distributed**: Multiple copies exist across the network
4. **Consensus**: Everyone agrees on the same ledger

## Smart Contract State

Smart contracts can store and manage data in two ways:

### 1. **Global State**
- **Shared by all users** of the contract
- **Persistent** across all transactions
- **Limited storage** (expensive to use)
- **Examples**: Total supply, contract owner, global settings

```python
# Global state example
class VotingContract:
    def __init__(self):
        # Global state - shared by everyone
        self.total_votes = 0
        self.voting_active = True
        self.contract_owner = "admin_address"
```

### 2. **Local State**
- **Specific to each user** (account)
- **Persistent** for that user
- **More storage** available per user
- **Examples**: User balance, voting history, preferences

```python
# Local state example
class VotingContract:
    def cast_vote(self, voter, choice):
        # Local state - specific to this voter
        self.voter_choice[voter] = choice
        self.voter_has_voted[voter] = True
```

## Transaction Flow

### Step 1: Transaction Creation
```
User creates transaction
↓
Transaction includes:
- Sender address
- Receiver address (contract address)
- Amount (if payment)
- Function call data
- Gas limit
```

### Step 2: Transaction Broadcasting
```
Transaction sent to network
↓
Network nodes receive transaction
↓
Transaction enters mempool (waiting area)
```

### Step 3: Block Creation
```
Validator selects transactions from mempool
↓
Creates new block with transactions
↓
Executes smart contracts in block
```

### Step 4: State Updates
```
Smart contract execution:
- Reads current state
- Processes transaction
- Updates state
- Returns result
```

### Step 5: Block Addition
```
Block added to blockchain
↓
State changes become permanent
↓
Transaction is confirmed
```

## Smart Contract Execution

### Execution Environment

Smart contracts run in a **virtual machine** (like a computer within a computer):

```
User Transaction
↓
Blockchain Network
↓
Virtual Machine (AVM)
↓
Smart Contract Code
↓
State Updates
↓
Result
```

### Execution Process

1. **Input Validation**
   - Check transaction format
   - Verify sender permissions
   - Validate input parameters

2. **State Reading**
   - Read current global state
   - Read relevant local state
   - Load contract code

3. **Code Execution**
   - Run contract logic
   - Process business rules
   - Calculate results

4. **State Writing**
   - Update global state
   - Update local state
   - Record changes

5. **Result Return**
   - Return success/failure
   - Provide error messages
   - Log events

## State Management Examples

### Example 1: Simple Counter Contract

```python
class CounterContract:
    def __init__(self):
        # Global state
        self.count = 0
        self.owner = None
    
    def initialize(self, owner):
        # Set contract owner (global state)
        self.owner = owner
    
    def increment(self, caller):
        # Check permissions
        if caller != self.owner:
            return False
        
        # Update global state
        self.count += 1
        return True
    
    def get_count(self):
        # Read global state
        return self.count
```

### Example 2: Token Contract

```python
class TokenContract:
    def __init__(self):
        # Global state
        self.total_supply = 1000000
        self.name = "MyToken"
        self.symbol = "MTK"
        
        # Local state (per user)
        self.balances = {}  # user_address -> balance
        self.allowances = {}  # user_address -> {spender: amount}
    
    def transfer(self, sender, recipient, amount):
        # Check sender balance (local state)
        if self.balances.get(sender, 0) < amount:
            return False
        
        # Update local state
        self.balances[sender] -= amount
        self.balances[recipient] = self.balances.get(recipient, 0) + amount
        
        return True
    
    def approve(self, owner, spender, amount):
        # Update local state
        if owner not in self.allowances:
            self.allowances[owner] = {}
        self.allowances[owner][spender] = amount
        
        return True
```

## Transaction Types

### 1. **Payment Transactions**
- Transfer ALGO between accounts
- Simple value transfer
- No smart contract execution

### 2. **Application Transactions**
- Call smart contract functions
- Execute contract logic
- Update contract state

### 3. **Asset Transactions**
- Create, transfer, or manage assets
- Algorand Standard Assets (ASAs)
- Custom token operations

### 4. **Atomic Transactions**
- Multiple transactions as one unit
- All succeed or all fail
- No partial execution

## Gas and Fees

### What is Gas?

Gas is the **computational cost** of executing smart contracts:

```
Simple operation = Low gas cost
Complex operation = High gas cost
```

### Gas Calculation

```python
# Example gas costs
def calculate_gas_cost(operation):
    costs = {
        'simple_math': 1,
        'state_read': 5,
        'state_write': 10,
        'complex_calculation': 50,
        'external_call': 100
    }
    return costs.get(operation, 1)

# Total gas = sum of all operations
total_gas = sum(calculate_gas_cost(op) for op in operations)
```

### Fee Structure

```
Transaction Fee = Base Fee + Gas Cost
```

- **Base Fee**: Fixed cost for transaction
- **Gas Cost**: Variable cost based on complexity
- **Priority Fee**: Optional fee for faster processing

## Error Handling

### Common Errors

1. **Insufficient Balance**
   - User doesn't have enough tokens
   - Contract doesn't have enough funds

2. **Invalid Parameters**
   - Wrong function arguments
   - Invalid data types

3. **Permission Denied**
   - Unauthorized access
   - Wrong caller

4. **State Conflicts**
   - Concurrent modifications
   - Race conditions

### Error Response

```python
def safe_contract_call(function, *args):
    try:
        result = function(*args)
        return {"success": True, "result": result}
    except InsufficientBalance:
        return {"success": False, "error": "Insufficient balance"}
    except InvalidParameter:
        return {"success": False, "error": "Invalid parameter"}
    except PermissionDenied:
        return {"success": False, "error": "Permission denied"}
    except Exception as e:
        return {"success": False, "error": str(e)}
```

## Event Logging

### What are Events?

Events are **notifications** that smart contracts can emit:

```python
class VotingContract:
    def cast_vote(self, voter, choice):
        # Process vote
        self.votes[voter] = choice
        
        # Emit event
        self.emit_event("VoteCast", {
            "voter": voter,
            "choice": choice,
            "timestamp": current_time()
        })
```

### Event Benefits

1. **Transparency**: Public record of contract activity
2. **Monitoring**: Track contract behavior
3. **Integration**: Connect with external systems
4. **Debugging**: Understand contract execution

## Best Practices

### 1. **State Management**
- Minimize global state usage
- Use local state when possible
- Optimize for gas efficiency

### 2. **Error Handling**
- Validate all inputs
- Handle edge cases
- Provide clear error messages

### 3. **Security**
- Check permissions
- Prevent reentrancy
- Validate external calls

### 4. **Testing**
- Test all code paths
- Test edge cases
- Test with different users

## Key Takeaways

- **Ledger** is the immutable, shared database
- **Global state** is shared by all users
- **Local state** is specific to each user
- **Transactions** trigger smart contract execution
- **Gas** is the computational cost
- **Events** provide transparency and monitoring
- **Error handling** is crucial for reliability

## Next Steps

Now that you understand smart contracts at a high level, let's explore:
1. **Smart Contracts in Algorand** - Algorand-specific features
2. **Stateless vs Stateful** - Different types of smart contracts

Understanding these concepts will help you build better smart contracts on Algorand!
