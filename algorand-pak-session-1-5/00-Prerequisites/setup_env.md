# AlgoKit Development Environment Setup

This guide will help you set up AlgoKit, the official Algorand development toolkit that provides a simple, one-stop tool for building and launching secure, automated, production-ready decentralized applications on the Algorand protocol.

## What is AlgoKit?

AlgoKit is a comprehensive development toolkit that features:
- **Native Python Support**: Write Algorand smart contracts in regular Python
- **Smart Contract Templates**: Library of templates to kickstart your build
- **Local Development**: All necessary application infrastructure running locally
- **Toolchain Integrations**: Support for Python and TypeScript
- **Simplified Frontend Design**: Easy-to-use development experience

## Step 0: Project Setup and Environment Choice

Before installing AlgoKit, you need to set up your development workspace. You have two main options:

### Option A: Windows with WSL (Recommended for Windows Users)

**Why WSL?**
- Better compatibility with Linux-based development tools
- Improved performance for Docker and containerized applications
- Native Linux environment for Algorand development
- Better terminal experience and package management

### Option B: Native Windows/macOS/Linux

- Direct installation on your operating system
- Simpler setup but may have compatibility issues on Windows

## Step 0A: WSL Setup (Windows Users)

### Install WSL 2

1. **Open PowerShell as Administrator** and run:
```powershell
# Enable WSL feature
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart

# Enable Virtual Machine Platform
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart

# Restart your computer
```

2. **After restart, set WSL 2 as default**:
```powershell
wsl --set-default-version 2
```

3. **Install Ubuntu from Microsoft Store**:
   - Open Microsoft Store
   - Search for "Ubuntu"
   - Install "Ubuntu 22.04 LTS" or latest version

4. **Launch Ubuntu and complete setup**:
   - Create username and password
   - Update the system:
   ```bash
   sudo apt update && sudo apt upgrade -y
   ```

### Install Required Tools in WSL

```bash
# Install Python 3.12+
sudo apt update
sudo apt install python3.12 python3.12-venv python3-pip -y

# Install Git
sudo apt install git -y

# Install Docker (for LocalNet)
# Note: Docker Desktop should be installed on Windows, not in WSL
# WSL will use Docker Desktop from Windows

# Install VS Code Server (for remote development)
curl -fsSL https://code-server.dev/install.sh | sh
```

### Install VS Code WSL Extension

1. **Open VS Code on Windows**
2. **Install WSL Extension**:
   - Go to Extensions (Ctrl+Shift+X)
   - Search for "WSL"
   - Install "WSL" extension by Microsoft

3. **Connect to WSL**:
   - Press `Ctrl+Shift+P`
   - Type "WSL: Connect to WSL"
   - Select your Ubuntu distribution

## Step 0B: Create Project Folder

### Create Your Development Folder

**Choose your preferred location:**

#### For WSL Users:
```bash
# Navigate to your home directory
cd ~

# Create a dedicated folder for Algorand projects
mkdir algorand-projects
cd algorand-projects

# Create a folder for this fellowship
mkdir algorand-pak-fellowship
cd algorand-pak-fellowship

# Verify you're in the right location
pwd
# Should show: /home/yourusername/algorand-projects/algorand-pak-fellowship
```

#### For Native Windows/macOS/Linux:
```bash
# Windows (PowerShell/Command Prompt)
mkdir C:\Users\%USERNAME%\algorand-projects
cd C:\Users\%USERNAME%\algorand-projects
mkdir algorand-pak-fellowship
cd algorand-pak-fellowship

# macOS/Linux (Terminal)
mkdir ~/algorand-projects
cd ~/algorand-projects
mkdir algorand-pak-fellowship
cd algorand-pak-fellowship
```

### Open Folder in VS Code

#### For WSL Users:
```bash
# From your project folder in WSL terminal
code .
# This will open VS Code with WSL integration
```

#### For Native Users:
```bash
# From your project folder in terminal
code .
# Or open VS Code and use File > Open Folder
```

### Verify VS Code Setup

1. **Check if you're in the right environment**:
   - WSL users: Look for "WSL: Ubuntu" in the bottom-left corner
   - Native users: Look for your Python interpreter in the bottom-left corner

2. **Open integrated terminal**:
   - Press `Ctrl+`` (backtick) or Terminal > New Terminal
   - Verify you're in the correct directory

3. **Check Python version**:
   ```bash
   python3 --version
   # Should show Python 3.12.x or higher
   ```

## Step 0C: Environment Verification

### Quick Environment Check

Create a test file to verify everything is working:

```bash
# Create a test file
touch test_setup.py
```

Add this content to `test_setup.py`:
```python
#!/usr/bin/env python3
"""
Environment verification script
"""
import sys
import platform
import subprocess

