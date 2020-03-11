import time
import sys
import json
import dataset
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from ParseInput import parseInput
from flask import Flask, request

calls = []
cooldown = False

def webhook():

    # We don't want to reply to ourselves!
    if True:
        input = '!test'
        # parses commands from input
        msg = ''
        if(call(5, 60)):
            msg = parseInput(input)
            global cooldown
            cooldown = False
        elif(not cooldown):
            cooldown = True
            msg = 'Woah woah woah slow down... don\'t you have better things to do than spam me with commands?'
        if(msg != ''):
            send_message(msg)

    return "ok", 200

# sends message in body of post to Group.me api
def send_message(msg):
    print(msg)

def log(msg):
    print(str(msg))
    sys.stdout.flush()


def call(max, duration):
    if(not too_frequent(max, duration)):
        calls.insert(0,time.time()-1583899800)
        return True
    else:
        return False

def too_frequent(max, duration):
    if(len(calls) >= max):
        if(calls[len(calls)-1]+duration > time.time()-1583899800):
            return True
        else:
            calls.remove(calls[len(calls)-1])
    return False

webhook()
webhook()
webhook()
webhook()
webhook()
webhook()
webhook()
