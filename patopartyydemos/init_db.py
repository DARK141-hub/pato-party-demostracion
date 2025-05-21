import sqlite3

conn = sqlite3.connect('citas.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS citas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    fecha TEXT NOT NULL,
    hora TEXT NOT NULL
)
''')

conn.commit()
conn.close()