def check_environment():
    print("🔍 Checking Development Environment...")
    print("=" * 50)
    
    # Check Python version
    python_version = sys.version_info
    print(f"Python Version: {python_version.major}.{python_version.minor}.{python_version.micro}")
    
    if python_version >= (3, 12):
        print("✅ Python version is compatible")
    else:
        print("❌ Python 3.12+ required")
    
    # Check operating system
    print(f"Operating System: {platform.system()} {platform.release()}")
    
    # Check if we're in WSL
    if "microsoft" in platform.uname().release.lower():
        print("🐧 Running in WSL (Windows Subsystem for Linux)")
    else:
        print("💻 Running natively")
    
    # Check Git
    try:
        git_version = subprocess.check_output(['git', '--version'], text=True).strip()
        print(f"Git: {git_version}")
        print("✅ Git is available")
    except FileNotFoundError:
        print("❌ Git not found")
    
    # Check Docker (if available)
    try:
        docker_version = subprocess.check_output(['docker', '--version'], text=True).strip()
        print(f"Docker: {docker_version}")
        print("✅ Docker is available")
    except FileNotFoundError:
        print("⚠️  Docker not found (will be needed for LocalNet)")
    
    print("=" * 50)
    print("🎯 Environment check complete!")

if __name__ == "__main__":
    check_environment()
```

Run the verification:
```bash
python3 test_setup.py
```

### Expected Output

**For WSL Users:**
```
🔍 Checking Development Environment...
==================================================
Python Version: 3.12.x
✅ Python version is compatible
Operating System: Linux 5.15.x
🐧 Running in WSL (Windows Subsystem for Linux)
Git: git version 2.34.x
✅ Git is available
Docker: Docker version 24.x.x
✅ Docker is available
==================================================
🎯 Environment check complete!
```

**For Native Users:**
```
🔍 Checking Development Environment...
==================================================
Python Version: 3.12.x
✅ Python version is compatible
Operating System: Windows 10/11 (or macOS/Linux)
💻 Running natively
Git: git version 2.34.x
✅ Git is available
Docker: Docker version 24.x.x
✅ Docker is available
==================================================
🎯 Environment check complete!
```

## Troubleshooting WSL Setup

### Common WSL Issues

**WSL not starting:**
```powershell
# Check WSL status
wsl --list --verbose

# If not running, start it
wsl --distribution Ubuntu
```

**Docker not working in WSL:**
- Ensure Docker Desktop is installed on Windows
- Enable "Use the WSL 2 based engine" in Docker Desktop settings
- Restart Docker Desktop

**VS Code WSL connection issues:**
- Install the WSL extension in VS Code
- Use `code .` from WSL terminal
- Check that VS Code is in your PATH

**Permission issues:**
```bash
# Fix file permissions if needed
sudo chown -R $USER:$USER ~/algorand-projects
```

## Next Steps

Once your environment is verified, you're ready to proceed with AlgoKit installation! Choose your path:

- **WSL Users**: Continue with the AlgoKit installation in your WSL environment
- **Native Users**: Continue with the AlgoKit installation in your native environment

Your development workspace is now properly set up and ready for Algorand development! 🚀

## Prerequisites

Before installing AlgoKit, ensure you have the following installed:

- **Python 3.12 or higher** ✅ (Already installed from prerequisites)
- **Git** ✅ (Already installed from prerequisites)
- **Docker** ✅ (Already installed from prerequisites)
- **VS Code** ✅ (Already installed from prerequisites)
- **PipX** (We'll install this)

## Step 1: Install PipX

PipX is a tool for installing and running Python applications in isolated environments. It's the recommended way to install AlgoKit.

### Windows
```powershell
# Install pipx
pip install --user pipx
python -m pipx ensurepath

# Restart terminal to ensure pipx is available
```

### macOS/Linux
```bash
# Install pipx
pip install --user pipx
python -m pipx ensurepath

# Restart terminal to ensure pipx is available
```

## Step 2: Install AlgoKit

Install AlgoKit using pipx:

```bash
# Install AlgoKit
pipx install algokit

# If you've used AlgoKit before, update it:
pipx upgrade algokit
```

## Step 3: Verify Installation

Verify that AlgoKit is installed correctly:

```bash
algokit --version
```

You should see output similar to:
```
algokit, version 2.6.0
```

## Step 4: Start LocalNet

AlgoKit provides a local Algorand blockchain for development and testing. This is much faster and cheaper than using TestNet or MainNet.

### Prerequisites for LocalNet
1. **Start Docker Desktop** on your computer
2. **Ensure Docker is running** before proceeding

### Start LocalNet
```bash
# Start the local Algorand blockchain
algokit localnet start
```

This will:
- Start a local Algorand blockchain instance in Docker
- Create a local network for testing
- Provide accounts with test ALGO for development

### Verify LocalNet is Running
1. Open Docker Desktop
2. You should see a running container for Algorand LocalNet
3. The terminal should show LocalNet startup messages

## Step 5: Create Your First AlgoKit Project

AlgoKit provides templates for different types of projects. Let's create a smart contract project:

```bash
# Create a new AlgoKit project
algokit init
```

### Project Creation Steps

1. **Select Project Type**: Choose "Smart Contracts"
2. **Select Language**: Choose "Python" (or TypeScript if you prefer)
3. **Project Name**: Enter a name like "hello-algorand"
4. **Smart Contract Name**: Keep default or customize
5. **Template Preset**: Choose "Starter" for learning
6. **Bootstrap Dependencies**: Choose "y" (yes) to install dependencies
7. **Initialize Git**: Choose "y" (yes) to create a git repository

### Example Project Structure
After creation, you'll have a project structure like:
```
hello-algorand/
├── smart_contracts/
│   └── hello_world/
│       ├── contract.py          # Your smart contract
│       └── deploy_config.py     # Deployment script
├── artifacts/                   # Generated files
├── .algokit/                   # AlgoKit configuration
└── README.md
```

## Step 6: Run Your First Smart Contract

Navigate to your project directory and run the demo:

```bash
# Navigate to your project
cd hello-algorand

