from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Connect to MySQL database
db = mysql.connector.connect(
    host="your_host",
    user="your_username",
    password="your_password",
    database="your_database"
)
cursor = db.cursor()

# Define routes
@app.route('/')
def index():
    cursor.execute("SELECT * FROM merchandise")
    merchandise = cursor.fetchall()
    return render_template('index.html', merchandise=merchandise)

@app.route('/add_merchandise', methods=['POST'])
def add_merchandise():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']
        quantity = request.form['quantity']
        cursor.execute("INSERT INTO merchandise (name, description, price, quantity) VALUES (%s, %s, %s, %s)", (name, description, price, quantity))
        db.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
