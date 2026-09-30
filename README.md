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

<img width="661" height="397" alt="Screenshot 2026-09-30 194241" src="https://github.com/user-attachments/assets/5b96f5fa-a3d8-4452-9962-8d98bf413ed1" />
<img width="396" height="324" alt="Screenshot 2026-09-30 194218" src="https://github.com/user-attachments/assets/b080c297-49af-4c13-9fd3-d3fe61679851" />
<img width="397" height="447" alt="Screenshot 2026-09-30 194143" src="https://github.com/user-attachments/assets/ec6636e6-2867-4b85-9531-af793acac086" />
<img width="392" height="211" alt="Screenshot 2026-09-30 194107" src="https://github.com/user-attachments/assets/a64de189-ac89-495b-99e9-6ab57223b5c1" />
<img width="370" height="292" alt="Screenshot 2026-09-30 194041" src="https://github.com/user-attachments/assets/a4694d0c-3e0d-45c5-af58-817d07d85bba" />


## License

No license has been specified for this project.