# Build and deploy the smart contract
algokit project run build
algokit project deploy localnet
```

### Expected Output
You should see output similar to:
```
=== Deploying HelloWorld ===
Idempotently deploying app "HelloWorld" from creator RQGFSWXL2RKDBO53MN3ZRWCO3CP2HCZ6T4D5DMNJSIXRV76XAEBUJNHOMY using 86 bytes of AVM bytecode and 4 bytes of AVM bytecode
App HelloWorld not found in apps created by RQGFSWXL2RKDBO53MN3ZRWCO3CP2HCZ6T4D5DMNJSIXRV76XAEBUJNHOMY; deploying app with version 1.0.
App created by RQGFSWXL2RKDBO53MN3ZRWCO3CP2HCZ6T4D5DMNJSIXRV76XAEBUJNHOMY with ID 2225 via transaction PSO2XD77YINZRSNH5X76EN6QZYC2I3P6NITJQCCSDS7IC2PJ4RYA
Sending 1000000 µALGO from RQGFSWXL2RKDBO53MN3ZRWCO3CP2HCZ6T4D5DMNJSIXRV76XAEBUJNHOMY to JM7DKIZGR3M4EGZYYR7LXUDX3R7X6QLRV4S2YVLTSDZP73XLX5A6ZDAQLE via transaction T66O4VNOD5CV6RZ75J53PHFMIIX2DCGT2Q3VM7W3W4CJ7DJQK6MA
App 2225 called with hello(world) by RQGFSWXL2RKDBO53MN3ZRWCO3CP2HCZ6T4D5DMNJSIXRV76XAEBUJNHOMY via transaction W2ZQYBEAFXDKHWDBBKJ6WC56ASAQ267ZEHYESWYLZP3YT3AACMGQ
Called hello on HelloWorld (2225) with name = world, received: Hello, world
```

## Step 7: Explore with Lora (Optional)

Lora is a web-based interface for visualizing and interacting with your smart contracts:

```bash
# Open Lora in your browser
algokit explore
```

This will:
- Open Lora in your default web browser
- Show your deployed smart contracts
- Allow you to interact with contracts visually
- Display transaction details and account information

## Generated Artifacts

AlgoKit automatically generates several useful files in the `artifacts/` folder:

- **TEAL Files**: `HelloWorld.approval.teal`, `HelloWorld.clear.teal`
- **ABI File**: `HelloWorld.arc56.json` (Application Binary Interface)
- **Client Code**: `hello_world_client.py` (Auto-generated client for your contract)

## Common AlgoKit Commands

```bash
# Project management
algokit init                    # Create new project
algokit project bootstrap       # Install dependencies
algokit project run build       # Build smart contracts
algokit project deploy localnet # Deploy to LocalNet
algokit project deploy testnet  # Deploy to TestNet

# LocalNet management
algokit localnet start          # Start LocalNet
algokit localnet stop           # Stop LocalNet
algokit localnet status         # Check LocalNet status

# Utilities
algokit explore                 # Open Lora explorer
algokit doctor                  # Check system health
algokit --help                  # Show all commands
```

## Troubleshooting

### Common Issues

**AlgoKit command not found**
- Restart your terminal after installing pipx
- Ensure pipx is in your PATH: `python -m pipx ensurepath`

**LocalNet won't start**
- Ensure Docker Desktop is running
- Check Docker has enough resources allocated
- Try: `algokit localnet stop` then `algokit localnet start`

**Project creation fails**
- Ensure you have Python 3.12+ installed
- Check your internet connection
- Try running `algokit doctor` to diagnose issues

**Build errors**
- Ensure you're in the project directory
- Check that all dependencies are installed: `algokit project bootstrap`
- Verify LocalNet is running: `algokit localnet status`

## Next Steps

Your AlgoKit development environment is now ready! You can:

1. **Explore the generated code** in your project's `smart_contracts/` folder
2. **Modify the smart contract** to add your own functionality
3. **Learn about Algorand concepts** in the `01-Blockchain-Introduction/` section
4. **Start building your own dApp** using AlgoKit templates

## Additional Resources

- [AlgoKit Official Documentation](https://dev.algorand.co/getting-started/algokit-quick-start/)
- [AlgoKit Examples Gallery](https://dev.algorand.co/getting-started/algokit-examples-gallery/)
- [Algorand Developer Portal](https://dev.algorand.co/)
- [Lora Explorer](https://lora.algorand.foundation/)
