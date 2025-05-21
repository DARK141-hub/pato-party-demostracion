from flask import Flask, render_template, request, jsonify
import sqlite3
import os

app = Flask(__name__)
DATABASE = 'citas.db'

def init_db():
    if not os.path.exists(DATABASE):
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS citas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                correo TEXT NOT NULL,
                fecha TEXT NOT NULL,
                hora TEXT NOT NULL
            )
        """)
        conn.commit()
        conn.close()

@app.route('/')
def calendario():
    return render_template('calendario.html')

@app.route('/agendar', methods=['POST'])
def agendar():
    data = request.form  # ← Aquí cambiamos a request.form para aceptar FormData

    nombre = data.get('nombre')
    correo = data.get('correo')
    fecha = data.get('fecha')
    hora = data.get('hora')

    if not all([nombre, correo, fecha, hora]):
        return jsonify({'error': 'Todos los campos son obligatorios'}), 400

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO citas (nombre, correo, fecha, hora) VALUES (?, ?, ?, ?)', (nombre, correo, fecha, hora))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Cita agendada correctamente'})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
