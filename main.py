import tkinter as tk
from tkinter import ttk
from datetime import datetime

# Tkinter setup
root = tk.Tk()
root.title("Fintrack: Personal Finance Tracker")
root.configure(bg="#f0f2f5")  

root.mainloop()

# Dashboard
dashboard_frame = tk.Frame(root, bg="#f0f2f5", pady=20)
dashboard_frame.pack(fill='x')  # Fill horizontally

income_label = tk.Label(dashboard_frame, text="Total Income: $0.00", bg="#f0f2f5", fg="#34a853", 
                       font=('Helvetica', 12, 'bold'), pady=5)
income_label.pack()

expense_label = tk.Label(dashboard_frame, text="Total Expenses: $0.00", bg="#f0f2f5", fg="#ea4335",
                        font=('Helvetica', 12, 'bold'), pady=5)
expense_label.pack()

balance_label = tk.Label(dashboard_frame, text="Current Balance: $0.00", bg="#f0f2f5", fg="#1a73e8",
                        font=('Helvetica', 14, 'bold'), pady=10)
balance_label.pack()


# Add Transaction Form
form_frame = tk.Frame(root, bg="#f0f2f5", padx=20, pady=20)
form_frame.pack(fill='x')

# Transaction Type (Income/Expense)
tk.Label(form_frame, text="Type:").grid(row=0, column=0)
type_var = tk.StringVar(value="Expense")
type_radio_frame = tk.Frame(form_frame)
type_radio_frame.grid(row=0, column=1)
tk.Radiobutton(type_radio_frame, text="Expense", variable=type_var, value="Expense").pack(side=tk.LEFT)
tk.Radiobutton(type_radio_frame, text="Income", variable=type_var, value="Income").pack(side=tk.LEFT)

# Date
tk.Label(form_frame, text="Date:").grid(row=1, column=0)
date_entry = DateEntry(form_frame, width=12, background='darkblue', foreground='white', date_pattern='yyyy-mm-dd')
date_entry.set_date(datetime.now())  # Set today's date as default
date_entry.grid(row=1, column=1)

# Category (Placeholder - will be dynamically updated later)
tk.Label(form_frame, text="Category:").grid(row=2, column=0)
category_var = tk.StringVar()
category_dropdown = ttk.Combobox(form_frame, textvariable=category_var)
category_dropdown.grid(row=2, column=1, sticky='ew')

# Amount
tk.Label(form_frame, text="Amount:").grid(row=3, column=0)
amount_entry = tk.Entry(form_frame)
amount_entry.grid(row=3, column=1)

# Description
tk.Label(form_frame, text="Description:").grid(row=4, column=0)
description_entry = tk.Entry(form_frame)
description_entry.grid(row=4, column=1)

# Add Transaction Button
add_btn = tk.Button(form_frame, text="Add Transaction")
add_btn.grid(row=5, column=0, columnspan=2, pady=15)


# Transaction History Table
transaction_frame = tk.Frame(root, bg="#f0f2f5", padx=20, pady=20)
transaction_frame.pack()

transaction_table = ttk.Treeview(transaction_frame, columns=("Date", "Type", "Category", "Amount", "Description"), show="headings")
transaction_table.heading("Date", text="Date")
transaction_table.heading("Type", text="Type")
transaction_table.heading("Category", text="Category")
transaction_table.heading("Amount", text="Amount")
transaction_table.heading("Description", text="Description")
transaction_table.pack()

#Add transaction method
def add_transaction():
    date = date_entry.get()
    transaction_type = type_var.get()
    category = category_var.get()
    amount = float(amount_entry.get())
    description = description_entry.get()

    # Add new transaction to the transactions list
    transactions.append({
        "Date": date,
        "Type": transaction_type,
        "Category": category,
        "Amount": amount,
        "Description": description
    })

    # Update the transaction table to show the new transaction
    update_table()

    clear_form()

    calculate_totals()


def update_table():
    # Clear existing rows in the table
    for row in transaction_table.get_children():
        transaction_table.delete(row)

    # Insert each transaction in the list as a new row in the table
    for txn in transactions:
        transaction_table.insert("", "end", values=(txn["Date"], txn["Type"], txn["Category"], txn["Amount"], txn["Description"]))
    




                        

root.mainloop() 




