# Stateless vs Stateful Smart Contracts

Understanding the difference between stateless and stateful smart contracts is crucial for Algorand development. Let's explore their characteristics, use cases, and when to use each type.

## Quick Comparison

| Feature | Stateless | Stateful |
|---------|-----------|----------|
| **Data Storage** | None | Global + Local |
| **Complexity** | Simple | Complex |
| **Cost** | Very Low | Higher |
| **Speed** | Very Fast | Fast |
| **Use Cases** | Validation, Signatures | Applications, DApps |
| **State** | No persistent state | Persistent state |

## Stateless Smart Contracts (Logic Signatures)

### What Are They?

Stateless smart contracts are **pure validation logic** that approve or reject transactions without storing any data.

**Think of them as "smart signatures"** - they're like having a very smart signature that can check conditions before approving a transaction.

### Characteristics

#### ✅ **Advantages**
- **No state storage** - Cannot store data
- **Lightweight** - Very fast execution
- **Cheap** - Minimal transaction costs
- **Simple** - Easy to understand and deploy
- **Secure** - Limited attack surface

#### ❌ **Limitations**
- **No memory** - Cannot remember previous transactions
- **Limited logic** - Simple validation only
- **No data persistence** - Cannot store information
- **Account-bound** - Attached to specific accounts

### How They Work

```
User Transaction
↓
Stateless Contract (Logic Signature)
↓
Validation Logic
↓
Approve or Reject
```

### Use Cases

#### 1. **Multi-Signature Wallets**
```python
# Require 2 out of 3 signatures
def multi_sig_wallet():
    # Check if transaction is valid
    return And(
        Txn.amount() <= Int(1000000),  # Max 1 ALGO
        Txn.receiver() == Addr("RECIPIENT_ADDRESS"),
        # Additional signature validation would go here
        Int(1)  # Simplified for example
    )
```

#### 2. **Time-Locked Transactions**
```python
# Only allow withdrawal after specific time
def time_locked_payment():
    return And(
        Global.latest_timestamp() > Int(1640995200),  # After Jan 1, 2022
        Txn.amount() <= Int(1000000),  # Max 1 ALGO
        Txn.receiver() == Addr("BENEFICIARY_ADDRESS")
    )
```

#### 3. **Conditional Payments**
```python
# Pay only if specific conditions are met
def conditional_payment():
    return And(
        # Check if recipient has specific asset
        AssetHolding.balance(Int(0), Int(ASSET_ID)) > Int(0),
        # Check if amount is within limits
        Txn.amount() <= Int(500000),  # Max 0.5 ALGO
        # Check if transaction is from authorized sender
        Txn.sender() == Addr("AUTHORIZED_SENDER")
    )
```

#### 4. **Atomic Swaps**
```python
# Exchange assets without intermediaries
def atomic_swap():
    return And(
        # Check if swap conditions are met
        Txn.amount() == Int(1000000),  # Exact amount
        Txn.receiver() == Addr("SWAP_PARTNER"),
        # Additional swap validation logic
        Int(1)
    )
```

### Real-World Example: Escrow Service

```python
def escrow_contract():
    """
    Simple escrow that releases funds after time delay
    """
    return And(
        # Only allow withdrawal after 30 days
        Global.latest_timestamp() > App.globalGet(Bytes("release_time")),
        # Only allow specific amount
        Txn.amount() <= App.globalGet(Bytes("escrow_amount")),
        # Only allow specific recipient
        Txn.receiver() == App.globalGet(Bytes("beneficiary"))
    )
```

## Stateful Smart Contracts (Applications)

### What Are They?

Stateful smart contracts are **full applications** that can store data, maintain state, and execute complex logic.

**Think of them as "smart applications"** - they're like having a full application running on the blockchain that can remember things and interact with users.

### Characteristics

#### ✅ **Advantages**
- **State storage** - Can store global and local state
- **Complex logic** - Full programming capabilities
- **Data persistence** - Information survives between transactions
- **User interaction** - Multiple users can interact
- **Rich functionality** - Build complex applications

