# Installation Guide

This guide will help you install all the necessary tools for Algorand Python development in 2025.

## System Requirements

- **Operating System**: Windows 10+, macOS 10.15+, or Linux (Ubuntu 20.04+)
- **RAM**: Minimum 4GB, recommended 8GB+
- **Storage**: At least 2GB free space
- **Internet**: Stable connection for downloading packages

## Step 1: Install Python 3.12+

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

## Step 2: Install Git (if not already installed)

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

## Step 3: Install VS Code (Recommended IDE)

1. Download from [code.visualstudio.com](https://code.visualstudio.com/)
2. Install Python extension:
   - Open VS Code
   - Go to Extensions (Ctrl+Shift+X)
   - Search for "Python" and install the official Microsoft extension

## Step 4: Verify Installation

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

## Next Steps

Once installation is complete, proceed to:
1. `setup_env.md` - Set up your development environment
2. `python_basics.md` - Learn Python fundamentals (if needed)

## Additional Resources

- [Python Official Documentation](https://docs.python.org/3/)
- [VS Code Python Tutorial](https://code.visualstudio.com/docs/python/python-tutorial)
- [Git Documentation](https://git-scm.com/doc)
