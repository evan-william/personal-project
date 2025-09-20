# FinPlanner

A basic personal finance tracker I built to practice Python programming and test out some ideas for managing money through a terminal interface.

## What It Does

This is a simple command-line app that helps track your balance and plan future expenses. I made it because I wanted to practice building a complete program with file handling, user input, and data management.

It lets you record transactions, plan future income/expenses by month, and see projected balances. Nothing fancy, but it covers the basics of what you'd want in a personal finance tool.

## Features

- Track current balance
- Add income/expense transactions manually
- Plan future transactions by month
- Apply planned transactions to your balance automatically
- View balance projections
- Stores data in CSV files locally

## Requirements

Python packages needed:
- `inquirer` (for menu interface)
- `pyfiglet` (for text formatting)
- Standard library modules (csv, datetime, etc.)

Install the external ones:
```bash
pip install inquirer pyfiglet
```

## How to Use

Run the program:
```bash
python app.py
```

Main menu gives you these options:
1. Show current balance
2. Add transactions manually 
3. Apply planned transactions to balance
4. Use the planner for future income/expenses
5. Exit

The planner lets you set expected income and expenses for different months, then see how your balance might look over time.

## Why I Built This

Wanted to practice building a complete Python program that actually does something useful. File handling, user menus, data validation, date calculations - seemed like a good way to test different programming concepts.

I set it up for Indonesian Rupiah since that's what I'd use, but the currency is just formatting - the logic works for any currency.

## Project Structure

```
app.py           # Main application
balance.csv      # Current balance storage
transactions.csv # Transaction history
planner.csv      # Future planned transactions
```

## What I Learned

- Working with CSV files for data persistence
- Building interactive terminal menus with inquirer
- Date and calendar calculations in Python
- Input validation and error handling
- Organizing code into functions
- Managing program state across sessions

## Limitations

Pretty basic implementation:
- No data visualization
- Terminal-only interface  
- Single currency support
- No budget categories or limits
- Limited reporting features
- No data backup/export options

## Possible Improvements

Could add:
- GUI interface
- Charts and graphs
- Multiple account support
- Budget categories
- Expense analysis
- Data export features
- Better error handling

## Author

**Evan William**  
Version 1.0 (2025)

Built this as a learning project to practice Python programming concepts. It's my first complete application that handles user data, file storage, and has multiple features working together.

Good exercise in building something from scratch and thinking through the user experience, even for a simple terminal app.

---

*Personal project for learning and experimentation.*
