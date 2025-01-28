import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == "Addition":
            result = num1 + num2
        elif operation == "Subtraction":
            result = num1 - num2
        elif operation == "Multiplication":
            result = num1 * num2
        elif operation == "Division":
            if num2 == 0:
                messagebox.showerror("Error", "Division by zero is not allowed!")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Select a valid operation!")
            return

        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input! Please enter numeric values.")

root = tk.Tk()
root.title("Simple Calculator")

tk.Label(root, text="Enter first number:").grid(row=0, column=0, padx=10, pady=5)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Enter second number:").grid(row=1, column=0, padx=10, pady=5)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Select operation:").grid(row=2, column=0, padx=10, pady=5)
operation_var = tk.StringVar(value="Addition")
operations = ["Addition", "Subtraction", "Multiplication", "Division"]
tk.OptionMenu(root, operation_var, *operations).grid(row=2, column=1, padx=10, pady=5)

tk.Button(root, text="Calculate", command=calculate).grid(row=3, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="Result: ")
result_label.grid(row=4, column=0, columnspan=2, pady=5)

root.mainloop()
