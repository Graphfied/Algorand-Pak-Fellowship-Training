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

PyTeal smart contracts follow a consistent structure:

- **Import Statements**: Importing necessary PyTeal modules and functions
- **Approval Program**: Main contract logic that validates transactions
- **Clear Program**: Cleanup logic for when users opt out
- **Compilation Process**: Converting PyTeal code to TEAL bytecode
- **Mode Specification**: Defining whether it's an application or signature program
- **Output Generation**: Producing TEAL code for deployment

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

PyTeal supports standard arithmetic operations:

- **Addition**: Combining numeric values
- **Subtraction**: Calculating differences between values
- **Multiplication**: Scaling values by factors
- **Division**: Splitting values into parts
- **Modulo**: Finding remainders after division

#### Comparison Operators

Comparison operations enable conditional logic:

- **Equality**: Checking if values are identical
- **Inequality**: Verifying values are different
- **Greater Than**: Comparing magnitude relationships
- **Less Than**: Establishing ordering relationships
- **Greater Than or Equal**: Inclusive comparison operations
- **Less Than or Equal**: Inclusive ordering operations

#### Logical Operators

Logical operations enable complex decision making:

- **Logical AND**: Requiring multiple conditions to be true
- **Logical OR**: Allowing alternative conditions
- **Logical NOT**: Inverting boolean values
- **Conditional**: Implementing if-then-else logic

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

Multi-signature wallets provide enhanced security through:

- **Signature Requirements**: Defining minimum number of signatures needed
- **Signer Validation**: Verifying that required signers have authorized the transaction
- **Threshold Logic**: Implementing flexible signature requirements
- **Security Enhancement**: Reducing single points of failure
- **Access Control**: Managing permissions across multiple parties

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

Stateful counter contracts demonstrate persistent state management:

- **State Retrieval**: Accessing current counter values from global state
- **Value Modification**: Incrementing or decrementing counter values
- **State Persistence**: Storing updated values for future transactions
- **Transaction Sequencing**: Ensuring proper order of operations
- **State Validation**: Verifying counter values before modifications

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

Approval programs follow a structured approach to handle different transaction types:

- **Transaction Type Detection**: Identifying the specific type of transaction being processed
- **Route Management**: Directing transactions to appropriate handlers
- **Creation Handling**: Managing application deployment and initialization
- **Opt-in Processing**: Handling user enrollment in the application
- **Close-out Management**: Processing user opt-out and cleanup
- **Update Handling**: Managing application upgrades and modifications
- **Deletion Processing**: Handling application removal and finalization
- **No-op Operations**: Processing regular application interactions

### Transaction Type Handlers

#### 1. **Application Creation**

Application creation involves several key steps:

- **Global State Initialization**: Setting up application-wide parameters and settings
- **Creator Assignment**: Recording the application creator for future reference
- **Parameter Configuration**: Establishing initial values for application variables
- **Permission Setup**: Defining access controls and authorization rules
- **Validation Logic**: Ensuring creation parameters are valid and appropriate

#### 2. **Opt-in Handling**

User opt-in processing requires careful state management:

- **Local State Initialization**: Creating user-specific state variables
- **Permission Assignment**: Granting appropriate access rights to the user
- **Balance Setup**: Initializing user balances and holdings
- **Status Tracking**: Recording user enrollment status
- **Validation Checks**: Ensuring user meets opt-in requirements

#### 3. **No-Op Handling**

Regular transaction processing involves method routing:

- **Method Identification**: Determining which application method to execute
- **Argument Processing**: Extracting and validating method parameters
- **Route Management**: Directing to appropriate method handlers
- **State Updates**: Modifying application state based on method execution
- **Result Processing**: Handling method outcomes and responses

### Common Approval Patterns

#### 1. **Authorization Checks**

Authorization validation ensures proper access control:

- **Creator Verification**: Confirming the transaction sender is the application creator
- **Opt-in Status**: Verifying the user has properly enrolled in the application
- **Permission Levels**: Checking if the user has required permissions for the operation
- **Role-based Access**: Implementing different access levels for different user types
- **Time-based Authorization**: Considering temporal aspects of permissions

#### 2. **Balance Validation**

Balance checks prevent insufficient fund transactions:

- **Current Balance Retrieval**: Accessing user's current balance from local state
- **Amount Verification**: Ensuring the requested amount is available
- **Overflow Protection**: Preventing balance calculations that exceed limits
- **Precision Handling**: Managing decimal places and rounding appropriately
- **Locked Balance**: Considering any frozen or locked funds

#### 3. **Supply Validation**

Supply validation maintains token economics:

- **Total Supply Limits**: Ensuring operations don't exceed maximum supply
- **Current Supply Tracking**: Monitoring actual tokens in circulation
- **Minting Restrictions**: Controlling new token creation
- **Burn Validation**: Verifying burn operations don't exceed available supply
- **Economic Constraints**: Maintaining token value and scarcity

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

