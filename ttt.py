from IPython.display import clear_output
import random

#function to display a board.
def display_board(board):
    clear_output()  # Remember, this only works in jupyter!
    
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')    
    
#function to assign marker to players 
def player_input():
    marker = ''
    while marker != 'x' and marker != 'o':
        marker = input('player 1, choose x or o: ')

    if marker == 'x':    
        return ('x','o')
    else:
        return ('o','x')

#function to place cselected marker in chose position.
def place_marker(board,marker,position):
    board[position] = marker
    
#function to see weather the selected player has won or lost
def win_check(board,mark):
    #conditions to win are 
    #check all rows 
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or 
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    (board[7] == mark and board[8] == mark and board[9] == mark) or
    #check all coloumns
    (board[7] == mark and board[4] == mark and board[1] == mark) or
    (board[8] == mark and board[5] == mark and board[2] == mark) or
    (board[9] == mark and board[6] == mark and board[3] == mark) or
    #check two diagonals 
    (board[7] == mark and board[5] == mark and board[3] == mark) or
    (board[9] == mark and board[5] == mark and board[1] == mark))

#writing a function using the random module to decide which player goes first
def who_first():
    flip = random.randint(0,1)
    if flip == 0:
        return 'player 1'
    else:
        return 'player 2'

#function to check if player chosen space is available
def space_check(board,position):
    return board[position] == ''

#function to check weather a board is full
def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False    
    return True
        
#function to ask for players next postion and use the prvious function to check weather board is empty at that position
#if empty return the position for using
def player_choise(board):
    position = 0
    
    while position not in range(1,10) or not space_check(board,position):
        position = int(input('choose a position: (1-9)'))
        return position 
    
#function to see if the players want to play again.
def replay():
    choise = input('play again? enter yes or no')
    return choise == 'yes'
   
   #game logicc
       
#while loop to keep running the game
print('Welcome to Tic Tack TOE')
while True:
    
    the_board = ['']*10
    player1_input_type, player2_input_type = player_input()
    turn = who_first()
    print(turn + 'will go first')
    begin_game = input('ready to play? y or n?')
    
    if begin_game == 'y':
        game_on = True
    else:
        game_on = False
        
    while game_on == True:
        
            if turn == 'player 1':
                #showing the board
                display_board(the_board)
                #letting player choose a position
                position = player_choise(the_board)
                #placeing the marker on the selected position
                place_marker(the_board,player1_input_type,position)
                if win_check(the_board,player1_input_type):
                    display_board(the_board)
                    print('player 1 has won')
                    game_on = False
                else:
                    if full_board_check(the_board):
                        display_board(the_board)
                        print('tie game')
                        game_on = False
                    else:
                        turn = 'player 2'            
            
            else:
                #showing the board
                display_board(the_board)
                #letting player choose a position
                position = player_choise(the_board)
                #placeing the marker on the selected position
                place_marker(the_board,player2_input_type,position)
                if win_check(the_board,player2_input_type):
                    display_board(the_board)
                    print('player 2 has won')
                    game_on = False
                else:
                    if full_board_check(the_board):
                        display_board(the_board)
                        print('tie game')
                        game_on = False
                    
                    else:
                        turn = 'player 1'    
                        


    if not replay():
        break