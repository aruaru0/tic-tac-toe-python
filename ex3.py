# 置けない場合は入力を繰り返す
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


def get_input() :
    s = input()
    print(s)
    if '0' <= s[0] and s[0] <= '9' :
        y = int(s[0])-1
        x = ord(s[1]) - ord('a')
    else :
        y = int(s[1])-1
        x = ord(s[0]) - ord('a')

    return x, y

board = [[0,0,0] for _ in range(3)]

for i in range(9) :
    print_board(board)
    print("Enter position(ex. 1a):", end="")
    while(1) :
        x, y = get_input()
        if board[y][x] != 0 :
            print("already occupied. try again.")
        else:
            break
    if i%2 == 0 :
        board[y][x] = -1
    else :
        board[y][x] = 1

