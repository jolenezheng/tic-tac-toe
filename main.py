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

# Checks the row, column, and diagonals (if applicable) of the most recent move
# Algorithm can be made much simpler with the use of a normal 1d array and listing out the 
# indexes of winning combinations, but I wanted to practice using 2d arrays so this will have to do...
def check_win(game_board, player, last_move, turn):
    index = last_move[1]
    matches = 0
    player_num = 2 # X

    if player == 'O':
        player_num = 3

    # Check row:
    # Left of curr x pos
    while (index - 1) >= 0:
        if game_board[last_move[0]][index - 1] == player:
            matches += 1
            index -= 1
        else:
            break

        if matches == 2:
            return player_num


    # Right of curr x pos
    index = last_move[1]
    while (index + 1) <= 2:
        if game_board[last_move[0]][index + 1] == player:
            matches += 1
            index += 1
        else:
            break

        if matches == 2:
            return player_num


    matches = 0

    #Check col:
    # Above curr y pos
    index = last_move[0]
    while (index - 1) >= 0:
        if game_board[index - 1][last_move[1]] == player:
            matches += 1
            index -= 1
        else:
            break
    
        if matches == 2:
            return player_num


    # Below curr y pos
    index = last_move[0]
    while (index + 1) <= 2:
        if game_board[index + 1][last_move[1]] == player:
            matches += 1
            index += 1
        else:
            break
        
        if matches == 2:
            return player_num


    matches = 0

    # Check diagonal: top left to bottom right
    # Towards top left
    index_row = last_move[0]
    index_col = last_move[1]
    while (index_row - 1) >= 0 and (index_col - 1) >= 0:
        if game_board[index_row - 1][index_col - 1] == player:
            matches += 1
            index_row -= 1
            index_col -= 1
        else:
            break

        if matches == 2:
            return player_num


    # Towards bottom right
    index_row = last_move[0]
    index_col = last_move[1]
    while (index_row + 1) <= 2 and (index_col + 1) <= 2:
        if game_board[index_row + 1][index_col + 1] == player:
            matches += 1
            index_row += 1
            index_col += 1
        else:
            break

        if matches == 2:
            return player_num


    matches = 0

    # Check diagonal: top right to bottom left
    # Towards top right
    index_row = last_move[0]
    index_col = last_move[1]
    while (index_row - 1) >= 0 and (index_col + 1) <= 2:
        if game_board[index_row - 1][index_col + 1] == player:
            matches += 1
            index_row -= 1
            index_col += 1
        else:
            break

        if matches == 2:
            return player_num


    # Towards bottom left
    index_row = last_move[0]
    index_col = last_move[1]
    while (index_row + 1) <= 2 and (index_col - 1) >= 0:
        if game_board[index_row + 1][index_col - 1] == player:
            matches += 1
            index_row += 1
            index_col -= 1
        else:
            break

        if matches == 2:
            return player_num


    # If there's no winner yet and the grid isn't filled yet continue the game.
    if turn < 8:
        return 0

    # If no winner is detected by this point, it's a tie game.
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

    win_detected = check_win(game_board, player, (move_row, move_col), turn) # change tuple to be last move

    if win_detected == 1:
        print('Tie Game!')
    elif win_detected == 2:
        print ('X wins!')
    elif win_detected == 3:
        print('O wins!')

    turn += 1
