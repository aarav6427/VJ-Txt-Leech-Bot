from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '🏴‍☠️ W A C K Y 🏴‍☠️'


if __name__ == "__main__":
    app.run()
