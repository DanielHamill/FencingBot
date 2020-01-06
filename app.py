import json

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

app = Flask(__name__)

def send_message(msg):
    url  = 'https://api.groupme.com/v3/bots/post'

    data = {
            'bot_id' : '9441ec69d3223735bd84ef90eb',
            'text'   : 'response',
            }
    request = Request(url, urlencode(data).encode())
    json = urlopen(request).read().decode()


@app.route('/', methods=['POST'])
def webhook():
  data = request.get_json()

  # We don't want to reply to ourselves!
  if data['name'] != 'apnorton-test-bot':
    msg = '{}, you sent "{}".'.format(data['name'], data['text'])
    send_message(msg)

  return "ok", 200
