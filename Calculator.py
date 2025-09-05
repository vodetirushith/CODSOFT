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
                messagebox.showerror("Error", "Cannot divide by zero")
                return
            result = num1 / num2
        else:
            messagebox.showwarning("Warning", "Select an operation")
            return

        result_label.config(text=f"Result: {result:.2f}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")


root = tk.Tk()
root.title("Calculator")
root.geometry("350x300")
root.config(bg="#f4f6f7")


header = tk.Label(root, text="Calculator", font=("Arial", 16, "bold"), bg="#2E86C1", fg="white", pady=10)
header.pack(fill=tk.X)


tk.Label(root, text="Enter first number:", font=("Arial", 12), bg="#f4f6f7").pack(pady=5)
entry1 = tk.Entry(root, font=("Arial", 12))
entry1.pack(pady=5)

tk.Label(root, text="Enter second number:", font=("Arial", 12), bg="#f4f6f7").pack(pady=5)
entry2 = tk.Entry(root, font=("Arial", 12))
entry2.pack(pady=5)


tk.Label(root, text="Choose operation:", font=("Arial", 12), bg="#f4f6f7").pack(pady=5)
operation_var = tk.StringVar()
operation_var.set("Addition")  

operations = ["Addition", "Subtraction", "Multiplication", "Division"]
for op in operations:
    tk.Radiobutton(root, text=op, variable=operation_var, value=op, font=("Arial", 11), bg="#f4f6f7").pack(anchor="w", padx=50)


calc_btn = tk.Button(root, text="Calculate", command=calculate, bg="#27AE60", fg="white", font=("Arial", 12, "bold"), padx=10, pady=5)
calc_btn.pack(pady=15)


result_label = tk.Label(root, text="Result: ", font=("Arial", 14, "bold"), bg="#f4f6f7", fg="#2C3E50")
result_label.pack(pady=10)

root.mainloop()
