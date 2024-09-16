# Python Model for Bank Accounts with Transactions

This repository contains a Python model that simulates 100 savings bank accounts with random deposits and withdrawals over a period of 6 months. The accounts are sorted based on their final balances from lowest to highest, and each account's transaction history for the last 6 months is displayed.

## Features:
- **Random Account Generation**: Creates 100 random bank accounts, each with a randomly generated initial balance.
- **Simulated Transactions**: Deposits and withdrawals are randomly generated for each account over a period of 6 months.
- **Transaction History**: The last 6 transactions for each account are displayed.
- **Sorting by Balance**: The final account balances are sorted from lowest to highest.
- **Seed Value**: A seed value is used to ensure reproducibility of random account balances and transactions.

## How to Use:
1. Run the `bank_account.py` script.
2. The script will generate 100 random accounts and simulate transactions for 6 months.
3. The accounts will be displayed, sorted by final balance from lowest to highest.
4. Each account will include a transaction history for the last 6 months.

### Example Output:
Account 1: Balance = 9500 Last 6 transactions: Deposit: +500 Withdrawal: -1000 Deposit: +200 Withdrawal: -500 Deposit: +1500 Withdrawal: -200

Account 2: Balance = 8300 Last 6 transactions: Deposit: +1000 Withdrawal: -500 Withdrawal: -1500 Deposit: +2000 Withdrawal: -800 Deposit: +300 ...


## Requirements:
- Python 3.x
- pandas

## Installation:
1. Clone the repository.
2. Install the required libraries:
   ```bash
   pip install pandas
