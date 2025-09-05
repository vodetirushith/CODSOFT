import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        use_digits = digits_var.get()
        use_symbols = symbols_var.get()

        letters = string.ascii_letters
        digits = string.digits
        symbols = string.punctuation

        characters = letters
        if use_digits:
            characters += digits
        if use_symbols:
            characters += symbols

        if length < 4:
            messagebox.showerror("Error", "Password length should be at least 4")
            return

        password = ''.join(random.choice(characters) for _ in range(length))
        result_entry.delete(0, tk.END)
        result_entry.insert(0, password)

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for length")

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.config(bg="#f4f6f7")


header = tk.Label(root, text="Password Generator", font=("Arial", 16, "bold"), bg="#2E86C1", fg="white", pady=10)
header.pack(fill=tk.X)


tk.Label(root, text="Enter password length:", font=("Arial", 12), bg="#f4f6f7").pack(pady=5)
length_entry = tk.Entry(root, font=("Arial", 12))
length_entry.pack(pady=5)


digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include digits (0-9)", variable=digits_var, font=("Arial", 11), bg="#f4f6f7").pack(anchor="w", padx=50)
tk.Checkbutton(root, text="Include symbols (!@#$...)", variable=symbols_var, font=("Arial", 11), bg="#f4f6f7").pack(anchor="w", padx=50)


generate_btn = tk.Button(root, text="Generate Password", command=generate_password, bg="#27AE60", fg="white", font=("Arial", 12, "bold"), padx=10, pady=5)
generate_btn.pack(pady=15)


result_entry = tk.Entry(root, font=("Arial", 12), width=30, justify="center")
result_entry.pack(pady=10)

root.mainloop()
