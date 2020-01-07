import sys
import json

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

app = Flask(__name__)

commands = {
    '!test' : 'test command',
    '!UGAOpen' : 'Here is the askfred for the UGA Open: https://askfred.net/Events/moreInfo.php?tournament_id=45465',
    '!TravelForm' : 'Here is the travelForm'
}

def parseInput(msg):
    if(msg[0]=='!'):
        for state in commands:
            if(msg.find(state) != -1):
                return commands[state]
    return ''

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    log('Recieved {}'.format(data))

    # We don't want to reply to ourselves!
    if data['name'] != 'Stabby':
        input = data['text']
        msg = parseInput(input)
        if(msg != ''):
            send_message(msg)

    return "ok", 200

def send_message(msg):
    url  = 'https://api.groupme.com/v3/bots/post'

    data = {
          'bot_id' : '9441ec69d3223735bd84ef90eb',
          'text'   : msg,
         }
    request = Request(url, urlencode(data).encode())
    json = urlopen(request).read().decode()

def log(msg):
    print(str(msg))
    sys.stdout.flush()
