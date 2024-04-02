rooms = {
    '1st corridor': { 
        'right': 'dead end',
        'left': 'intersection 1'
    },
    'intersection 1': {
        'straight': '2nd corridor'
    },
    '2nd corridor': {
        'straight': 'trolls lair',
        'right': 'intersection 2'
    },
    'intersection 2': {
        'right': '3rd corridor'
    },
    '3rd corridor': {
        'right': ' intersection 3'
    },
    'intersection 3':{
        'straight': 'intersection 4'
    },
    'intersection 4':{
        'left': 'challenge room',
        'right': '4th corridor'
    },
    '4th corridor': {
        'right': 'intersection 5'
    },
    'intersection 5': {
        'straight': '5th corridor',
        'right': 'dead end 2'
    },
    '5th corridor': {
        'left': 'intersection 6'
    },
    'intersection 6': {
        'left': 'locked door 1',
        'straight': 'locked door 2'
    },
    'locked door 1': {
        'left': 'dead end 3'
    },
    'locked door 2': {
        'straight': 'intersection 7'
    },
    'intersection 7': {
        'right': 'treasure room'
    },
    'treasure room': 'Final Room'
    }

def showStatus(currentRoom):
    """determine the current status of the player"""
    # print the player's current location
    print('---------------------------')
    print('You are in the ' + currentRoom)
def showInstruction():
    """Show the game instructions when called"""
    #!print a main menu and the commands
    print('''
    RPG Game
    By: Merchpup
    ========
    Commands:
        go [direction]
        get [item]
    ''')
#start
currentRoom = '1st corridor'

showInstruction()
#Game flow
while currentRoom != 'Final Room':
    showStatus(currentRoom)
#Get user input
    choice = input('> ') 

    move = choice.lower().split(' ', 1)
        
    if move [0] == 'go':
            #move[0] = move[0].lower()
        if len(move) == 2 and move[1].lower() in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1].lower()]
            print('You have moved to', currentRoom)
        else:
            print("You can/'t go that way!")
#End of Game
print('Final Room')
