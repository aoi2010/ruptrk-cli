def sell_stock(conn, name, qty):
    cur = conn.cursor()
    cur.execute("SELECT id, qty, price FROM stocks WHERE name = ?", (name,))
    row = cur.fetchone()
    if not row:
        raise ValueError("Stock not found")
    stock_id, available, price = row
    if available < qty:
        raise ValueError("Not enough stock")

    total = price * qty
    cur.execute("UPDATE stocks SET qty = qty - ? WHERE id = ?", (qty, stock_id))
    cur.execute("INSERT INTO sales (stock_id, qty, total) VALUES (?, ?, ?)",
                (stock_id, qty, total))
    conn.commit()
    return total
