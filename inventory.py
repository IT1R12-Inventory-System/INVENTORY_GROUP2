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
