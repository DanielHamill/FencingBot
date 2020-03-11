import dataset
from ParseInput import parseInput

db = dataset.connect('sqlite:///mydatabase.db')
commands = {}



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

insert_commands()
print(parseInput('!test'))
