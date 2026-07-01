import sqlite3

print("Database file started...")


def create_database():
    conn = sqlite3.connect("resumeiq.db")

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()

    print("Database Created Successfully!")


if __name__ == "__main__":
    create_database()