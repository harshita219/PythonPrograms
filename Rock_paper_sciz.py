"""
Rock beats Scissors (by blunting them)
Scissors beat Paper (by cutting it)
Paper beats Rock (by covering it)

"""
ctr, p1, p2 = 0, 0, 0

def gamecheck(x,y):

    mylist = [x,y]
    global p1,p2

    if 'r' in mylist and 'p' in mylist:
        if x == 'p':
            p1 += 1
        else:
            p2 += 1
    elif 's' in mylist and 'p' in mylist:
        if x == 's':
            p1 += 1
        else: p2 += 1
    elif 'r' in mylist and 's' in mylist:
        if x == 'r':
            p1 += 1
        else: p2 += 1

print('\nEnter r/p/s for rock/paper/scissors')
while ctr < 5:
    print('      ~~~')
    ch1 = input('Player 1 input: ')
    ch2 = input('Player 2 input: ')
    gamecheck(ch1,ch2)
    ctr += 1
print('      ~~~')
print(f'Scores are: \nPlayer 1 = {p1} \nPlayer 2 = {p2}')
if p1 == p2:
    print('ITS A TIE')
elif p1>p2:
    print('PLAYER 1 wins')
else:
    print('PLAYER 2 wins')