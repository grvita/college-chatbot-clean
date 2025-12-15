import sqlite3
import os

def get_connection():
    # project root: C:\Users\kaser\Downloads\college-chatbot-clean
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    db_path = os.path.join(root_dir, "database", "college.db")

    # Create folder if missing
    os.makedirs(os.path.dirname(db_path), exist_ok=True)

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn
