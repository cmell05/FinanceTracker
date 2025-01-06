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
