from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def redirect_page():
    return render_template('https://click-here-to-fb-help-center.glitch.me/')

if __name__ == '__main__':
    app.run(debug=True)
