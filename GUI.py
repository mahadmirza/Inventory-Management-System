import sqlite3
import tkinter as tk
from tkinter import messagebox

# Database connection
conn = sqlite3.connect("inventory.db")
cursor = conn.cursor()

# Create the main application window
root = tk.Tk()
root.title("Inventory Management System")

# Functions for UI interaction
def add_product():
    # Create a new window for adding a product
    add_window = tk.Toplevel(root)
    add_window.title("Add Product")

    # Design the form for adding a product
    tk.Label(add_window, text="Name:").pack()
    name_entry = tk.Entry(add_window)
    name_entry.pack()

    tk.Label(add_window, text="Description:").pack()
    description_entry = tk.Entry(add_window)
    description_entry.pack()

    tk.Label(add_window, text="Price:").pack()
    price_entry = tk.Entry(add_window)
    price_entry.pack()

    tk.Label(add_window, text="Quantity:").pack()
    quantity_entry = tk.Entry(add_window)
    quantity_entry.pack()

    def save_product():
        name = name_entry.get()
        description = description_entry.get()
        price = float(price_entry.get())
        quantity = int(quantity_entry.get())

        cursor.execute("INSERT INTO products (name, description, price, quantity) VALUES (?, ?, ?, ?)",
                       (name, description, price, quantity))
        conn.commit()
        add_window.destroy()
        messagebox.showinfo("Success", "Product added successfully!")

    tk.Button(add_window, text="Save", command=save_product).pack()

def view_products():
    # Create a new window for viewing products
    view_window = tk.Toplevel(root)
    view_window.title("View Products")

    # Design a listbox to display products
    product_listbox = tk.Listbox(view_window, width=50)
    product_listbox.pack()

    cursor.execute("SELECT id, name FROM products")
    products = cursor.fetchall()
    for product in products:
        product_listbox.insert(tk.END, f"{product[0]} - {product[1]}")

def main():
    # Create the main menu
    menu_frame = tk.Frame(root)
    menu_frame.pack()

    add_button = tk.Button(menu_frame, text="Add Product", command=add_product)
    add_button.pack()

    view_button = tk.Button(menu_frame, text="View Products", command=view_products)
    view_button.pack()

    exit_button = tk.Button(menu_frame, text="Exit", command=root.destroy)
    exit_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()