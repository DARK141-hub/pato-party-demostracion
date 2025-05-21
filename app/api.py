from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

DATABASE = 'citas.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/api/citas', methods=['POST'])
def crear_cita():
    data = request.get_json()
    conn = get_db_connection()
    conn.execute('INSERT INTO citas (nombre, correo, fecha, hora, motivo) VALUES (?, ?, ?, ?, ?)',
                 (data['nombre'], data['correo'], data['fecha'], data['hora'], data['motivo']))
    conn.commit()
    conn.close()
    return jsonify({"mensaje": "Cita creada con éxito"}), 201

@app.route('/api/citas', methods=['GET'])
def obtener_citas():
    conn = get_db_connection()
    citas = conn.execute('SELECT * FROM citas').fetchall()
    conn.close()
    return jsonify([dict(row) for row in citas])

if __name__ == '__main__':
    app.run(debug=True)
