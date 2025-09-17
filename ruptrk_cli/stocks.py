def add_stock(conn, name, qty, price):
    cur = conn.cursor()
    cur.execute("INSERT OR REPLACE INTO stocks (name, qty, price) VALUES (?, ?, ?)",
                (name, qty, price))
    conn.commit()

def restock(conn, name, qty):
    cur = conn.cursor()
    cur.execute("UPDATE stocks SET qty = qty + ? WHERE name = ?", (qty, name))
    conn.commit()

def view_stocks(conn):
    cur = conn.cursor()
    cur.execute("SELECT id, name, qty, price FROM stocks")
    return cur.fetchall()

def edit_stock(conn, name, price):
    cur = conn.cursor()
    cur.execute("UPDATE stocks SET price = ? WHERE name = ?", (price, name))
    conn.commit()

def delete_stock(conn, name):
    cur = conn.cursor()
    cur.execute("DELETE FROM stocks WHERE name = ?", (name,))
    conn.commit()
