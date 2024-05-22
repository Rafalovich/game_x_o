from humen_player import HumanPlayer
from AI_player import AIPlayer
board= [
    ['.', '.', '.'],
    ['.', '.', '.'],
    ['.', '.', '.']
]
# arrey

players = [HumanPlayer('x'),AIPlayer('o')]
current_player = 0


def game_over(board):
    if get_winner(board) is not None:
        return True

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == '.':
                return False

    return True


def is_all_the_same(board ,i1, i2, i3, val):
    """the funksion accept """
    if (board[i1[0]][i1[1]] == board[i2[0]][i2[1]] and
        board[i1[0]][i1[1]] == board[i3[0]][i3[1]] and
        board[i1[0]][i1[1]] == val
    ):
        return True
    else:
        return False


def get_winner(board):
    for player in ['x', 'o']:
        # rows
        if is_all_the_same(board,(0, 0), (0, 1), (0, 2), player): return player
        if is_all_the_same(board, (1, 0), (1, 1), (1, 2), player): return player
        if is_all_the_same(board, (2, 0), (2, 1), (2, 2), player): return player
        # columns
        if is_all_the_same(board, (0, 0), (1, 0), (2, 0), player): return player
        if is_all_the_same(board, (0, 1), (1, 1), (2, 1), player): return player
        if is_all_the_same(board, (0, 2), (1, 2), (2, 2), player): return player
        # diagonals
        if is_all_the_same(board, (0, 0), (1, 1), (2, 2), player): return player
        if is_all_the_same(board, (0, 2), (1, 1), (2, 0), player): return player


def is_valid(board, next_move):
    row, column = next_move
    #try:
    return board[row][column] == '.'


def print_board(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            print("{:^3}".format(board[i][j]), end = '')
        print("")


def play(board, next_move):
    global current_player
    row, column = next_move
    player_value = players[current_player].value
    board[row][column] = player_value
    current_player = (current_player +1) % len(players)
    print_board(board)


if __name__ == '__main__':
    while not game_over(board):
        next_move = players[current_player].get_move()
        if is_valid(board, next_move):
            play(board, next_move)

    winner = get_winner(board)
    if winner == 'x':
        print("Yay! x won")
    elif winner == 'o':
        print("Yay! o won")
    else:
        print("game over...")


