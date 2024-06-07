# 入力を受け付ける

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
    x, y = get_input()
    if i%2 == 0 :
        board[y][x] = -1
    else :
        board[y][x] = 1

