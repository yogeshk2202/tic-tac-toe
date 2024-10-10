from ui import display_board, get_player_move, display_winner, display_tie
from utils import initialize_board, check_winner, is_board_full

def play_game():
    board = initialize_board()
    current_player = "X"
    
    while True:
        display_board(board)
        row, col = get_player_move(board, current_player)
        board[row][col] = current_player
        
        if check_winner(board, current_player):
            display_board(board)
            display_winner(current_player)
            break
        
        if is_board_full(board):
            display_board(board)
            display_tie()
            break
        
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play_game()
