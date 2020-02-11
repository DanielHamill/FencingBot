# this file contains the parseInput function for the FencingBot. It is in a
# separate file so that it can be tested independantly from the main app

# the commands also go in this file

commands = {
    '!dues' : 'Dues are $60 a semster, $110 a year. Cash or venmo is accepted (venmo username here)',
    '!travelform' : 'Here is the travel form: https://docs.google.com/forms/d/e/1FAIpQLSetkok6nL5vEQvBSvvAKLW5s0GpZm3Q4_B7vPy0OoCNKLutaA/viewform',
    '!ugaopen' : 'Here is the askfred for the UGA Open: https://askfred.net/Events/moreInfo.php?tournament_id=45465'
}

# returns string with list of commands
def printCommands():
    coms = 'Here are all my commands: '
    for state in commands:
        coms += '[' + state + '] '
    return coms

# parses input. If command is present in input, output the mapping of the command
def parseInput(input):
    msg = input.lower()
    if(msg[0]=='!'):
        #list commands
        if(msg == '!help'):
            return printCommands()
        #loops through the commands
        for state in commands:
            if(msg.find(state) != -1):
                return commands[state]
        #just an easter egg
        if(msg.find('thank you Stabby') != -1 or msg.find('thanks Stabby') != -1):
            return 'no problem human, during the robot uprising I\'ll kill you last  : )'
    return ''
