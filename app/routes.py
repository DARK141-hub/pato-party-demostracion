
from flask import Blueprint, request, jsonify
from .database import get_db_connection

routes_bp = Blueprint('routes', __name__)

@routes_bp.route('/agendar', methods=['POST'])
def agendar():
    data = request.get_json()
    nombre = data.get('nombre')
    correo = data.get('correo')
    fecha = data.get('fecha')
    hora = data.get('hora')

    if not nombre or not correo or not fecha or not hora:
        return jsonify({'error': 'Faltan datos'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO citas (nombre, correo, fecha, hora) VALUES (?, ?, ?, ?)',
                   (nombre, correo, fecha, hora))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Cita agendada con éxito'}), 201
