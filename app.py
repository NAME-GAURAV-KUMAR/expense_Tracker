from flask import Flask, render_template, request, jsonify
import mysql.connector

app = Flask(__name__)

# Set your initial balance here (can be dynamic later)
INITIAL_BALANCE = 10000  # Example initial balance

# Database Connection
def get_db_connection():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password=' ',
        database='org'
    )
    return conn

# Initialize Database Table
def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            amount FLOAT NOT NULL,
            date DATE NOT NULL
        )
    ''')
    conn.commit()
    cursor.close()
    conn.close()

init_db()

# Home Route
@app.route('/')
def index():
    return render_template('index.html', initial_balance=INITIAL_BALANCE)

# API to get all expenses
@app.route('/api/expenses', methods=['GET'])
def get_expenses():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM expenses')
    expenses = [{'id': row[0], 'title': row[1], 'amount': float(row[2]), 'date': str(row[3])} for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return jsonify(expenses)

# API to add a new expense
@app.route('/api/expenses', methods=['POST'])
def add_expense():
    data = request.json
    title = data['title']
    amount = data['amount']
    date = data['date']

    conn = get_db_connection()
    cursor = conn.cursor()
    sql = 'INSERT INTO expenses (title, amount, date) VALUES (%s, %s, %s)'
    val = (title, amount, date)
    cursor.execute(sql, val)
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Expense added successfully!'})

# API to delete an expense
@app.route('/api/expenses/<int:id>', methods=['DELETE'])
def delete_expense(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = 'DELETE FROM expenses WHERE id = %s'
    val = (id,)
    cursor.execute(sql, val)
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Expense deleted successfully!'})

# API to get remaining balance
@app.route('/api/balance', methods=['GET'])
def get_balance():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT SUM(amount) FROM expenses')
    total_expenses = cursor.fetchone()[0] or 0  # In case there are no expenses yet
    remaining_balance = INITIAL_BALANCE - total_expenses
    cursor.close()
    conn.close()
    return jsonify({'remaining_balance': remaining_balance})

if __name__ == '__main__':
    app.run(debug=True)
