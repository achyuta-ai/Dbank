from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return {'message':'Welcome to DBank'}

if __name__ == '__main':
    app.run(debug=True)