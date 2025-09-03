# Development Environment Setup

This guide will help you set up a proper development environment for Algorand Python development, including Docker for containerized development.

## Why Use Virtual Environments?

Virtual environments isolate your project dependencies, preventing conflicts between different projects. This is especially important for blockchain development where you might work on multiple projects with different package versions.

## Step 1: Create a Virtual Environment

Navigate to your project directory and create a virtual environment:

```bash
# Create virtual environment
python -m venv algorand-env

# Activate virtual environment
# Windows:
algorand-env\Scripts\activate

# macOS/Linux:
source algorand-env/bin/activate
```

You should see `(algorand-env)` in your terminal prompt, indicating the virtual environment is active.

## Step 2: Upgrade pip

```bash
python -m pip install --upgrade pip
```

## Step 3: Install Algorand Development Packages

### Core Algorand Packages

```bash
# Algorand Python SDK
pip install py-algorand-sdk

# Algorand Python (Puya)
pip install algorand-python

# PyTeal (for smart contract development)
pip install pyteal

# Additional useful packages
pip install algokit-utils
pip install algosdk
```

### Development Tools

```bash
# Code formatting and linting
pip install black flake8 mypy

# Testing framework
pip install pytest

# Jupyter notebook (for interactive development)
pip install jupyter notebook

# Docker integration tools
pip install docker-compose

# Git integration
pip install gitpython
```

## Step 4: Verify Installation

Create a verification script:

```python
# verify_setup.py
def test_imports():
    """Test that all required packages can be imported."""
    
    packages = [
        'algosdk',
        'pyteal',
        'algokit_utils'
    ]
    
    print("Testing package imports...")
    
    for package in packages:
        try:
            __import__(package)
            print(f"✓ {package} imported successfully")
        except ImportError as e:
            print(f"✗ Failed to import {package}: {e}")
    
    # Test Algorand Python specifically
    try:
        import algopy
        print("✓ Algorand Python (algopy) imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import algopy: {e}")
        print("Note: algopy might not be available yet - this is normal for now")

if __name__ == "__main__":
    test_imports()
```

Run the verification:
```bash
python verify_setup.py
```

## Step 5: Configure VS Code (Optional but Recommended)

Create a `.vscode/settings.json` file in your project:

```json
{
    "python.defaultInterpreterPath": "./algorand-env/bin/python",
    "python.linting.enabled": true,
    "python.linting.flake8Enabled": true,
    "python.formatting.provider": "black",
    "python.testing.pytestEnabled": true,
    "python.testing.pytestArgs": [
        "tests"
    ]
}
```

## Step 6: Docker Setup (Optional but Recommended)

### Create Dockerfile
```dockerfile
# Dockerfile
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose port (if needed)
EXPOSE 8000

# Default command
CMD ["python", "main.py"]
```

### Create docker-compose.yml
```yaml
# docker-compose.yml
version: '3.8'

services:
  algorand-dev:
    build: .
    volumes:
      - .:/app
    ports:
      - "8000:8000"
    environment:
      - PYTHONPATH=/app
    command: python -m pytest tests/
```

## Step 7: Create Project Structure

```bash
# Create basic project structure
mkdir src tests docs
touch src/__init__.py
touch tests/__init__.py
touch requirements.txt
touch Dockerfile
touch docker-compose.yml
```

## Step 8: Generate Requirements File

```bash
# Generate requirements.txt from installed packages
pip freeze > requirements.txt
```

## Environment Variables Setup

Create a `.env` file for configuration (don't commit this to version control):

```bash
# .env
ALGORAND_NETWORK=testnet
ALGORAND_API_TOKEN=your_api_token_here
ALGORAND_INDEXER_URL=https://testnet-idx.algonode.cloud
ALGORAND_ALGOD_URL=https://testnet-api.algonode.cloud
```

## Deactivating Virtual Environment

When you're done working:

```bash
deactivate
```

## Reactivating Virtual Environment

To resume work:

```bash
# Navigate to your project directory
cd your-project-directory

# Activate virtual environment
# Windows:
algorand-env\Scripts\activate

# macOS/Linux:
source algorand-env/bin/activate
```

## Troubleshooting

### Common Issues

**Virtual environment not activating**
- Make sure you're in the correct directory
- Check that the virtual environment was created successfully
- Try using the full path to the activation script

**Package installation fails**
- Make sure your virtual environment is activated
- Check your internet connection
- Try upgrading pip first: `python -m pip install --upgrade pip`

**Import errors after installation**
- Verify the virtual environment is activated
- Check that packages were installed in the correct environment
- Try reinstalling the problematic package

## Docker Commands

### Basic Docker Commands
```bash
# Build Docker image
docker build -t algorand-dev .

# Run container
docker run -it algorand-dev

# Run with docker-compose
docker-compose up

# Stop containers
docker-compose down

# View running containers
docker ps

# View logs
docker logs <container_id>
```

## Best Practices

1. **Always use virtual environments** for Python projects
2. **Keep requirements.txt updated** when adding new packages
3. **Use descriptive environment names** (e.g., `algorand-dev-env`)
4. **Document your setup** in your project README
5. **Never commit virtual environment folders** to version control
6. **Use Docker for consistent environments** across different machines
7. **Version control your Dockerfile** and docker-compose.yml

## Next Steps

Your development environment is now ready! Proceed to:
1. `python_basics.md` - Learn Python fundamentals (if needed)
2. `01-Blockchain-Introduction/` - Start learning about blockchain and Algorand

## Additional Resources

- [Python Virtual Environments Guide](https://docs.python.org/3/tutorial/venv.html)
- [Algorand Python Documentation](https://algorandfoundation.github.io/puya/)
- [VS Code Python Environment Setup](https://code.visualstudio.com/docs/python/environments)
