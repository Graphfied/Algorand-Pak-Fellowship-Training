# Installation Guide

This guide will help you install all the necessary tools for Algorand Python development in 2025. Follow the video tutorials for step-by-step guidance.

## System Requirements

- **Operating System**: Windows 10+, macOS 10.15+, or Linux (Ubuntu 20.04+)
- **RAM**: Minimum 4GB, recommended 8GB+
- **Storage**: At least 2GB free space
- **Internet**: Stable connection for downloading packages

## Step 1: Install Python 3.12+

### Video Tutorial
📺 **Watch this tutorial**: [Python 3.12 Installation Guide](https://www.youtube.com/watch?v=ddGTXBhaGWA&ab_channel=AmitThinks)

### Windows
1. Visit [python.org](https://www.python.org/downloads/)
2. Download Python 3.12+ (latest stable version)
3. Run the installer
4. **Important**: Check "Add Python to PATH" during installation
5. Verify installation:
   ```bash
   python --version
   pip --version
   ```

### macOS
1. Install using Homebrew (recommended):
   ```bash
   brew install python@3.12
   ```
2. Or download from [python.org](https://www.python.org/downloads/)
3. Verify installation:
   ```bash
   python3 --version
   pip3 --version
   ```

### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3.12 python3.12-venv python3.12-pip
```

## Step 2: Install Git

### Video Tutorial
📺 **Watch this tutorial**: [Git Installation and Setup](https://www.youtube.com/watch?v=cJTXh7g-uCM&ab_channel=AmitThinks)

### Windows
- Download from [git-scm.com](https://git-scm.com/download/win)
- Use default installation options

### macOS
```bash
brew install git
```

### Linux
```bash
sudo apt install git
```

## Step 3: Create GitHub Account

### Video Tutorial
📺 **Watch this tutorial**: [GitHub Account Setup](https://www.youtube.com/watch?v=J2PQuVAI99c)

1. Visit [github.com](https://github.com)
2. Click "Sign up" to create a new account
3. Choose a username, email, and password
4. Verify your email address
5. Complete your profile setup

## Step 4: Install VS Code (Recommended IDE)

### Video Tutorial
📺 **Watch this tutorial**: [VS Code Installation and Setup](https://www.youtube.com/watch?v=DoLYVXR9SSc&ab_channel=AmitThinks)

1. Download from [code.visualstudio.com](https://code.visualstudio.com/)
2. Install Python extension:
   - Open VS Code
   - Go to Extensions (Ctrl+Shift+X)
   - Search for "Python" and install the official Microsoft extension

## Step 5: Install Docker

### Video Tutorial
📺 **Watch this tutorial**: [Docker Installation and Setup](https://www.youtube.com/watch?v=JBEUKrjbWqg&ab_channel=AmitThinks)

### Windows
1. Download Docker Desktop from [docker.com](https://www.docker.com/products/docker-desktop/)
2. Run the installer
3. **Important**: Enable WSL 2 integration if prompted
4. Restart your computer if required

### macOS
1. Download Docker Desktop from [docker.com](https://www.docker.com/products/docker-desktop/)
2. Drag Docker to Applications folder
3. Launch Docker Desktop
4. Complete the setup wizard

### Linux (Ubuntu/Debian)
```bash
# Update package index
sudo apt update

# Install Docker
sudo apt install docker.io

# Start Docker service
sudo systemctl start docker

# Enable Docker to start on boot
sudo systemctl enable docker

# Add your user to docker group (optional)
sudo usermod -aG docker $USER
```

### WSL 2 for Docker (Windows)
If you're on Windows and need WSL 2 for Docker:

1. **Enable WSL 2**:
   ```powershell
   # Run in PowerShell as Administrator
   dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
   dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
   ```

2. **Download WSL 2 Linux kernel update**:
   - Visit [Microsoft WSL page](https://docs.microsoft.com/en-us/windows/wsl/install-win10)
   - Download and install the WSL 2 Linux kernel update

3. **Set WSL 2 as default**:
   ```powershell
   wsl --set-default-version 2
   ```

4. **Install a Linux distribution**:
   ```powershell
   wsl --install -d Ubuntu
   ```

## Step 6: Verify Installation

Create a test file to verify everything works:

```python
# test_installation.py
print("Python is working!")
print(f"Python version: {__import__('sys').version}")

# Test imports
try:
    import json
    print("✓ Standard library imports work")
except ImportError as e:
    print(f"✗ Import error: {e}")

try:
    import pip
    print("✓ pip is available")
except ImportError as e:
    print(f"✗ pip error: {e}")
```

Run the test:
```bash
python test_installation.py
```

### Verify Docker Installation
```bash
# Check Docker version
docker --version

# Test Docker with hello-world
docker run hello-world
```

### Verify Git Installation
```bash
# Check Git version
git --version

# Configure Git (replace with your details)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

## Troubleshooting

### Common Issues

**"python is not recognized" (Windows)**
- Python wasn't added to PATH during installation
- Reinstall Python and check "Add Python to PATH"
- Or manually add Python to your system PATH

**Permission denied errors (macOS/Linux)**
- Use `python3` instead of `python`
- Use `pip3` instead of `pip`
- Consider using virtual environments (covered in next section)

**Multiple Python versions**
- Use `python3.12` to specify version
- Use `py -3.12` on Windows with Python Launcher

**Docker issues on Windows**
- Ensure WSL 2 is properly installed
- Restart Docker Desktop
- Check Windows features for Hyper-V and WSL

**Git authentication issues**
- Set up SSH keys for GitHub
- Use personal access tokens for HTTPS

## Installation Checklist

Before proceeding to the next section, ensure you have:

- ✅ **Python 3.12+** installed and working
- ✅ **Git** installed and configured
- ✅ **GitHub account** created
- ✅ **VS Code** installed with Python extension
- ✅ **Docker** installed and running
- ✅ **WSL 2** (Windows users only)

## Next Steps

Once installation is complete, proceed to:
1. `setup_env.md` - Set up your development environment
2. `python_basics.md` - Learn Python fundamentals (if needed)

## Additional Resources

- [Python Official Documentation](https://docs.python.org/3/)
- [VS Code Python Tutorial](https://code.visualstudio.com/docs/python/python-tutorial)
- [Git Documentation](https://git-scm.com/doc)
- [Docker Documentation](https://docs.docker.com/)
- [WSL Documentation](https://docs.microsoft.com/en-us/windows/wsl/)