#### ❌ **Limitations**
- **Higher cost** - More expensive to execute
- **Slower** - More complex execution
- **More complex** - Harder to develop and debug
- **State management** - Need to manage data carefully

### How They Work

```
User Transaction
↓
Stateful Contract (Application)
↓
Read Current State
↓
Execute Logic
↓
Update State
↓
Return Result
```

### Use Cases

#### 1. **DeFi Protocols**
```python
# Lending protocol
def lending_contract():
    # Global state
    total_liquidity = App.globalGet(Bytes("total_liquidity"))
    interest_rate = App.globalGet(Bytes("interest_rate"))
    
    # Local state (per user)
    user_balance = App.localGet(Int(0), Bytes("balance"))
    user_debt = App.localGet(Int(0), Bytes("debt"))
    
    # Lending logic
    if Txn.application_args[0] == Bytes("deposit"):
        return deposit_liquidity()
    elif Txn.application_args[0] == Bytes("borrow"):
        return borrow_funds()
    elif Txn.application_args[0] == Bytes("repay"):
        return repay_loan()
    else:
        return Int(0)  # Reject
```

#### 2. **NFT Marketplaces**
```python
# NFT trading platform
def nft_marketplace():
    # Global state
    total_nfts = App.globalGet(Bytes("total_nfts"))
    marketplace_fee = App.globalGet(Bytes("marketplace_fee"))
    
    # Local state (per user)
    user_nfts = App.localGet(Int(0), Bytes("nft_count"))
    user_listings = App.localGet(Int(0), Bytes("active_listings"))
    
    # Marketplace logic
    if Txn.application_args[0] == Bytes("mint"):
        return mint_nft()
    elif Txn.application_args[0] == Bytes("list"):
        return list_nft()
    elif Txn.application_args[0] == Bytes("buy"):
        return buy_nft()
    else:
        return Int(0)  # Reject
```

#### 3. **Gaming Applications**
```python
# Simple game with in-game assets
def game_contract():
    # Global state
    game_state = App.globalGet(Bytes("game_state"))
    total_players = App.globalGet(Bytes("total_players"))
    
    # Local state (per player)
    player_level = App.localGet(Int(0), Bytes("level"))
    player_score = App.localGet(Int(0), Bytes("score"))
    player_items = App.localGet(Int(0), Bytes("item_count"))
    
    # Game logic
    if Txn.application_args[0] == Bytes("join"):
        return join_game()
    elif Txn.application_args[0] == Bytes("play"):
        return play_game()
    elif Txn.application_args[0] == Bytes("claim_reward"):
        return claim_reward()
    else:
        return Int(0)  # Reject
```

#### 4. **Governance Systems**
```python
# Voting and decision making
def governance_contract():
    # Global state
    voting_active = App.globalGet(Bytes("voting_active"))
    total_votes = App.globalGet(Bytes("total_votes"))
    proposal_count = App.globalGet(Bytes("proposal_count"))
    
    # Local state (per voter)
    has_voted = App.localGet(Int(0), Bytes("has_voted"))
    vote_choice = App.localGet(Int(0), Bytes("vote_choice"))
    
    # Governance logic
    if Txn.application_args[0] == Bytes("create_proposal"):
        return create_proposal()
    elif Txn.application_args[0] == Bytes("vote"):
        return cast_vote()
    elif Txn.application_args[0] == Bytes("execute"):
        return execute_proposal()
    else:
        return Int(0)  # Reject
```

### Real-World Example: Simple Voting System

