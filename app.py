from flask import Flask, render_template

app = Flask(__name__)

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

