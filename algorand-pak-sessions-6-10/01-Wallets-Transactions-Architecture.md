# Wallets + Transactions + Architecture

## Table of Contents
1. [Introduction to Algorand Wallets](#introduction-to-algorand-wallets)
2. [Account Generation with algosdk](#account-generation-with-algosdk)
3. [Funding Wallets with TestNet Faucet](#funding-wallets-with-testnet-faucet)
4. [Understanding Transactions](#understanding-transactions)
5. [Transaction Lifecycle](#transaction-lifecycle)
6. [System Architecture](#system-architecture)
7. [Practical Examples](#practical-examples)

## Introduction to Algorand Wallets

### What is a Wallet?

A wallet in the Algorand ecosystem is a digital tool that allows users to:
- **Store cryptographic keys** (private keys, public keys)
- **Manage accounts** and addresses
- **Sign transactions** securely
- **Interact with dApps** (decentralized applications)
- **View account balances** and transaction history

### Types of Algorand Wallets

#### 1. **Pera Wallet (Mobile)**
- **Primary mobile wallet** for Algorand
- **User-friendly interface** for beginners
- **Built-in dApp browser** for seamless interactions
- **Biometric security** (fingerprint, face ID)
- **Multi-account support**

#### 2. **Defly Wallet (Mobile)**
- **Advanced trading features**
- **Portfolio tracking** and analytics
- **DEX integration** (Decentralized Exchange)
- **Professional trading tools**

#### 3. **algosdk Local Accounts (Programmatic)**
- **For developers** and automated systems
- **Generated programmatically** using algosdk
- **Full control** over private keys
- **Integration with applications**

### Wallet Security Concepts

#### Private Keys
- **256-bit cryptographic key** that proves ownership
- **Never share** with anyone
- **Used to sign transactions** and prove identity
- **If lost, account is permanently inaccessible**

#### Public Keys & Addresses
- **Derived from private key** using cryptographic functions
- **Safe to share** publicly
- **Used to receive funds** and identify accounts
- **Algorand addresses start with 'A'** and are 58 characters long

## Account Generation with algosdk

### Understanding Account Structure

An Algorand account consists of:
- **Private Key**: 32 bytes (256 bits)
- **Public Key**: 32 bytes (256 bits) 
- **Address**: 58-character string derived from public key

### Basic Account Generation

```python
from algosdk import account, mnemonic

# Generate a new account
private_key, address = account.generate_account()

# Convert private key to mnemonic (24 words)
mnemonic_phrase = mnemonic.from_private_key(private_key)

print(f"Address: {address}")
print(f"Private Key: {private_key}")
print(f"Mnemonic: {mnemonic_phrase}")
```

### Account Recovery

```python
# Recover account from mnemonic
recovered_private_key = mnemonic.to_private_key(mnemonic_phrase)
recovered_address = account.address_from_private_key(recovered_private_key)
```

### Account Validation

```python
from algosdk import encoding

# Validate if address is correct
is_valid = encoding.is_valid_address(address)
print(f"Address is valid: {is_valid}")
```

## Funding Wallets with TestNet Faucet

### What is TestNet?

TestNet is Algorand's **testing environment** where:
- **No real money** is involved
- **Free test tokens** (ALGOs) are available
- **Same functionality** as MainNet
- **Safe for development** and experimentation

### TestNet Faucet Usage

#### 1. **Official Algorand TestNet Faucet**
- **URL**: https://testnet.algoexplorer.io/dispenser
- **Free 10 ALGO** per day per address
- **No registration required**
- **Instant funding**

#### 2. **Alternative Faucets**
- **Algorand Foundation Faucet**
- **Community-run faucets**
- **Higher limits** for verified developers

### Faucet Integration in Code

```python
import requests
from algosdk.v2client import algod

# TestNet configuration
ALGOD_TOKEN = ""  # No token needed for TestNet
ALGOD_ADDRESS = "https://testnet-api.algonode.cloud"

# Initialize client
client = algod.AlgodClient(ALGOD_TOKEN, ALGOD_ADDRESS)

def fund_account_with_faucet(address):
    """Request funding from TestNet faucet"""
    try:
        response = requests.post(
            "https://testnet.algoexplorer.io/api/v1/faucet",
            json={"address": address}
        )
        if response.status_code == 200:
            print(f"Funding request successful for {address}")
            return True
        else:
            print(f"Funding failed: {response.text}")
            return False
    except Exception as e:
        print(f"Error requesting funding: {e}")
        return False
```

## Understanding Transactions

### What is a Transaction?

A transaction in Algorand is a **cryptographic message** that:
- **Transfers value** (ALGOs, ASAs)
- **Calls smart contracts**
- **Modifies blockchain state**
- **Requires digital signature** for authorization

### Transaction Types

#### 1. **Payment Transactions**
- **Transfer ALGOs** between accounts
- **Most common** transaction type
- **Required for** all value transfers

#### 2. **Asset Transfer Transactions**
- **Transfer ASAs** (tokens, NFTs)
- **Requires opt-in** for receiving account
- **Supports** fractional amounts

#### 3. **Application Call Transactions**
- **Interact with smart contracts**
- **Deploy applications**
- **Call contract methods**

#### 4. **Asset Configuration Transactions**
- **Create ASAs**
- **Modify asset parameters**
- **Freeze/unfreeze assets**

### Transaction Parameters

#### Essential Parameters
- **Sender**: Account initiating the transaction
- **Receiver**: Account receiving the value
- **Amount**: Quantity to transfer
- **Fee**: Transaction fee (minimum 0.001 ALGO)
- **First Valid**: First round when transaction is valid
- **Last Valid**: Last round when transaction is valid

#### Optional Parameters
- **Note**: Additional data (up to 1000 bytes)
- **Close Remainder To**: Close account and send remaining balance
- **Rekey To**: Change account's spending key

### Transaction Fees

#### Fee Structure
- **Minimum fee**: 0.001 ALGO
- **Fee per byte**: 0.0001 ALGO
- **Priority fee**: Additional fee for faster processing
- **Total fee**: Base fee + (size × per-byte fee) + priority fee

#### Fee Calculation Example
```python
def calculate_transaction_fee(tx_size_bytes, priority_fee=0):
    """Calculate transaction fee"""
    base_fee = 1000  # 0.001 ALGO in microALGOs
    per_byte_fee = 1  # 0.000001 ALGO per byte
    return base_fee + (tx_size_bytes * per_byte_fee) + priority_fee
```

## Transaction Lifecycle

### 1. **Prepare Phase**
- **Create transaction object** with all parameters
- **Set validity window** (first valid, last valid rounds)
- **Calculate appropriate fee**
- **Validate all parameters**

### 2. **Sign Phase**
- **Use private key** to create digital signature
- **Prove ownership** of the account
- **Ensure transaction integrity**
- **Cannot be modified** after signing

### 3. **Send Phase**
- **Submit to network** via algod node
- **Broadcast to validators**
- **Enter mempool** (pending transactions)
- **Wait for inclusion** in block

### 4. **Confirm Phase**
- **Validators verify** transaction
- **Include in block** if valid
- **Update account balances**
- **Transaction becomes final**

### Transaction States

#### Pending
- **Submitted to network**
- **Waiting for validation**
- **Can be cancelled** (if not yet included)

#### Confirmed
- **Included in block**
- **Permanently recorded**
- **Cannot be reversed**
- **Balances updated**

#### Failed
- **Invalid parameters**
- **Insufficient funds**
- **Expired validity window**
- **Rejected by network**

## System Architecture

### High-Level Architecture

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   Wallet    │◄──►│  Frontend   │◄──►│  Backend    │◄──►│  Blockchain │
│  (Pera/     │    │   (Web/     │    │  (Node.js/  │    │  (Algorand  │
│  Defly)     │    │   Mobile)   │    │  Python)    │    │  Network)   │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
```

### Component Interactions

#### 1. **Wallet ↔ Frontend**
- **Wallet Connect** protocol
- **Transaction signing** requests
- **Account information** sharing
- **User authentication**

#### 2. **Frontend ↔ Backend**
- **API calls** for data
- **Transaction preparation**
- **User interface** updates
- **Error handling**

#### 3. **Backend ↔ Blockchain**
- **algod client** connections
- **Transaction submission**
- **State queries**
- **Event monitoring**

#### 4. **Blockchain ↔ Smart Contracts**
- **Contract deployment**
- **Method calls**
- **State updates**
- **Event emission**

### Data Flow Example

#### Sending ALGOs
1. **User initiates** transfer in frontend
2. **Frontend prepares** transaction parameters
3. **Wallet signs** transaction with private key
4. **Backend submits** signed transaction to network
5. **Blockchain validates** and includes in block
6. **Frontend updates** UI with new balances

#### Smart Contract Interaction
1. **User triggers** contract method
2. **Frontend calls** backend API
3. **Backend prepares** application call transaction
4. **Wallet signs** transaction
5. **Transaction submitted** to network
6. **Contract executes** and updates state
7. **Frontend reflects** new state

## Practical Examples

### Example 1: Basic Payment Transaction

```python
from algosdk import transaction, account
from algosdk.v2client import algod

def create_payment_transaction(sender, receiver, amount, private_key):
    """Create and send a payment transaction"""
    
    # Initialize client
    client = algod.AlgodClient("", "https://testnet-api.algonode.cloud")
    
    # Get suggested parameters
    params = client.suggested_params()
    
    # Create transaction
    txn = transaction.PaymentTxn(
        sender=sender,
        sp=params,
        receiver=receiver,
        amt=amount,
        note="Payment transaction example"
    )
    
    # Sign transaction
    signed_txn = txn.sign(private_key)
    
    # Submit transaction
    txid = client.send_transaction(signed_txn)
    
    # Wait for confirmation
    confirmed_txn = transaction.wait_for_confirmation(client, txid, 4)
    
    return confirmed_txn
```

### Example 2: Account Balance Check

```python
def check_account_balance(address):
    """Check account balance and information"""
    
    client = algod.AlgodClient("", "https://testnet-api.algonode.cloud")
    
    try:
        account_info = client.account_info(address)
        balance = account_info.get('amount', 0)
        
        print(f"Account: {address}")
        print(f"Balance: {balance / 1000000} ALGO")  # Convert from microALGOs
        print(f"Assets: {len(account_info.get('assets', []))}")
        
        return account_info
    except Exception as e:
        print(f"Error checking balance: {e}")
        return None
```

### Example 3: Transaction History

```python
def get_transaction_history(address, limit=10):
    """Get recent transaction history for an account"""
    
    client = algod.AlgodClient("", "https://testnet-api.algonode.cloud")
    
    try:
        # Get account transactions
        transactions = client.account_transactions(address, limit=limit)
        
        print(f"Recent transactions for {address}:")
        for txn in transactions['transactions']:
            print(f"ID: {txn['id']}")
            print(f"Type: {txn['tx-type']}")
            print(f"Round: {txn['confirmed-round']}")
            print(f"Amount: {txn.get('amount', 0) / 1000000} ALGO")
            print("---")
            
        return transactions
    except Exception as e:
        print(f"Error getting transaction history: {e}")
        return None
```

## Best Practices

### Security
- **Never share private keys**
- **Use hardware wallets** for large amounts
- **Verify addresses** before sending
- **Keep software updated**

### Development
- **Test on TestNet** first
- **Handle errors gracefully**
- **Implement proper logging**
- **Use proper fee estimation**

### User Experience
- **Clear error messages**
- **Transaction status updates**
- **Confirmation dialogs**
- **Loading indicators**

## Summary

This session covered the fundamental concepts of Algorand wallets, transactions, and system architecture. Understanding these concepts is crucial for building applications on Algorand, as they form the foundation for all blockchain interactions.

Key takeaways:
- **Wallets** are essential for managing accounts and signing transactions
- **Transactions** are the primary way to interact with the blockchain
- **Architecture** understanding helps in building robust applications
- **Security** should always be a top priority
- **TestNet** provides a safe environment for development

In the next session, we'll explore Algorand Standard Assets (ASAs) and how to create tokens and NFTs on the Algorand blockchain.
