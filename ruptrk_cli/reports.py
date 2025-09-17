def sales_report(conn):
    cur = conn.cursor()
    cur.execute("""SELECT s.id, st.name, s.qty, s.total, s.ts
                   FROM sales s
                   JOIN stocks st ON s.stock_id = st.id
                   ORDER BY s.ts DESC""")
    return cur.fetchall()

def stock_summary(conn):
    cur = conn.cursor()
    cur.execute("SELECT name, qty, price FROM stocks")
    return cur.fetchall()
