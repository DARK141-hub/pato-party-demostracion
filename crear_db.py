
import sqlite3

conn = sqlite3.connect('comentarios.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS comentarios (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nombre TEXT NOT NULL,
  mensaje TEXT NOT NULL
);
''')

conn.commit()
conn.close()
