# tic_tac_toe.py

def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print("\n")

def check_winner(board, player):
    # Rows, columns, diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]):
            return True
        if all([board[j][i] == player for j in range(3)]):
            return True

    if all([board[i][i] == player for i in range(3)]):
        return True
    if all([board[i][2-i] == player for i in range(3)]):
        return True

    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    current = "X"

    while True:
        print_board(board)
        print(f"Player {current}'s turn")

        try:
            row = int(input("Enter row (0,1,2): "))
            col = int(input("Enter col (0,1,2): "))
        except ValueError:
            print("❌ Invalid input. Please enter numbers 0,1,2.")
            continue

        if row not in [0,1,2] or col not in [0,1,2]:
            print("❌ Out of range. Try again.")
            continue
        if board[row][col] != " ":
            print("❌ Cell already taken. Try again.")
            continue

        board[row][col] = current

        if check_winner(board, current):
            print_board(board)
            print(f"🎉 Player {current} wins!")
            break
        if is_full(board):
            print_board(board)
            print("🤝 It's a draw!")
            break

        current = "O" if current == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
