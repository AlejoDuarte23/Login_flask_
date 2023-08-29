
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Replace with your actual authentication logic
        if username == 'engineer1' and password == 'Mincka2023':
            return redirect('http://localhost:8000')  # Redirect to the Streamlit app
        else:
            return "Invalid credentials"
    return render_template('login.html')


if __name__ == '__main__':
    app.run(port=5000)
