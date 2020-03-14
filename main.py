# import numpy as np
import sys

print('Tic Tac Toe')

turn = 0 # even is 'X', odd is 'O'
player = 'X'
win_detected = 0 # 0 = no, 1 = tie, 2 = x wins, 3 = o wins
game_board = [['', '', ''],['', '', ''],['', '', '']]
move_row = None
move_col = None

def print_board(game_board):
    for row in game_board:
        for cell in row:
            if cell != '':
                print(cell + ' ', end='')
            else:
                print('- ', end='')
        print()

def check_win(game_board, last_move, turn):
    if turn < 8:
        return 0
    return 1    

while win_detected == 0:
    print()
    while True:
        if turn%2 == 0:
            player = 'X'
        else:
            player = 'O'

        print(player + "'s turn. Enter the row where you would like to make a move, 0 indexed.")
        move_row = int(sys.stdin.readline())
        if move_row <= 2:
            break

    while True:
        print("Enter the column where you would like to make a move, 0 indexed.")
        move_col = int(sys.stdin.readline())
        if move_col <= 2:
            break

    game_board[move_row][move_col] = player
    print_board(game_board)

    win_detected = check_win(game_board, (move_row, move_col), turn) # change tuple to be last move
    if win_detected == 1:
        print('Tie Game!')
    elif win_detected == 2:
        print ('X wins!')
    elif win_detected == 3:
        print('O wins!')

    turn += 1
