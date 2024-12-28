from flask import Flask, render_template

app = Flask(__name__)

# Route for the main page (landing or index page)
@app.route('/')
def index():
    return render_template('index.html')  # Renders index.html as the home/landing page

# Route for the "Get Started" page (which could be your home or another page)
@app.route('/home')
def home():
    return render_template('home.html')  # Renders home.html for the "Get Started" page

if __name__ == '__main__':
    app.run(debug=True)
