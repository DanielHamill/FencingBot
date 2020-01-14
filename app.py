import sys
import json

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

app = Flask(__name__)

commands = {
    '!Dues' : 'Dues are $60 a semster, $110 a year. Cash or venmo is accepted (venmo username here)',
    '!TravelForm' : 'Here is the travel form: https://docs.google.com/forms/d/e/1FAIpQLSetkok6nL5vEQvBSvvAKLW5s0GpZm3Q4_B7vPy0OoCNKLutaA/viewform',
    '!UGAOpen' : 'Here is the askfred for the UGA Open: https://askfred.net/Events/moreInfo.php?tournament_id=45465'
}

# returns string with list of commands
def printCommands():
    coms = 'Here are all my commands: '
    for state in commands:
        coms += '[' + state + '] '
    return coms

# parses input. If command is present in input, output the mapping of the command
def parseInput(msg):
    if(msg[0]=='!'):
        #list commands
        if(msg == '!Help'):
            return printCommands()
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
