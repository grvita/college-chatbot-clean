from backend.database import get_connection

def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS faqs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            keywords TEXT,
            question TEXT NOT NULL,
            answer TEXT NOT NULL,
            category TEXT
        )
    """)
    
    conn.commit()
    conn.close()
    print("Database table created successfully!")

if __name__ == "__main__":
    create_table()
