import random
import sys

gamematrix=[i for i in range(0,9)]
human, cpu = '',''

# Gonies Kentro kai alla kelia
movements=((1,7,3,9),(5,),(2,4,6,8))
# Pote iparxei niki
winners=((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
# Pinakas
tab=range(1,10)

def print_gamematrix():
    x=1
    for i in gamematrix:
        end = ' | '
        if x%3 == 0:
            end = ' \n'
            if i != 1: end+='---------\n';
        char=' '
        if i in ('X','O'): char=i;
        x+=1
        print(char,end=end)
        
def select_char():
    chars=('X','O')
    if random.randint(0,1) == 0:
        return chars[::-1]
    return chars

def can_movement(brd, human, movement):
    if movement in tab and brd[movement-1] == movement-1:
        return True
    return False

def can_win(brd, human, movement):
    places=[]
    x=0
    for i in brd:
        if i == human: places.append(x);
        x+=1
    win=True
    for tup in winners:
        win=True
        for ix in tup:
            if brd[ix] != human:
                win=False
                break
        if win == True:
            break
    return win

def make_movement(brd, human, movement, undo=False):
    if can_movement(brd, human, movement):
        brd[movement-1] = human
        win=can_win(brd, human, movement)
        if undo:
            brd[movement-1] = movement-1
        return (True, win)
    return (False, False)

# Kinisi ipologisti
def cpu_movement():
    movement=-1
    for i in range(1,10):
        if make_movement(gamematrix, cpu, i, True)[1]:
            movement=i
            break
    if movement == -1:
        # Otherwise, try to take one of desired places.
        for tup in movements:
            for mv in tup:
                if movement == -1 and can_movement(gamematrix, cpu, mv):
                    movement=mv
                    break
    return make_movement(gamematrix, cpu, movement)

def space_exist():
    return gamematrix.count('X') + gamematrix.count('O') != 9

human, cpu = select_char()
print('Human is [%s] and CPU is [%s]' % (human, cpu))
result='%%% Deuce ! %%%'
while space_exist():
    print_gamematrix()
    print(' Its your turn ! [1-9] : ', end='')
    movement = int(input())
    movementd, won = make_movement(gamematrix, human, movement)
    if not movementd:
        print(' >> Invalid number ! Try again !')
        continue
    #
    if won:
        result='CONGRATS! YOU ARE THE CHAMPION!'
        break
    elif cpu_movement()[1]:
        result='Better luck next time'
        break;

print_gamematrix()
print(result)
