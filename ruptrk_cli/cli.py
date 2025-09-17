import argparse
from . import __version__, __author__
from .config import get_default_db, set_default_db, list_dbs
from .db import connect, init_db
from . import stocks, sales, reports

def main():
    parser = argparse.ArgumentParser(
        prog="ruptrk-cli",
        description="RUPTRK CLI - Simple inventory & sales tracker by Aoishik Khan"
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__} by {__author__}")

    subparsers = parser.add_subparsers(dest="command")

    # set default db
    p_db = subparsers.add_parser("setdb", help="Set default database")
    p_db.add_argument("name", help="Database name")

    # list dbs
    subparsers.add_parser("listdb", help="List available databases")

    # stock commands
    p_add = subparsers.add_parser("add", help="Add new stock")
    p_add.add_argument("name")
    p_add.add_argument("qty", type=int)
    p_add.add_argument("price", type=float)

    p_restock = subparsers.add_parser("restock", help="Restock item")
    p_restock.add_argument("name")
    p_restock.add_argument("qty", type=int)

    p_view = subparsers.add_parser("view", help="View stocks")

    p_edit = subparsers.add_parser("edit", help="Edit stock price")
    p_edit.add_argument("name")
    p_edit.add_argument("price", type=float)

    p_del = subparsers.add_parser("delete", help="Delete stock")
    p_del.add_argument("name")

    # sales
    p_sell = subparsers.add_parser("sell", help="Sell stock")
    p_sell.add_argument("name")
    p_sell.add_argument("qty", type=int)

    # reports
    subparsers.add_parser("sales-report", help="Show sales report")
    subparsers.add_parser("stock-summary", help="Show stock summary")

    args = parser.parse_args()

    if args.command == "setdb":
        set_default_db(args.name)
        print(f"Default DB set to {args.name}")
        return

    if args.command == "listdb":
        print("Available DBs:", list_dbs())
        return

    dbname = get_default_db()
    if not dbname:
        print("No default DB set. Use: ruptrk-cli setdb <dbname>")
        return

    conn = connect(dbname)
    init_db(conn)

    if args.command == "add":
        stocks.add_stock(conn, args.name, args.qty, args.price)
        print("Stock added.")
    elif args.command == "restock":
        stocks.restock(conn, args.name, args.qty)
        print("Stock updated.")
    elif args.command == "view":
        for row in stocks.view_stocks(conn):
            print(row)
    elif args.command == "edit":
        stocks.edit_stock(conn, args.name, args.price)
        print("Stock edited.")
    elif args.command == "delete":
        stocks.delete_stock(conn, args.name)
        print("Stock deleted.")
    elif args.command == "sell":
        total = sales.sell_stock(conn, args.name, args.qty)
        print(f"Sold! Total = {total}")
    elif args.command == "sales-report":
        for row in reports.sales_report(conn):
            print(row)
    elif args.command == "stock-summary":
        for row in reports.stock_summary(conn):
            print(row)
    else:
        parser.print_help()
