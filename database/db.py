import sqlite3

DB_PATH = "database/neural_logs.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS neural_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            signal TEXT NOT NULL,
            status TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def log_signal(signal: str, status: str):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO neural_logs (signal, status)
        VALUES (?, ?)
    ''', (signal, status))
    conn.commit()
    conn.close()

