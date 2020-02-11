import dataset

db = dataset.connect('sqlite:///mydatabase.db')
commands = {}

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

def insert_commands():
    table = db['commands']
    table.insert(dict(command='!test', output='test command'))
    table.insert(dict(command='!Valentine', output='Here is the askfred for the UGA Valentine\'s Slasher: https://askfred.net/Events/moreInfo.php?tournament_id=46098'))
    table.insert(dict(command='!TravelForm', output='Here is the travel form: https://docs.google.com/forms/d/e/1FAIpQLSetkok6nL5vEQvBSvvAKLW5s0GpZm3Q4_B7vPy0OoCNKLutaA/viewform'))

def test():
    db = dataset.connect('sqlite:///mydatabase.db')
    command_table = db['commands']

    for c in command_table:
        commands[c['command']] = c['output']
    print(parseInput('!Valentine'))
test()
