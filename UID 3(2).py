import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        op = operator.get()

        if op == "+":
            result = a + b
        elif op == "-":
            result = a - b
        elif op == "*":
            result = a * b
        elif op == "/":
            result = a / b

        result_label.config(text="Result: " + str(result))

    except:
        messagebox.showerror("Error", "Invalid Input")

root = tk.Tk()
root.title("GUI Calculator")

tk.Label(root, text="Number 1").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Number 2").pack()
entry2 = tk.Entry(root)
entry2.pack()

operator = tk.StringVar(value="+")
tk.OptionMenu(root, operator, "+", "-", "*", "/").pack()

tk.Button(root, text="Calculate", command=calculate).pack()
result_label = tk.Label(root, text="Result:")
result_label.pack()

root.mainloop()
