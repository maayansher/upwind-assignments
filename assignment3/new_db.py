import sqlite3

# Connect to SQLite database (this creates the file if it doesn't exist)
conn = sqlite3.connect('users.db')

# Create a cursor to run SQL commands
cursor = conn.cursor()

# Create a table called 'users'
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
''')

# Insert a sample user
cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ('admin', 'admin123'))

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database created and user added!")
