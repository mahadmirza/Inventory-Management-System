import sqlite3

Connection = sqlite3.connect("inventory.db")

c = Connection.cursor()

c.execute("""
    CREATE TABLE products (
        id INTEGER PRIMARY KEY,
        name TEXT not NULL,
        description TEXT,
        price REAL,
        quantity INTEGER
)
""")

c.execute("""
    CREATE TABLE transactions (
          id INTEGER PRIMARY KEY,
          product_id INTEGER,
          quantity INTEGER,
          transaction_date TEXT,
          FOREIGN KEY (product_id) REFERENCES products(id)
    )
""")

Connection.commit()

def add_product(name, description, price, quantity):
    c.execute("INSERT INTO products (name, description, price, quantity) VALUES (?,?,?,?)", (name, description, price, quantity))
    Connection.commit()

def update_product(product_id, new_name, new_description, new_price, new_quantity):
    c.execute("""
        Update products
        SET name=?, description=?, price=?, quantity=?
        WHERE id=?
    """,(product_id, new_name, new_description, new_price, new_quantity))
    Connection.commit()

def record_transaction(product_id, quantity, transaction_date):
    c.execute("INSERT INTO transactions (product_id, quantity, transaction_date) VALUES (?,?,?)",(product_id, quantity, transaction_date))
    Connection.commit()

def get_product_details(product_id):
    c.execute("SELECT * FROM products WHERE id=?",(product_id))
    product = c.fetchone()
    return product

def get_all_products():
    c.execute("SELECT * FROM products")
    products = c.fetchall()
    return products

def get_transactions(product_id):
    c.execute("SELECT * FROM transactions WHERE product_id = ?",(product_id)) 
    transactions = c.fetchall()
    return transactions

Connection.close()