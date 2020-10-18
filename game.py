def main():
    print("----------------------")
    print("Welcome to TIC TAC TOE")
    print("----------------------")
    board = [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]
    active_player_index = 0
    players = ["Darren", "Computer"]
    symbols = ["X", "O"]
    player = players[active_player_index]

    while not find_winner(board):
        player = players[active_player_index]
        symbol = symbols[active_player_index]
        announce_turn(player)
        show_board(board)
        if not choose_location(board, symbol):
            print("That isn't an option, try again.")
            continue

        # TOGGLE ACTIVE PLAYER
        active_player_index = (active_player_index + 1) % len(players)
    print()
    print(f"GAME OVER! {player} has won with the board: ")
    print()
    show_board(board)


def choose_location(board, symbol):
    row = int(input("Choose which row: "))
    column = int(input("Choose which column: "))
    row -= 1
    column -= 1
    if row < 0 or row > len(board):
        return False
    if column < 0 or column > (len(board[0])):
        return False

    cell = board[row][column]
    if cell is not None:
        return False

    board[row][column] = symbol
    return True


def show_board(board):
    for row in board:
        print("| ", end="")
        for cell in row:
            symbol = cell if cell is not None else "-"
            print(symbol, end=" | ")
        print()


def announce_turn(player):
    print()
    print(f"It's {player}'s turn. Here's the board:")
    print()


def find_winner(board):
    sequences = get_winning_sequences(board)

    for cells in sequences:
        symbol1 = cells[0]
        if symbol1 and all(symbol1 == cell for cell in cells):
            return True

    return False


def get_winning_sequences(board):
    sequences = []

    # Win by Rows
    rows = board
    sequences.extend(rows)

    # Win by Columns
    for col_index in range(0, 3):
        col = [
            board[0][col_index],
            board[1][col_index],
            board[2][col_index],
        ]
        sequences.append(col)

    # Win by Diagonals
    diagonals = [
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    ]
    sequences.extend(diagonals)

    return sequences


if __name__ == '__main__':
    main()