Global state management involves several key operations:

- **State Setting**: Storing values in global state with appropriate keys
- **State Retrieval**: Accessing values from global state for processing
- **State Deletion**: Removing unnecessary global state entries
- **Existence Checking**: Verifying whether specific keys exist in global state
- **Type Management**: Handling different data types in global state

#### Example: Token Contract Global State

Token contract global state typically includes:

- **Token Metadata**: Name, symbol, and decimal information
- **Supply Management**: Total supply and current circulation tracking
- **Creator Information**: Recording the token creator for administrative purposes
- **Contract Status**: Pause/unpause states and operational flags
- **Permission Settings**: Minting, burning, and transfer permissions
- **Economic Parameters**: Fee structures and economic constraints

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

Local state management focuses on user-specific data:

- **User State Setting**: Storing values specific to individual users
- **User State Retrieval**: Accessing user-specific data for processing
- **User State Deletion**: Removing user-specific state entries
- **User State Validation**: Verifying user state existence and validity
- **Privacy Management**: Ensuring user data remains private and secure

#### Example: User Balance Management

User balance management involves several key aspects:

- **Balance Initialization**: Setting up initial user balances and holdings
- **Status Tracking**: Recording user enrollment and participation status
- **Preference Management**: Storing user-specific settings and preferences
- **Permission States**: Managing user access levels and restrictions
- **Activity Logging**: Tracking user interactions and transaction history

### State Management Best Practices

#### 1. **Key Naming**

Effective key naming strategies include:

- **Descriptive Names**: Using clear, meaningful names for state keys
- **Consistent Patterns**: Following established naming conventions
- **Namespace Management**: Organizing keys by functionality or scope
- **Documentation**: Maintaining clear documentation of key purposes
- **Version Control**: Managing key changes across contract versions

#### 2. **State Validation**

State validation ensures data integrity:

- **Opt-in Verification**: Confirming user enrollment before state access
- **Contract Status**: Checking application operational status
- **Permission Validation**: Verifying user has required permissions
- **Data Integrity**: Ensuring state values are within expected ranges
- **Consistency Checks**: Validating state relationships and dependencies

#### 3. **State Cleanup**

State cleanup maintains system efficiency:

- **User Opt-out**: Removing user-specific state when users leave
- **Resource Management**: Freeing up storage space efficiently
- **Data Privacy**: Ensuring user data is properly removed
- **State Consistency**: Maintaining global state integrity during cleanup
- **Transaction Approval**: Confirming cleanup operations complete successfully

## Writing Basic Approval Logic

### Example 1: Simple Counter Contract

A simple counter contract demonstrates basic smart contract concepts:

- **Contract Structure**: Organizing code into logical functions and handlers
- **State Management**: Maintaining both global and local state variables
- **Transaction Routing**: Directing different transaction types to appropriate handlers
- **Access Control**: Implementing creator-only operations and user permissions
- **State Operations**: Incrementing, decrementing, and resetting counter values
- **User Tracking**: Recording individual user interactions with the contract
- **Validation Logic**: Ensuring operations are performed correctly and safely

### Example 2: Minimum Payment Rule

Minimum payment rules enforce economic constraints:

- **Transaction Type Validation**: Ensuring only payment transactions are processed
- **Amount Verification**: Checking that payments meet minimum thresholds
- **Economic Logic**: Implementing business rules for transaction approval
- **Security Enhancement**: Preventing dust attacks and spam transactions
- **Fee Optimization**: Encouraging efficient transaction batching

### Example 3: Multi-signature Logic

Multi-signature logic provides enhanced security:

- **Signer Definition**: Establishing authorized signers for transactions
- **Signature Validation**: Verifying that required signers have authorized the transaction
- **Flexible Authorization**: Supporting different signature requirements for different operations
- **Security Enhancement**: Reducing single points of failure in transaction authorization
- **Access Control**: Implementing sophisticated permission systems

## Practical Applications

### Example 1: Simple Token Contract

Token contracts implement digital asset functionality:

- **Token Creation**: Establishing token parameters and initial supply
- **User Management**: Handling user opt-in and opt-out processes
- **Balance Tracking**: Monitoring user balances and token circulation
- **Transfer Operations**: Enabling secure token transfers between users
- **Minting Control**: Managing token creation and supply expansion
- **Access Control**: Implementing appropriate permissions for different operations

### Example 2: Escrow Contract

Escrow contracts facilitate secure transactions:

- **Multi-party Management**: Coordinating between buyers, sellers, and arbitrators
- **Deposit Handling**: Securing funds in escrow with proper validation
- **Release Mechanisms**: Enabling authorized fund release to appropriate parties
- **Dispute Resolution**: Managing conflict resolution through arbitration
- **Status Tracking**: Monitoring transaction states throughout the process
- **Security Measures**: Ensuring funds are protected until proper resolution

## Best Practices

### 1. **Code Organization**

#### Use Functions

