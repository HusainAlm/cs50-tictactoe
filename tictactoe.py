import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():

    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):

    x_counter = 0
    O_counter = 0
 
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == X:
                x_counter+=1
            elif board[i][j] == O:
                O_counter+=1

    if  x_counter > O_counter:
        return O
    else:
        return X

def actions(board):

    allPossibleActions = set()
  
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == EMPTY:
                allPossibleActions.add((i,j))
    return allPossibleActions


def result(board, action):

    if action not in actions(board):
        raise Exception("Not valid action")
    
    i, j = action
    board_copy = copy.deepcopy(board)
    board_copy[i][j] = player(board)
    return board_copy

def checkRow(board, player):
    for i in range(len(board)):
        if board[i][0] == player and board[i][1] == player and board[i][2]  == player:
            return True
    return False

def checkCol(board, player):
    for j in range (len(board)):
        if board[0][j] == player and board[1][j]== player and board[2][j] == player:
            return True
    return False

def checkFirstDig(board, player):
    count = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if i == j and board[i][j] == player:
                count+=1
    if count == 3:
        return True
    else:
        return False
    
def checkSecondDig(board, player):
    count = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if(len(board) - i - 1) == j and board[i][j] == player:
                count+=1
    if count == 3:
        return True
    else:
        return False

def winner(board):
    if checkRow(board, X) or checkCol(board, X) or checkFirstDig(board, X) or checkSecondDig(board, X):
        return X
    elif checkRow(board, O) or checkCol(board, O) or checkFirstDig(board, O) or checkSecondDig(board, O):
        return O
    else:
        return None

def terminal(board):

    if winner(board)==X:
        return True
    if winner(board)==O:
        return True
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]==EMPTY:
                return False
    return True


def utility(board):
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def max_value(board):
    v = -math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    v = math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    elif player(board) == X:
        plays = []
        for action in actions(board):
            plays.append([min_value(result(board, action)), action])
        return sorted(plays, key=lambda x: x[0], reverse=True)[0][1]
    
    elif player(board) == O:   
        plays = []
        for action in actions(board):
            plays.append([max_value(result(board, action)), action])
        return sorted(plays, key=lambda x: x[0])[0][1]
