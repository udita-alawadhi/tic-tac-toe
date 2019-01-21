import random

board={1:' ', 2:' ', 3:' ', 4:' ', 5:' ', 6:' ', 7:' ', 8:' ', 9:' '}

def printBoard(board):
    print(board[1]+'|'+board[2]+'|'+board[3])
    print('-----')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-----')
    print(board[7]+'|'+board[8]+'|'+board[9])

def playAgain():
    print('Do you want to play again? (yes or no)')
    if input().lower()=='yes':
        return True
    else:
        return False

def whoGoesFirst():
    r = random.randint(0,1)
    if r==0:
        return 'Computer'
    else:
        return 'Player'

def chooseVar():
    var=''
    while not (var=='X' or var=='O'):
        print('Do you want X or O?')
        var=input().upper()
    return var

def choosePlayer():
    var=chooseVar()
    print(var+' chosen')
    if var=='X':
        return ['X','O']
    else:
        return ['O','X']
    
def choosePlayerMove():
    position = True
    while position:
        #check if input is an integer only
        empty = []
        for i in range(1,10):
            if freespace(i):
                empty.append(i)
        if len(empty)==0:
                return None
        else:
            value=input()
            if value.isdecimal():
                pos=int(value)
                if pos not in (1,2,3,4,5,6,7,8,9):
                    print('Please enter appropriate position.')
                else:
                    if freespace(pos):
                        return pos
                    else:
                        print('This position is already taken.')
            else:
                print('Please enter an integer value')
    
def freespace(p):
    if board[p]==' ':
        return True
    else:
        return False

    
def chooseComputerMove():
    empty = []
    for i in range(1,10):
        if freespace(i):
            empty.append(i)
    if len(empty)!=0:
        return random.choice(empty)
    else:
        return None

def Winner(board, turn):
    return ((board[1]==board[2]==board[3]==turn) or (board[4]==board[5]==board[6]==turn) or (board[7]==board[8]==board[9]==turn) or
       (board[1]==board[4]==board[7]==turn) or (board[2]==board[5]==board[8]==turn) or (board[3]==board[6]==board[9]==turn) or
       (board[1]==board[5]==board[9]==turn) or (board[3]==board[5]==board[7]==turn))


play=True


while play:
    print('-------WELCOME TO THE TIC-TAC-TOE GAME-------')
    #--start here
    player, computer = choosePlayer()
    turn=whoGoesFirst()
    print(turn+ ' goes first')

    #--Player's turn
    gameOn=True
    while gameOn:
        if turn=='Player':
            printBoard(board)
            print('Enter your move')
            mov=choosePlayerMove()
            if mov == None:
                print('Game tied')
                gameOn=False
            else:
                board[mov]=player

            if Winner(board, player):
                printBoard(board)
                print('Congratulations!! You won')
                gameOn =False
            else:
                turn='Computer'
    #---

    #--Computer's turn
        if turn=='Computer':
            move=chooseComputerMove()
            if move==None:
                print('Game tied.')
                gameOn=False
            else:
                board[move]=computer

            if Winner(board, computer):
                printBoard(board)
                print('You lose. The computer won')
                gameOn =False
            else:
                turn='Player'
    #---
                
    play=playAgain()
    board={1:' ', 2:' ', 3:' ', 4:' ', 5:' ', 6:' ', 7:' ', 8:' ', 9:' '}

''' --------------------------------------------------THIS CODE WILL RUN FOR 2 PLAYER GAME-----------------------------------------------
print('What goes first: X or O?')
turn=input()
for i in range(0,9):
    print('Position for '+turn+'?')
    while(True):
        pos=int(input())
        if board[pos]==' ':
            board[pos]=turn
            break
        else:
            print('this position is already taken')
    printboard(board)
    if((board[1]==board[2]==board[3]!=' ') or (board[4]==board[5]==board[6]!=' ') or (board[7]==board[8]==board[9]!=' ')+\
       (board[1]==board[4]==board[7]!=' ') or (board[2]==board[5]==board[8]!=' ') or (board[3]==board[6]==board[9]!=' ')+\
       (board[1]==board[5]==board[9]!=' ') or (board[3]==board[5]==board[7]!=' ')):
        print('Player '+turn+' won')
        break;
    if turn=='X':
        turn='O'
    else:
        turn='X'
'''
