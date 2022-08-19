def display_board(board):
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])

def player_input():
    
    marker = ''
    
    while marker != 'X' and marker != 'O':
        marker = input('Player 1, input value of  X or O: ')
    
    player1 = marker
    
    if player1 == 'X':
        player2 ='O'
    else:
        player2 = 'X'
        
    print(f'Player 1 is : {player1}')
    print(f'Player 2 is : {player2}')
    
    return (player1,player2)

def place_marker(board, marker, position):
    
    board[position] = marker

def win_check(board,marker):
    
    return (board[1] == marker and board[2] == marker and board[3] == marker or
            board[4] == marker and board[5] == marker and board[6] == marker or
            board[7] == marker and board[8] == marker and board[9] == marker or
            board[1] == marker and board[4] == marker and board[7] == marker or
            board[2] == marker and board[5] == marker and board[8] == marker or
            board[3] == marker and board[6] == marker and board[9] == marker or 
            board[1] == marker and board[5] == marker and board[9] == marker or
            board[3] == marker and board[5] == marker and board[7] == marker)

import random

def choose_first():
    
    flip = random.randint(0,1)
    
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board,position):
    
    return board[position] == ' '

def full_board_check(board):
    
    for i in range(1,10):
        if space_check(board,i):
            return False
    
    return True 

def player_choice(board):
    
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Choose a position (1-9): '))
        
    return position

def replay():
    
    choice = input('Play again?: yes or no')
    return choice == 'yes'

print('Tic-Tac-Toe')

while True:
    
    the_board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    player1_marker, player2_marker = player_input()
    
    turn = choose_first()
    print(turn+' will go first')
    
    play_game = input('Ready? y or n')
    if play_game == 'y':
        game_on = True
    else:
        game_on = False
        
    while game_on:
        
        if turn == 'Player 1':
            
            display_board(the_board)
            
            position = player_choice(the_board)
            
            place_marker(the_board,player1_marker,position)
            
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('Player 1 has won!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board()
                    print('Tie Game!')
                    game_on = False
                else:
                    turn = 'Player 2'
        else:
            
            display_board(the_board)
            
            position = player_choice(the_board)
            
            place_marker(the_board,player2_marker,position)
            
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board()
                    print('Tie Game!')
                    game_on = False
                else:
                    turn = 'Player 1'
            
                
    
    if not replay():
        break
        
        