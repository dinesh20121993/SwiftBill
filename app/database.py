from datetime import datetime
import sqlite3
import os

#set the database path
DATABASE_PATH = os.path.join("database","invoices.db")

insert_invoice_query = """
INSERT INTO invoices(client, total, filename, created_at)
VALUES (?, ?, ?, ?) 
"""

fetch_all_invoices_query = """
SELECT * FROM invoices ORDER BY created_at DESC 
"""
def insert_invoice_details_DB(client, total, filename):
    created_at = datetime.now().strftime('%Y%m%d%H%M%S')
    #connect to the database
    with sqlite3.connect(DATABASE_PATH) as conn:
        conn.execute(insert_invoice_query,(client, total, filename, created_at))
        conn.commit()

def get_all_Invoices():
    with sqlite3.connect(DATABASE_PATH) as conn:
        cursor = conn.execute(fetch_all_invoices_query)
        data = cursor.fetchall()
        return data