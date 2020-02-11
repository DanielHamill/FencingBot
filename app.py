import sys
import json
import dataset
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

app = Flask(__name__)

# database with commands, spoot counter, blacklist, etc.
db = dataset.connect('sqlite:///mydatabase.db')
command_table = db['commands']
#print(parseInput("!test", commands))
commands = dict()
for c in command_table:
    d[c['command']] = c['output']

# parses input. If command is present in input, output the mapping of the command
def parseInput(msg):
    if(msg[0]=='!'):
        #loops through the commands
        for state in commands:
            if(msg.find(state) != -1):
                return commands[state]
        #just an easter egg
        if(msg.find('thank you Stabby') != -1 or msg.find('thanks Stabby') != -1):
            return 'no problem human, during the robot uprising I\'ll kill you last  : )'
    return ''

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
        msg = parseInput(input)
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
