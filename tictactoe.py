"""
    This is a tic tac toe game made by Abhishek.   
"""
import random

def choose_first():
    go_first = random.randint(1, 2)
    print(f'Player {go_first} will go first by random choice')
    return f'P{go_first}'

def win_check(board, mark):
    return ((board[0] == mark and board[1] == mark and board[2] == mark) or
            (board[3] == mark and board[4] == mark and board[5] == mark) or 
            (board[6] == mark and board[7] == mark and board[8] == mark) or 
            (board[0] == mark and board[3] == mark and board[6] == mark) or 
            (board[2] == mark and board[5] == mark and board[8] == mark) or 
            (board[1] == mark and board[4] == mark and board[7] == mark) or 
            (board[0] == mark and board[4] == mark and board[8] == mark) or 
            (board[2] == mark and board[4] == mark and board[6] == mark) 
            )

def display_board(board):
    print(' {} | {} | {} '.format(board[0], board[1], board[2]))
    print('-----------')
    print(' {} | {} | {} '.format(board[3], board[4], board[5]))
    print('-----------')
    print(' {} | {} | {} '.format(board[6], board[7], board[8]))

def user_input():
    ini=True
    while ini:  
        player1 = input("Player 1, Please pick a marker 'X' or 'O': ")
        if player1 not in ['X','O']:
            print('Enter valid value')
        else:
            ini=False
            if player1 == 'X':
                player2 = 'O'
            elif player1 == 'O':
                player2 = 'X'
    print(f'Player 2 is {player2}')
    return player1, player2

def place_marker(board, marker, Turn):
    try:
       pos_r= range(9) 
       #print(pos_r)
       if Turn =='P1': t = 'Player 1'
       else: t = 'Player 2'
       vrexcept=False
       while not vrexcept:
            position = int(input(t+ ': Enter the position to put the value: '))
            if position not in pos_r:
                print('Enter valid Number in range')
            elif not space_check(board,position):
                print('Position already filled') 
            else:
                board[position]=marker
                vrexcept=True
    except ValueError:
        print('Enter valid number ')
        
def space_check(board, position):
    if board[position] in ['X','O']:    
        return False
    return True
    
def replay():
    ini=True
    while ini:  
        rep_q = input('Do you want to replay? Y or N: ')
        if rep_q not in ['Y','N']:
            print('Enter valid value')
        else:
            ini=False
    if rep_q == 'Y':
        return True
    else: 
        return False 

def full_board_check(board):
    for i in board:
        if i in ['X','O']:
            continue
        else: 
            return False
    return True

        
if __name__ == "__main__":
    print("Welcome to my Abhishek's tic tac toe game!!! \n")

    while True:
        game_on=True
        print('Start the game!')
        board1 = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
        # Set the game up here
        display_board(board1)
        p1m,p2m=user_input()
        Turn = choose_first()
        
        while game_on :        
        
            # Player 1 Turn
            if Turn =='P1':
                place_marker(board1,p1m, Turn)
                display_board(board1)
                if full_board_check(board1):
                    print('Board is Full.')
                    if replay():
                        board1 = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
                        display_board(board1)
                        p1m, p2m = user_input()
                        Turn = choose_first()
                    else:
                        game_on = False
                
                
                if win_check(board1,p1m):
                    print('Congratulations, Player 1 has won the game')
                    game_on = False
                Turn='P2'
            # Player 2's turn.
            elif Turn =='P2':
                place_marker(board1,p2m, Turn)
                display_board(board1)
                if full_board_check(board1):
                    print('Board is Full.')
                    if replay():
                        board1 = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
                        display_board(board1)
                        p1m, p2m = user_input()
                        Turn = choose_first()
                    else:
                        game_on = False
                if win_check(board1,p2m):
                    print('Congratulations, Player 2 has won the game')
                    game_on = False
                Turn='P1'

        if not replay():
            break
