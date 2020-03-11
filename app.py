import sys
import json
import dataset
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from ParseInput import parseInput
from freq_counter import call
from flask import Flask, request

app = Flask(__name__)
cooldown = False

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

        if(call(5, 60)):
            msg = parseInput(input)
            cooldown = False
        elif(not cooldown):
            cooldown = True
            msg = 'Woah woah woah slow down... don\'t you have better things to do than spam me with commands?'
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
