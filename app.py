import sys
import json

from urllib.parse import urlencode
from urllib.request import Request, urlopen
from flask import Flask, request

import ParseInput as parse

app = Flask(__name__)

# executes if app gets POST request. Parses and sends message
@app.route('/', methods=['POST'])
def webhook():
    # gets data from post
    data = request.get_json()
    log('Recieved {}'.format(data))

    # We don't want to reply to ourselves!
    if data['name'] != 'Stabby':
        input = data['text']
        # parses commands from input
        msg = parse.parseInput(input)
        if(msg != ''):
            send_message(msg)

    return "ok", 200

# sends message in body of post to Group.me api
def send_message(msg):
    url  = 'https://api.groupme.com/v3/bots/post'

    data = {
          'bot_id' : '9441ec69d3223735bd84ef90eb',
          'text'   : msg,
         }

    # sends post request
    request = Request(url, urlencode(data).encode())
    json = urlopen(request).read().decode()

def log(msg):
    print(str(msg))
    sys.stdout.flush()
