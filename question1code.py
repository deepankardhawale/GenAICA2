# Q:1 Generate a model in Python for representation of a bank account of type savings and
# balance along with transactions of deposit and withdrawals and currently create a program to
# generate 100 accounts with Random balance and transactions for no. of months and no. of
# transactions with a seed value of amount. Print all 100 accounts with the last balance and
# organize them by lowest to highest balance.

# Code
import random
import pandas as pd

class BankAccount:
    def __init__(self, account_id, balance):
        self.account_id = account_id
        self.balance = balance
        self.transactions = []  # To store the transaction history

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposit: +{amount}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append(f"Withdrawal: -{amount}")
        else:
            self.transactions.append(f"Withdrawal failed: Insufficient balance")

    def __str__(self):
        # Account info with last 6 months' transactions
        transaction_history = "\n".join(self.transactions[-6:])
        return f"Account {self.account_id}: Balance = {self.balance}\nLast 6 transactions:\n{transaction_history}"

def generate_accounts(num_accounts, num_months, seed_value):
    random.seed(seed_value)
    accounts = []

    for i in range(num_accounts):
        initial_balance = random.randint(1000, 10000)
        account = BankAccount(account_id=i+1, balance=initial_balance)
        
        for _ in range(num_months):
            transaction_type = random.choice(["deposit", "withdraw"])
            transaction_amount = random.randint(100, 2000)
            if transaction_type == "deposit":
                account.deposit(transaction_amount)
            else:
                account.withdraw(transaction_amount)
        
        accounts.append(account)

    return accounts

def print_sorted_accounts(accounts):
    sorted_accounts = sorted(accounts, key=lambda x: x.balance)
    for account in sorted_accounts:
        print(account)
        print("-" * 40)

accounts = generate_accounts(num_accounts=100, num_months=6, seed_value=12345)
print_sorted_accounts(accounts)