```python
def voting_system():
    """
    Complete voting system with state management
    """
    # Handle different transaction types
    return Cond(
        [Txn.application_id() == Int(0), on_creation()],
        [Txn.on_completion() == OnComplete.NoOp, on_noop()],
        [Txn.on_completion() == OnComplete.OptIn, on_opt_in()]
    )

def on_creation():
    # Initialize global state
    return Seq([
        App.globalPut(Bytes("voting_active"), Int(1)),
        App.globalPut(Bytes("yes_votes"), Int(0)),
        App.globalPut(Bytes("no_votes"), Int(0)),
        App.globalPut(Bytes("total_voters"), Int(0)),
        Return(Int(1))
    ])

def on_opt_in():
    # User joins voting system
    return Seq([
        App.localPut(Int(0), Bytes("has_voted"), Int(0)),
        App.globalPut(Bytes("total_voters"), 
                     App.globalGet(Bytes("total_voters")) + Int(1)),
        Return(Int(1))
    ])

def on_noop():
    # Handle voting
    if Txn.application_args[0] == Bytes("vote"):
        return cast_vote()
    elif Txn.application_args[0] == Bytes("get_results"):
        return get_results()
    else:
        return Int(0)

def cast_vote():
    # Check if user can vote
    has_voted = App.localGet(Int(0), Bytes("has_voted"))
    voting_active = App.globalGet(Bytes("voting_active"))
    
    return Seq([
        Assert(has_voted == Int(0)),  # User hasn't voted
        Assert(voting_active == Int(1)),  # Voting is active
        
        # Record vote
        App.localPut(Int(0), Bytes("has_voted"), Int(1)),
        App.localPut(Int(0), Bytes("vote_choice"), Txn.application_args[1]),
        
        # Update global counts
        If(Txn.application_args[1] == Bytes("yes"),
           App.globalPut(Bytes("yes_votes"), 
                        App.globalGet(Bytes("yes_votes")) + Int(1)),
           App.globalPut(Bytes("no_votes"), 
                        App.globalGet(Bytes("no_votes")) + Int(1))
        ),
        Return(Int(1))
    ])
```

## When to Use Each Type

### Use Stateless When:
- ✅ **Simple validation** is needed
- ✅ **No data storage** required
- ✅ **Cost is critical** (very low fees)
- ✅ **Speed is important** (fast execution)
- ✅ **Account-specific** logic
- ✅ **Multi-signature** requirements
- ✅ **Time-based** conditions
- ✅ **Atomic swaps** or simple exchanges

### Use Stateful When:
- ✅ **Data storage** is needed
- ✅ **Complex logic** required
- ✅ **Multiple users** interact
- ✅ **State persistence** is important
- ✅ **Rich functionality** needed
- ✅ **DeFi protocols** or DApps
- ✅ **Gaming** applications
- ✅ **Governance** systems

## Hybrid Approach

Sometimes you can use **both types together**:

```python
# Stateful contract for main logic
def main_application():
    # Complex state management
    # User interactions
    # Data storage
    pass

# Stateless contract for validation
def validation_logic():
    # Simple validation
    # Time-based conditions
    # Signature requirements
    pass
```

## Development Considerations

### Stateless Development
- **Keep it simple** - Focus on validation logic
- **Test thoroughly** - No state to debug
- **Optimize for gas** - Every operation counts
- **Handle edge cases** - Limited error handling

### Stateful Development
- **Plan state structure** - Design data models
- **Handle state transitions** - Manage state changes
- **Test state scenarios** - Test different states
- **Optimize state usage** - State is expensive

## Key Takeaways

- **Stateless contracts** are lightweight and fast, perfect for validation
- **Stateful contracts** are powerful and flexible, perfect for applications
- **Choose based on needs** - Simple validation vs complex functionality
- **Consider costs** - Stateless is cheaper, stateful is more expensive
- **Plan carefully** - Stateful requires more planning and testing
- **Both have their place** - Use the right tool for the job

## Next Steps

Now that you understand the difference between stateless and stateful smart contracts, let's explore:
1. **Python Basics** - Essential Python concepts for blockchain development
2. **Algorand Python** - How Python works specifically on Algorand

Understanding these concepts will help you choose the right type of smart contract for your project!
