# FinanceTracker

FinanceTracker is a personal finance tracking application built with Tkinter for a graphical user interface (GUI). It helps users manage their finances by tracking income, expenses, and providing an overview of their balance. Users can add, view, and delete transactions, and the app dynamically calculates the total income, total expenses, and current balance.

---

## 🌟 Features

- **Track Transactions**: Add income and expense transactions with categories, descriptions, amounts, and dates.
- **Dynamic Categories**: Choose from predefined categories for both income and expenses.
- **Balance Calculation**: Displays total income, total expenses, and current balance.
- **Transaction History**: View all transactions in a user-friendly table with the option to delete any entry.

---

## 📁 Folder Structure
financetracker/
│
├── .gitignore         
├── .replit            
├── generated-icon.png 
├── main.py            
├── poetry.lock       
└── pyproject.toml     


---

## 🚀 Getting Started

### Prerequisites
1. **Python** (version 3.6+)

2. **Install Required Libraries** :

Install the required Python libraries using pip:

pip install tkinter tkcalendar

---

### **Setup**

1. Clone the repository:
git clone https://github.com/cmell05/financetracker.git

2. Navigate to the project directory:
cd financetracker

3. Run the application:
python main.py

---

## 🛠️ Built With

Python: Core programming language for the application.
Tkinter: GUI framework for the user interface.
tkcalendar: For date entry widget to select and display dates.
datetime: To handle date and time-related operations.

---
    
📖 How to Use

**Add Transaction**
1. Transaction Type: Select between Income or Expense.
2. Date: Choose the date for the transaction using the date picker.
3. Category: Select the relevant category based on the transaction type.
4. Amount: Enter the transaction amount.
5. Description: Provide a description for the transaction.
Click the "Add Transaction" button to save it.

**View Transaction History**
Transactions are displayed in a table format showing the date, type (income or expense), category, amount, and description. You can also delete a transaction if necessary.

**Balance Calculation**
The current balance is automatically updated after each transaction is added. The app will show the total income, total expenses, and the current balance.
