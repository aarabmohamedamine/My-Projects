import sqlite3

connection = sqlite3.connect("test_database.db")
cursor = connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    phone TEXT,
    email TEXT
)
""")
# Execute SQL query to insert data
cursor.execute("""
INSERT INTO contacts (name, phone, email) 
VALUES ('Ahmed', '0612345678', 'ahmed@email.com')
""")

# IMPORTANT: We must commit (save) the changes to the hard drive!
connection.commit()
print("Contact added successfully!")

connection.close()