Effective code organization involves:

- **Modular Design**: Breaking complex logic into smaller, manageable functions
- **Function Naming**: Using descriptive names that clearly indicate purpose
- **Parameter Management**: Designing functions with clear input and output parameters
- **Reusability**: Creating functions that can be used in multiple contexts
- **Documentation**: Providing clear documentation for each function

#### Use Constants

Constant management improves code maintainability:

- **Centralized Definition**: Defining all constants in a single location
- **Descriptive Names**: Using clear, meaningful names for constants
- **Type Consistency**: Ensuring constants are properly typed
- **Scope Management**: Organizing constants by functionality or scope
- **Version Control**: Managing constant changes across contract versions

#### Use Comments

Effective commenting enhances code understanding:

- **Purpose Documentation**: Explaining what each function does
- **Parameter Descriptions**: Documenting input and output parameters
- **Logic Explanation**: Clarifying complex business logic
- **Assumption Documentation**: Recording important assumptions and constraints
- **Update Maintenance**: Keeping comments current with code changes

### 2. **Error Handling**

#### Use Assertions

Assertion-based error handling provides:

- **Precondition Validation**: Checking that required conditions are met before processing
- **Input Verification**: Ensuring transaction parameters are valid and appropriate
- **State Validation**: Confirming application state is consistent and correct
- **Security Checks**: Preventing unauthorized or malicious operations
- **Fail-fast Behavior**: Stopping execution immediately when errors are detected

#### Use Conditional Logic

Conditional error handling enables:

- **Flexible Responses**: Different error handling for different situations
- **Graceful Degradation**: Providing alternative paths when primary operations fail
- **User Experience**: Offering meaningful feedback for different error conditions
- **Debugging Support**: Making it easier to identify and resolve issues
- **Recovery Mechanisms**: Implementing fallback strategies when possible

#### Use Reject for Errors

Transaction rejection provides:

- **Clear Failure Indication**: Explicitly signaling that operations cannot proceed
- **Resource Protection**: Preventing invalid operations from consuming resources
- **Security Enforcement**: Blocking unauthorized or malicious transactions
- **State Preservation**: Maintaining application integrity when operations fail
- **User Notification**: Providing clear feedback about why transactions were rejected

### 3. **State Management**

#### Initialize State Properly

Proper state initialization ensures:

- **Complete Setup**: All required state variables are properly initialized
- **Default Values**: Appropriate default values are set for all state variables
- **Type Consistency**: State variables are initialized with correct data types
- **Validation**: Initial values are validated before being stored
- **Documentation**: Clear documentation of what each state variable represents

#### Clean Up State

State cleanup maintains system efficiency:

- **User Opt-out**: Properly removing user-specific state when users leave
- **Resource Management**: Freeing up storage space efficiently
- **Data Privacy**: Ensuring user data is completely removed
- **State Consistency**: Maintaining global state integrity during cleanup
- **Validation**: Confirming cleanup operations complete successfully

### 4. **Testing**

#### Test All Paths

Comprehensive testing involves:

- **Code Path Coverage**: Testing every possible execution path through the contract
- **Edge Case Testing**: Verifying behavior under extreme or unusual conditions
- **Error Condition Testing**: Ensuring proper handling of all error scenarios
- **State Transition Testing**: Validating all possible state changes
- **Integration Testing**: Testing interactions between different contract functions

#### Use Logging

Effective logging provides:

- **Debug Information**: Recording important values and state during execution
- **Transaction Tracking**: Monitoring transaction flow and decision points
- **Error Diagnosis**: Providing detailed information when issues occur
- **Performance Monitoring**: Tracking execution time and resource usage
- **Audit Trail**: Creating records of important contract operations

### 5. **Security**

#### Validate Inputs

Input validation is crucial for security:

- **Argument Validation**: Checking that all required arguments are present and valid
- **Type Checking**: Ensuring arguments are of the expected data types
- **Range Validation**: Verifying that numeric values are within acceptable ranges
- **Format Validation**: Checking that string arguments follow expected formats
- **Length Validation**: Ensuring arguments don't exceed maximum length limits

#### Check Authorization

Authorization checks prevent unauthorized access:

- **Permission Verification**: Confirming users have required permissions for operations
- **Role-based Access**: Implementing different access levels for different user types
- **Creator Privileges**: Ensuring only authorized users can perform administrative operations
- **Time-based Authorization**: Considering temporal aspects of permissions
- **Multi-signature Support**: Implementing complex authorization schemes

#### Prevent Integer Overflow

Overflow protection maintains data integrity:

- **Pre-calculation Validation**: Checking for overflow before performing arithmetic operations
- **Range Checking**: Ensuring results stay within acceptable numeric ranges
- **Safe Arithmetic**: Using overflow-safe arithmetic operations where possible
- **Boundary Testing**: Testing edge cases where overflow might occur
- **Error Handling**: Providing appropriate responses when overflow is detected

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
