from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello Pritesh kaise hain aap!'


if __name__ == '__main__':
    app.run(host='0.0.0.0')