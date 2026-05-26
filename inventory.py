import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import os

FILE = "inventory_data.txt"


def load():
    if not os.path.exists(FILE):
        open(FILE, "w", encoding="utf-8").close()

    items = []
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            for line in f:
                name, unit, qty, price = line.strip().split("|")
                items.append({
                    "name": name,
                    "unit": unit,
                    "quantity": int(qty),
                    "price": float(price),
                })
    except Exception:
        messagebox.showerror("Load Error", "Could not read inventory file.")

    return items

def save(items):
    try:
        with open(FILE, "w", encoding="utf-8") as f:
            for item in items:
                f.write(f"{item['name']}|{item['unit']}|{item['quantity']}|{item['price']}\n")
        return True
    except Exception:
        messagebox.showerror("Save Error", "Could not write inventory file.")
        return False


def validate(name, unit, qty, price):
    if not name.strip():
        messagebox.showerror("Validation", "Product name is required.")
        return False
    if not unit.strip():
        messagebox.showerror("Validation", "Unit is required.")
        return False
    try:
        if int(qty) < 0:
            raise ValueError
    except Exception:
        messagebox.showerror("Validation", "Quantity must be a non-negative integer.")
        return False
    try:
        if float(price) < 0:
            raise ValueError
    except Exception:
        messagebox.showerror("Validation", "Price must be a non-negative number.")
        return False
    return True

# ✅ CREATE GUI FIRST
root = tk.Tk()
root.title("Inventory System")
root.geometry("600x400")

# (you can add buttons, labels here later)


# ✅ RUN GUI LAST (IMPORTANT)
root.mainloop()

