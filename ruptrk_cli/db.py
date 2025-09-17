import sqlite3
from .config import get_db_path

def connect(dbname: str):
    db_path = get_db_path(dbname)
    conn = sqlite3.connect(db_path)
    return conn

def init_db(conn):
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS stocks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE,
        qty INTEGER,
        price REAL
    )""")
    cur.execute("""CREATE TABLE IF NOT EXISTS sales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        stock_id INTEGER,
        qty INTEGER,
        total REAL,
        ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )""")
    conn.commit()
