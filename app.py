from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Configures the database file
app.config['SECRET_KEY'] = 'your_secret_key'  # Needed for session management and security
db = SQLAlchemy(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/tutor')
def tutor_dashboard():
    return render_template('tutor_dashboard.html')

@app.route('/student')
def student_dashboard():
    return render_template('student_dashboard.html')


if __name__ == '__main__':
    app.run(debug=True)

