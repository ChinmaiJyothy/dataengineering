'''from flask import Flask, jsonify, g
import mysql.connector

app = Flask(__name__)

def get_db():
    if 'db' not in g:
        g.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root123",
            database="joinassign"
        )
    return g.db

@app.route('/employee/<int:EmployeeID>', methods=['GET'])
def get_employee(EmployeeID):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM employee WHERE EmployeeID = %s", (EmployeeID,))
    employee = cursor.fetchone()
    cursor.close()

    if employee:
        return jsonify(employee), 200
    else:
        return jsonify({"message": "Employee not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
'''
from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

# MySQL Database Configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root123',
    'database': 'joinassign',
}

# Function to connect to MySQL and execute a query
def query_database(query, data=None):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor(dictionary=True)

    try:
        if data:
            cursor.execute(query, data)
        else:
            cursor.execute(query)

        result = cursor.fetchall()
        return result

    finally:
        cursor.close()
        connection.close()
# API endpoint to get employee data by ID
@app.route('/employee/<int:EmployeeID>', methods=['GET'])
def get_employee_by_id(EmployeeID):
    query = 'SELECT * FROM employee WHERE EmployeeID = %s'
    data = (EmployeeID,)
    result = query_database(query, data)

    if not result:
        return jsonify({'error': 'Employee not found'}), 404

    return jsonify(result[0])

if __name__ == '__main__':
    app.run(debug=True)
