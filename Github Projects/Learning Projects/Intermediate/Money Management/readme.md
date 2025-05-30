# 💰 FinPlanner

## 📋 Overview
FinPlanner is a simple personal finance management application built in Python to help track and plan your financial activities. This terminal-based application allows you to monitor your balance, record transactions, and plan future income and expenses. 

This is my first complete project that I use personally to manage my finances. While it has a simple terminal-based interface without a graphical UI, it effectively serves all my basic financial planning needs.

## ✨ Features
- **💵 Balance Tracking**: View your current balance with proper formatting  
- **📝 Manual Transaction Recording**: Add income or expenses with descriptions  
- **📅 Financial Planning**: Plan future income and expenses by month  
- **⚙️ Automatic Balance Updates**: Apply planned transactions to your actual balance  
- **📂 CSV Data Storage**: All data is stored locally in CSV files for privacy and ease of access  
- **📈 Projection Tool**: See your projected balance through the end of the year  

## 🛠️ Requirements
The application relies on the following Python packages:  
- inquirer  
- pyfiglet  
- time (standard library)  
- os (standard library)  
- platform (standard library)  
- subprocess (standard library)  
- csv (standard library)  
- calendar (standard library)  
- datetime (standard library)  
- collections (standard library)  

To install the non-standard packages, run:  
```

pip install inquirer pyfiglet

```

## 🚀 How to Use

### ▶️ Running the Application
1. Navigate to the directory containing the `app.py` file  
2. Run the application with:  
```

python app.py

```

### 📋 Main Menu Options
1. **Show Balance**: Displays your current balance formatted in Rupiah  
2. **Update Balance (Manual)**: Add or remove money from your balance manually  
3. **Update Balance (Automatic)**: Apply planned transactions to your actual balance  
4. **Planner**: Plan future income and expenses  
5. **Exit**: Close the application  

### 🗓️ Using the Planner
The planner allows you to:  
- Add expected income for specific months  
- Add expected expenses for specific months  
- View your projected balance through the end of the year  

## 🤔 Why I Made This
I built FinPlanner to help with my personal financial management. As a student handling my own finances, I needed something simple but effective to track my money and plan ahead. Despite its simplicity, this application helps me stay on top of my finances and avoid overspending.

This is my first complete Python project, and while it's just a terminal application, I'm proud of how practical and useful it has been for my daily life. The application was designed specifically for managing Indonesian Rupiah, as that's my local currency.

## 🔮 Future Improvements
In the future, I plan to enhance FinPlanner with:  
- A graphical user interface  
- Data visualization for spending patterns  
- Budget categories and limits  
- Multi-currency support  
- Transaction history reports  

## 👨‍💻 Developer  
Created by Evan William (2025)  
Version: 1.0
