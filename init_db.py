import sqlite3
connection = sqlite3.connect('biblioteca.db')
with open('schema.sql') as f:
    connection.executescript(f.read())
print("✅ Banco criado!")
connection.close()