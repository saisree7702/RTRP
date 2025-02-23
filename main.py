from flask import Flask, render_template, request, redirect, session
import pymysql

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Database connection
def get_db_connection():
    return pymysql.connect(host='localhost', user='root', password='', database='freelance')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, role, profile_created FROM login WHERE email=%s AND password=%s", (email, password))
    user = cursor.fetchone()
    conn.close()

    if user:
        session['user_id'] = user[0]
        session['role'] = user[1]

        if user[1] == 'Freelancer':
            if user[2]:  # profile_created = TRUE
                return redirect('/freelancer_dashboard')
            else:
                return redirect('/create_profile')
        else:
            return redirect('/client_dashboard')
    else:
        return "Invalid credentials"

@app.route('/create_profile', methods=['GET', 'POST'])
def create_profile():
    if request.method == 'POST':
        user_id = session['user_id']
        skills = request.form['skills']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE login SET profile_created = TRUE WHERE id = %s", (user_id,))
        conn.commit()
        conn.close()

        return redirect('/freelancer_dashboard')

    return render_template('create_profile.html')

@app.route('/freelancer_dashboard')
def freelancer_dashboard():
    return render_template('freelancer_dashboard.html')

@app.route('/client_dashboard')
def client_dashboard():
    return render_template('client_dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
