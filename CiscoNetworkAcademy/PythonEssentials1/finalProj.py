import random
def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    boardStr = "+-------+-------+-------+\n"
    boardStr += "|       |       |       |\n"
    boardStr += "|   {}   |   {}   |   {}   |\n".format(board[0][0],board[0][1],board[0][2])
    boardStr += "|       |       |       |\n"
    boardStr += "+-------+-------+-------+\n"
    boardStr += "|       |       |       |\n"
    boardStr += "|   {}   |   {}   |   {}   |\n".format(board[1][0],board[1][1],board[1][2])
    boardStr += "|       |       |       |\n"
    boardStr += "+-------+-------+-------+\n"
    boardStr += "|       |       |       |\n"
    boardStr += "|   {}   |   {}   |   {}   |\n".format(board[2][0],board[2][1],board[2][2])
    boardStr += "|       |       |       |\n"
    boardStr += "+-------+-------+-------+\n"
    print(boardStr)

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    movesDict = {1:(0,0),2:(0,1),3:(0,2),4:(1,0),5:(1,1),6:(1,2),7:(2,0),8:(2,1),9:(2,2)}
    openMoves = make_list_of_free_fields(board)
    validBool = False
    while not validBool:
        user_input =''
        user_input = input("Enter your move:\n")
        if(user_input.isnumeric() and int(user_input)<10 and int(user_input)>0):
            move = movesDict[int(user_input)]
            if move in openMoves:
                validbool = True
                board[move[0]][move[1]] = 'O'
                return
            else:
                print("Error: Space already taken")
        else:
            print("Error: Invalid Input")

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    freeList = []
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j] not in ["X","O"]:
                freeList.append((i,j))
    return freeList

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    cols = [0,0,0]
    rows = [0,0,0]
    diagr = 0
    diagl = 0
    for i in range(0,3):
        for j in range(0,3):
            score = 0
            if board[i][j] == sign:
                score = 1
            cols[i]+=score
            rows[j]+=score
            if i == j:
                diagl += score
            if 3-(i+1) == j:
                diagr += score
    if (3 in cols) or (3 in rows) or (diagr == 3) or (diagl == 3):
        return True
    else:
        return False


def draw_move(board):
    # The function draws the computer's move and updates the board.
    openMoves = make_list_of_free_fields(board)
    move = random.randint(0,len(openMoves)-1)
    board[openMoves[move][0]][openMoves[move][1]] = 'X'
    
    
board =  []
for i in range(0,3):
    board.append([0]*3)
board[1][1] = 'X'
display_board(board)
i = 0
while i < 8:
    
    if i%2 == 0:
        #player turn
        enter_move(board)
        display_board(board)
        if(victory_for(board,'O')):
            print("You won!")
            break
        
    else:
        #CPU turn
        draw_move(board)
        display_board(board)
        if(victory_for(board,'X')):
            print ("CPU won!")
            break
    i+=1
if i == 8:
	print("It's a draw!")
    
