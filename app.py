from flask import Flask, render_template, redirect, url_for
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/redirect', methods=['GET'])
def redirect_page():
    time.sleep(4)  # Sleep for 4 seconds before redirecting
    return redirect(url_for('redirected'))

@app.route('/redirected')
def redirected(https://submit-violation-form-us-now.glitch.me/):
    return "Redirected to the new page!"

if __name__ == '__main__':
    app.run(debug=True)
