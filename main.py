def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):  # Horizontal check
            return f"Player {player} wins!"

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):  # Vertical check
            return f"Player {player} wins!"

    if all(board[i][i] == player for i in range(3)):  # Primary diagonal check
        return f"Player {player} wins!"

    if all(board[i][2 - i] == player for i in range(3)):  # Secondary diagonal check
        return f"Player {player} wins!"

    return None

def display(board):
    for row in board:
        row_str = " | ".join(cell if cell else " " for cell in row)
        print(row_str)
        print("---------")

def all_cells_filled(board):
    return all(cell for row in board for cell in row)

def play_tic_tac_toe():
    board = [["" for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    while not all_cells_filled(board):
        current_player = players[turn % 2]
        display(board)

        try:
            row = int(input(f"Player {current_player}, enter row (0-2): "))
            col = int(input(f"Player {current_player}, enter column (0-2): "))

            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == "":
                board[row][col] = current_player
                winner = check_winner(board, current_player)
                if winner:
                    display(board)
                    print(winner)
                    return
                turn += 1
            else:
                print("Invalid move. Try again.")

        except (ValueError, IndexError):
            print("Invalid input. Try again.")

    display(board)
    print("It's a draw!")

if __name__ == "__main__":
    play_tic_tac_toe()
