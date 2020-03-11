import time

calls = []

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
