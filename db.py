import sqlite3

DB = "faceauto.db"

def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS registry (
        name TEXT,
        version TEXT
    )
    """)

    conn.commit()
    conn.close()
