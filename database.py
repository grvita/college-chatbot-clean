# database.py (same level as server.py and backend/)
import sqlite3
import os

def get_connection():
    db_path = os.path.join(os.path.dirname(__file__), 'college_data.db')
    conn = sqlite3.connect(db_path, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn
