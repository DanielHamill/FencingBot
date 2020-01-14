#hi ur cute

commands = {
    '!Dues' : 'Dues are $60 a semster, $110 a year. Cash or venmo is accepted (venmo username here)',
    '!TravelForm' : 'Here is the travel form: https://docs.google.com/forms/d/e/1FAIpQLSetkok6nL5vEQvBSvvAKLW5s0GpZm3Q4_B7vPy0OoCNKLutaA/viewform',
    '!UGAOpen' : 'Here is the askfred for the UGA Open: https://askfred.net/Events/moreInfo.php?tournament_id=45465'
}

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

msg = '!Help'

out = parseInput(msg)
print(out)
