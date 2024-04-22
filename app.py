from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'https://submit-violation-form-us-now.glitch.me/'

if __name__ == '__main__':
    app.run()
