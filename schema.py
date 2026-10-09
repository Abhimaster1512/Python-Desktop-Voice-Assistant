from database.connection import get_connection


def create_tables():

    conn = get_connection()
    cursor = conn.cursor()


    # User Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)


    # Notes Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS notes(
            note_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            title TEXT,
            content TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(user_id)
            REFERENCES users(user_id)
        )
    """)


    # Reminder Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reminders(
            reminder_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            task TEXT,
            reminder_time TEXT,
            status TEXT DEFAULT 'pending',
            FOREIGN KEY(user_id)
            REFERENCES users(user_id)
        )
    """)


    # Command History
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS history(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            command TEXT,
            response TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(user_id)
            REFERENCES users(user_id)
        )
    """)


    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_tables()
    print("Database created successfully")