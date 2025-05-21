import sqlite3
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

DB_NAME = 'comentarios.db'

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/api/comentarios', methods=['GET'])
def obtener_comentarios():
    conn = get_db_connection()
    comentarios = conn.execute('SELECT * FROM comentarios').fetchall()
    conn.close()
    comentarios = [dict(row) for row in comentarios]
    return jsonify(comentarios)

@app.route('/api/comentarios', methods=['POST'])
def agregar_comentario():
    data = request.get_json()
    nombre = data.get('nombre')
    mensaje = data.get('mensaje')

    if nombre and mensaje:
        conn = get_db_connection()
        conn.execute('INSERT INTO comentarios (nombre, mensaje) VALUES (?, ?)', (nombre, mensaje))
        conn.commit()
        conn.close()
        nuevo = {'nombre': nombre, 'mensaje': mensaje}
        return jsonify(nuevo), 201
    else:
        return jsonify({'error': 'Datos incompletos'}), 400

if __name__ == '__main__':
    app.run(debug=True)
