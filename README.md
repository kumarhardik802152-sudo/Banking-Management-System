# Banking Management System

A command-line banking application built with Python. The project demonstrates basic account creation, PIN-based login, deposits, withdrawals, and account history using object-oriented programming.

## Project Overview

Users can create an account, sign in with its account number and six-digit PIN, and perform basic banking actions through a numbered menu. Account information is kept in memory for the current program session.

## Features

- Create accounts with sequential account numbers beginning at 1001.
- Validate that account PINs contain exactly six digits.
- Deposit money and record the transaction.
- Withdraw money while checking the available balance.
- Display current balance and account details.
- View transaction history and log out.

## Technologies and Tools

- Python 3
- Python standard library only
- Any text editor or IDE
- Terminal or command prompt

## Project Files

- `banking_management_system.py` — complete application source code.
- `statement.md` — problem statement, scope, target users, and high-level features.

## Install and Run

1. Install Python 3 if it is not already installed.
2. Open a terminal in the folder containing `banking_management_system.py`.
3. Run:

   ```bash
   python banking_management_system.py
   ```

   On systems where Python is invoked as `python3`, use `python3 banking_management_system.py`.
4. Select an option from the main menu and follow the prompts.

There are no third-party packages to install.

## Testing Instructions

Run the program and try these manual checks:

1. Create an account using a six-digit numeric PIN and a non-negative opening balance.
2. Try creating an account with a PIN that is too short, too long, or contains non-numeric characters; the program should reject it.
3. Log in with the new account number and PIN, then try an incorrect PIN.
4. Deposit a positive amount and confirm that the displayed balance increases and the transaction appears in history.
5. Withdraw an amount within the balance, then try an amount larger than the available balance.
6. Check account details and transaction history, log out, and exit.

Accounts are not saved after the program closes, so create a fresh account when repeating these checks in a new run.

## Limitations

This is an educational project and is not suitable for real banking. Account data is stored only in memory and is lost when the application exits. PINs are stored as plain text. The program has no database, encryption, transfers, or persistent audit history. Floating-point numbers are used for money, so a production system should use decimal arithmetic and stronger validation.

## Screenshots

Screenshots are optional. Add terminal screenshots here if required for your submission.

## License

No license has been specified for this project.
