from flask import Flask, request
import requests

app = Flask(__name__)

def send():
    info = {
    "bot_id"  : "9441ec69d3223735bd84ef90eb",
    "text"    : "response"
    }
    r = requests.post('https://api.groupme.com/v3/bots/post', data=info)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/', methods=['POST'])
def result():
    send()
    return 'Received !' # response to your request.

if __name__ == '__main__':
    app.run(host='https://daniel-bot-test.herokuapp.com/', port=80)
