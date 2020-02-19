import os
import time

def showboard(board):
    os.system("cls")
    print('\n USE NUMBER PAD AS YOUR BOARD \n')
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('==========')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('==========')
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('\n')

def tie():
    if ' ' not  in board[1:]:
        print('ITS A TIEEE \n')
        return  True
    else:
        return  False

class players:

    def __init__(self,marker = '', turn = 0):
        self.marker = marker
        self.turn = turn

    def play(self):
        print(f"** Player {self.turn}'s turn **")
        while True:
            ch = int(input('Make your move: '))
            if board[ch] == ' ':
                board[ch] = self.marker
                break
            else:
                print('Already filled.')
        showboard(board)

    def game_won(self):
        if board[7] == board[8] == board[9] != ' ':
            print(f'Player {self.turn} wins in row 1')
            return True
        elif board[4] == board[5] == board[6] != ' ':
            print(f'Player {self.turn} wins in row 2')
            return True
        elif board[1] == board[2] == board[3] != ' ':
            print(f'Player {self.turn} wins in row 3')
            return True
        elif board[1] == board[4] == board[7] != ' ':
            print(f'Player {self.turn} wins in column 1')
            return True
        elif board[2] == board[5] == board[8] != ' ':
            print(f'Player {self.turn} wins in column 2')
            return True
        elif board[3] == board[6] == board[9] != ' ':
            print(f'Player {self.turn} wins in column 3')
            return True
        elif board[7] == board[5] == board[3] != ' ':
            print(f'Player {self.turn} wins in diagonal')
            return True
        elif board[1] == board[5] == board[9] != ' ':
            print(f'Player {self.turn} wins in diagonal')
            return True
        else:
            return False

again='y'
while again=='y':

    board = [' ']*10
    p1 = players()
    p2 = players()

    p1.marker, p1.turn = input('\nEnter marker (X or O) for player 1: '), 1
    p2.marker, p2.turn = 'o' if p1.marker == 'x' else 'x', 2

    print(f'Player 1 is: {p1.marker} \nPlayer 2 is: {p2.marker}')
    time.sleep(1)
    showboard(board)

    while not tie():
        p1.play()
        if p1.game_won():
            break
        if tie():
            break
        p2.play()
        if p2.game_won():
            break

    again = input('Want to play again? (y/n): ')