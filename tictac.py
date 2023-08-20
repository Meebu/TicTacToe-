board = [
    ["", "", ""], ["", "", ""], ["", "", ""], ]
IndexError
def horizontal_winner(board):
    for row in board:
        if all(cell == "X" for cell in row):
            return "Player X wins!"
        if all(cell == "O" for cell in row):
            return "Player O wins!"

def vertical_winner(board):
    for col in range(3):
        if all(board[row][col] == "X" for row in range(3)):
            return "Vertical X"
        if all(board[row][col] == "O" for row in range(3)):
            return "Vertical O"

def primary_diagonal(board):
    list = []
    for index, row in enumerate(board):
        list.append(board[index][index])
    if all(item == "X" for item in list):
        return "Diagonal X Won"
    if all(item == "O" for item in list):
        return "Diagonal O Won"

def secondary_diagonal(board):
    temp = []
    for row in board:
        temp.append(row[::-1])

    if all(item == "X" for item in temp):
        return "Diagonal X Won"
    if all(item == "O" for item in temp):
        return "Diagonal O Won"

def display(board):
    temp = []
    for row in board:
        row_strings = [str(item) for item in row]
        strings = " | "
        result = strings.join(row_strings)
        temp.append(result)

    for item in temp:
        print(item)
        print("----------")

def check_winner(board):
    val1 = horizontal_winner(board)
    val2 = vertical_winner(board)
    val3 = primary_diagonal(board)
    val4 = secondary_diagonal(board)
    my_list = []
    my_list.extend([val1, val2, val3, val4])
    for item in my_list:
        if item is not None:
            return item
    str1 = all_cells_filled(board)
    if str1 == True:
        return "Draw Game"

def all_cells_filled(board):
    for row in board:
        for cell in row:
            if cell == "":
                return False  # Found an empty cell
    return True  # All cells are filled


while True:
    user = input("Choose your sign X or O: ").upper()
    if user in ["X", "O"]:
        break
    else:
        print("Invalid choice. Please choose 'X' or 'O'.")
while True:
    try:
        rows = int(input("Enter row : "))  # value error exception handle
        column = int(input("Enter Col : "))
        if board[rows][column] == "":
            board[rows][column] = str(user)
        else:
            print("Cell Acquired... Choose Again!!!")
            continue

        res = check_winner(board)
        display(board)
        if res is not None:
            print(res)
            break
        if user == "X":
            user = "O"
        else:
            user = "X"
    except (ValueError, IndexError):
        print("Enter Again !!!")
