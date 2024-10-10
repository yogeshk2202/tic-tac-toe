def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def get_player_move(board, player):
    while True:
        try:
            move = input(f"Player {player}, enter your move as row,col (0, 1, or 2): ")
            row, col = map(int, move.split(","))
            if board[row][col] == " ":
                return row, col
            else:
                print("This spot is already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Enter row and column numbers as 0, 1, or 2.")

def display_winner(player):
    print(f"Player {player} wins!")

def display_tie():
    print("It's a tie!")
