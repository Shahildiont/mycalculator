import tkinter as tk

def add_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 + num2
        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Please enter valid numbers!")

def sub_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 - num2
        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Please enter valid numbers!")

def mul_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 * num2
        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Please enter valid numbers!")

def div_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 / num2
        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Please enter valid numbers!")

# main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x220")

# Input 1
tk.Label(root, text="Enter first number:").grid(row=0, column=0, padx=5, pady=5)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=5, pady=5)

# Input 2
tk.Label(root, text="Enter second number:").grid(row=1, column=0, padx=5, pady=5)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=5, pady=5)

# Buttons
tk.Button(root, text="Add", command=add_numbers).grid(row=2, column=0, padx=5, pady=5)
tk.Button(root, text="Sub", command=sub_numbers).grid(row=2, column=1, padx=5, pady=5)
tk.Button(root, text="Mul", command=mul_numbers).grid(row=3, column=0, padx=5, pady=5)
tk.Button(root, text="Div", command=div_numbers).grid(row=3, column=1, padx=5, pady=5)

# Result
result_label = tk.Label(root, text="Result: ")
result_label.grid(row=4, column=0, columnspan=2, pady=10)


root.mainloop()