from random import choice, randrange

def get_input():
    while True:
        try:
            nb_of_games = int(input('How many times do you want to play? '))
            if nb_of_games <= 0:
                raise ValueError
            break
        except ValueError:
            print('Wrong input, try again')
    while True:
        switch = input('Do you want to switch? ')
        if switch.istitle():
            switch = switch.lower()
        if switch in {'yes', 'y'}:
            switch = True
            break
        if switch in {'no', 'n'}:
            switch = False
            break
        print('Wrong input, try again')
    return nb_of_games, switch




nb_of_games, switch = get_input()
nb_of_wins = 0

for i in range(nb_of_games):
    doors = ['A', 'B', 'C']
    winning_door = choice(doors)
    print('Winning door happens to be', winning_door)
    first_choice = doors.pop(randrange(3))
    print('Contestant first chooses', first_choice)    
    if not switch:
        second_choice = first_choice
    if first_choice == winning_door:
        door_opened_by_host = doors.pop(randrange(2))
        if switch:
            second_choice = doors[0]
        else:
            nb_of_wins += 1
    else:
        doors.remove(winning_door)
        door_opened_by_host = doors[0]
        if switch:
            second_choice = winning_door
            nb_of_wins += 1
    print('Host opens', door_opened_by_host)
    print('As contestant',
          'switches,' if switch else 'does not switch,',
          'door finally opened is',
          second_choice
         )
    print()
    print(f'Proportion of wins: {nb_of_wins / nb_of_games:.2f}')