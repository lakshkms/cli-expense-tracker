# CLI Expense Tracker

A command-line expense tracker built in Python. Logs income and spending, stores everything in a JSON file so data persists between runs, and gives a monthly breakdown of credits vs. debits.

My first real Python project, built while learning the language from scratch.

## Features

- **Add a transaction** — log a credit (income) or debit (expense) with a date, category, and amount
- **View balance** — see current running balance
- **View history** — a formatted table of all logged transactions
- **Monthly summary** — total credits, debits, and net change for a given month/year

## How to run

```bash
python menu.py
```

```
==============================
       EXPENSE TRACKER
==============================
1. add transaction
2. view balance
3. view transactions
4. monthly summary
5. exit
==============================
```

## Project structure

```
├── menu.py          # UI layer — handles user choice
├── transaction.py   # logic — add/view/calculate
└── data.json         # persistent storage
```

## How it works

Each transaction is a dictionary (month, date, year, operation, amount, category) stored in a list inside `data.json`, alongside a running `balance` updated on every add.

```json
{
  "balance": 11870.0,
  "transactions": [
    {"month": "January", "date": 7, "operation": "b", "amount": 500.0, "category": "food", "year": 2026}
  ]
}
```