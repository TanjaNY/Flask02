from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import datetime
import os

app = Flask(__name__)

# Database connection configuration
BASE_DIR = os.getcwd()
db_path = os.path.join(BASE_DIR, "circle_calculations.db")


def get_db_connection():
    """
    Establishes a connection to the SQLite database.
    Returns:
        A sqlite3.Connection object representing the connection to the database.
    """
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row  # Allows accessing data by column names
    return conn

def create_table():
    """
    Creates the 'calculations' table in the SQLite database if it doesn't already exist.
    """
    conn = get_db_connection()
    conn.execute('''CREATE TABLE IF NOT EXISTS calculations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        radius REAL NOT NULL,
        area REAL NOT NULL,
        timestamp DATETIME NOT NULL
    )''')
    conn.commit()
    conn.close()




@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM calculations ORDER BY timestamp DESC')
    results = cursor.fetchall()
    conn.close()
    return render_template('index.html', results=results)


@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        radius = float(request.form['radius'])
        area = round(3.14159 * radius ** 2, 2)

        # Save calculation result and timestamp to database
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO calculations (radius, area, timestamp) VALUES (?, ?, ?)',
                       (radius, area, datetime.datetime.now()))
        conn.commit()
        conn.close()

        return render_template('index.html', radius=radius, result=area, success=True)
    except ValueError:
        return render_template('index.html', result=None, error="Invalid input")


@app.route('/delete/<int:calculation_id>', methods=['GET', 'POST'])
def delete(calculation_id):
    if request.method == 'POST':
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM calculations WHERE id = ?', (calculation_id,))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    else:
        # Display confirmation page before deletion (optional)
        return render_template('delete.html', calculation_id=calculation_id)


if __name__ == '__main__':
    # Establish a connection to the database
    conn = get_db_connection()

    # Create table only if it doesn't exist
    create_table()

    # Close the connection after creating the table
    conn.close()

    # Run the Flask application
    app.run(debug=True)
