available_exit = ['north', 'south', 'east', 'west']

chosen_exit = ''
while chosen_exit not in available_exit:
    chosen_exit = input('pleas enter a direction: ')
    if chosen_exit.upper() == 'QUIT':
        print('Game over')
        break
else:
    print('you exited')
