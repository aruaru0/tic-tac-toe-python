# ボードを表示する
def print_board(board):
    print("-"*20)
    print("  a b c")
    for i, row in enumerate(board):
        print(i+1, end=" ")
        for col in row:
            if col == 0:
                print('.', end=' ')
            if col == 1:
                print('X', end=' ')
            if col == -1:
                print('O', end=' ')
        print()

board = [[0,0,0] for _ in range(3)]
print_board(board)

