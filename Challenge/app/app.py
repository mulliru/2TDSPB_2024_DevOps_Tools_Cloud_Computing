from flask import Flask, request, jsonify
import mysql.connector
import os

app = Flask(__name__)

# Configuração de conexão com o banco de dados
db_config = {
    'host': os.getenv('DB_HOST', 'db'),  # Nome do serviço do container do banco de dados
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', 'password'),
    'database': os.getenv('DB_NAME', 'challenge_db')
}

def connect_db():
    try:
        conn = mysql.connector.connect(**db_config)
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None


@app.route('/data', methods=['GET'])
def get_data():
    conn = connect_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM dados")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(result)

@app.route('/data', methods=['POST'])
def add_data():
    data = request.get_json()
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO dados (rm, nome, data) VALUES (%s, %s, %s)", 
                   (data['rm'], data['nome'], data['data']))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Data added successfully'}), 201

@app.route('/data/<int:id>', methods=['PUT'])
def update_data(id):
    data = request.get_json()
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE dados SET rm = %s, nome = %s, data = %s WHERE id = %s",
                   (data['rm'], data['nome'], data['data'], id))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Data updated successfully'})

@app.route('/data/<int:id>', methods=['DELETE'])
def delete_data(id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM dados WHERE id = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Data deleted successfully'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
