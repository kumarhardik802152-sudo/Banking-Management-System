# Banking Management System Statement

## Problem Statement

Basic banking tasks such as creating an account, checking a balance, depositing money, and withdrawing money need a clear and organized way to record account details and apply simple transaction rules. This project provides a small, menu-driven program that demonstrates these tasks. It validates basic inputs and prevents withdrawals that exceed the available balance.

## Scope of the Project

The project is a local command-line application written in Python. It supports account creation, PIN-based login, deposits, withdrawals, balance checking, account detail display, transaction history, and logout. Account records are held in memory only for the duration of one run. Database storage, account-to-account transfers, persistent statements, and real banking integrations are outside the project's scope.

## Target Users

- Students learning Python fundamentals and object-oriented programming.
- Instructors demonstrating classes, functions, collections, loops, and input validation.
- Users who want to explore a simple console-based banking workflow for educational purposes.

This program is not intended for customers to manage real money or sensitive banking credentials.

## High-Level Features

- Create an account with a sequential account number and six-digit numeric PIN.
- Authenticate an account holder using the account number and PIN.
- Deposit a positive amount and update the balance.
- Withdraw money only when the amount is positive and does not exceed the available balance.
- Display the current balance and account details.
- Keep and display a transaction history during the current session.
- Provide menu options for account actions, logout, and program exit.
