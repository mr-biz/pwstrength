# pwstrength

## Description
**pwstrength** is a command-line tool for checking password strength using the zxcvbn library. It provides a simple interface to evaluate the security of passwords and offers detailed feedback on their strength.

## Key Features
- Uses the zxcvbn library for advanced password strength estimation.
- Provides a basic strength score from 0-4.
- Offers detailed feedback including warnings and suggestions for improvement.
- Includes a verbose mode for more in-depth analysis.
- Displays estimated crack times for different attack scenarios.
- Identifies patterns within the password.

## Components
The project consists of two main components:
1. **pwstrength.py**: A Python script that implements the core functionality.
2. **pwstrength**: A bash wrapper script that manages the Python virtual environment and provides a convenient command-line interface.

## Usage
```bash
./pwstrength -p <password> [-v]
```

## Installation:

```bash
# Clone the repository
git clone https://github.com/mr-biz/pwstrength.git
cd pwstrength

# Create virtual environment
python3 -m venv zxcvbn_env

# Activate virtual environment
source zxcvbn_env/bin/activate

# Install requirements
pip install -r requirements.txt

# Make the script executable
chmod +x pwstrength

# Deactivate virtual environment
deactivate
```
