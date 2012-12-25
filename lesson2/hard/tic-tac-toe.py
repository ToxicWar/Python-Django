#!/bin/python
# coding: utf-8

# статусы
win = "win"
tie = "tie"
lose = "lose"
inProgress = "inProgress"

# получение следующего игрока
getNextPlayer = {"X": "O", "O": "X"}.get

getNextPlayer = {"X": "O", "O": "X"}.get
cells = [(r, c) for r in range(3) for c in range(3)]
lines = [
    # вертикальные линии
    [(0,0),(0,1),(0,2)],
    [(1,0),(1,1),(1,2)],
    [(2,0),(2,1),(2,2)],
    # горизонтальные линии
    [(0,0),(1,0),(2,0)],
    [(0,1),(1,1),(2,1)],
    [(0,2),(1,2),(2,2)],
    # диагональ и обратная диагональ
    [(0,0),(1,1),(2,2)],
    [(2,0),(1,1),(0,2)],
]

# возвращает все возможные ходы
def getMoves(player, board):
    return [(r, c) for (r, c) in cells if board[r][c] == '_']

# проверка на выигрыш
def isWinning(player, board):
    return any(all(board[r][c] == player for (r, c) in line) for line in lines)

# моделируем следующий ход
def makeMove(player, board, move):
    moved = board[:]
    moved[move[0]] = moved[move[0]][:]
    moved[move[0]][move[1]] = player
    return moved

# проверка на первый ход
def is_empty(board):
    for row in board:
        if any(('X' in row, 'O' in row)):
            return False
    return True

# получение статуса
def getStatus(player, board):
    if isWinning(player, board): return win
    elif isWinning(getNextPlayer(player), board): return lose
    elif any("_" in row for row in board): return inProgress
    else: return tie

# выбераем лучший ход
def getBestMove(player, board):
    if is_empty(board):
        return (1, 1)
    moves = getMoves(player, board)
    if len(moves) in [1, 9]: return moves[0]

    boards = {move: makeMove(player, board, move) for move in moves}
    for move in moves:
        if isWinning(player, boards[move]): 
            return move

    outcomes = {move: getOutcome(player, boards[move]) for move in moves}
    best = max(outcomes.values())
    for move in moves:
        if outcomes[move] == best:
            return move

# получение результатов
def getOutcome(player, board):
    opponent = getNextPlayer(player)
    moves = getMoves(opponent, board)

    status = getStatus(player, board)
    if not moves or status == win: return status
    
    return min(getOpponentOutcome(opponent, makeMove(opponent, board, move)) for move in moves)

# получение результатов противника
def getOpponentOutcome(opponent, board):
    player = getNextPlayer(opponent)
    moves = getMoves(player, board)

    status = getStatus(player, board)
    if not moves or status == lose: return status

    return max(getOutcome(player, makeMove(player, board, move)) for move in moves)

def nextMove(player, board):
    move = getBestMove(player, board)
    print move[0], move[1]
    
player = raw_input()

board = []
for i in xrange(0, 3):
    board.append(list(raw_input()))

nextMove(player, board)