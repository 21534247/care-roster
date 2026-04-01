import sqlite3

conn = sqlite3.connect("careroster.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS participants (
    participant_id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    phone TEXT,
    address TEXT,
    support_needs TEXT,
    emergency_contact TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS support_workers (
    worker_id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    phone TEXT,
    email TEXT,
    availability TEXT,
    qualification_status TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS shifts (
    shift_id INTEGER PRIMARY KEY AUTOINCREMENT,
    participant_id INTEGER,
    worker_id INTEGER,
    shift_date TEXT,
    start_time TEXT,
    end_time TEXT,
    location TEXT,
    status TEXT,
    FOREIGN KEY (participant_id) REFERENCES participants(participant_id),
    FOREIGN KEY (worker_id) REFERENCES support_workers(worker_id)
)
""")

conn.commit()
conn.close()

print("Database and tables created successfully.")
