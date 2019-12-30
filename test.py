from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/', methods=['POST'])
def result():
    print('Requested') # should display 'bar'
    return 'Received !' # response to your request.

if __name__ == '__main__':
    app.run(host='10.0.0.148', port=5000)
