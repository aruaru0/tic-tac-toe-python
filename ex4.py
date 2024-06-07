# 人vs人完成
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
    if '0' <= s[0] and s[0] <= '9' :
        y = int(s[0])-1
        x = ord(s[1]) - ord('a')
    else :
        y = int(s[1])-1
        x = ord(s[0]) - ord('a')

    return x, y

def check_win(board) :
    for i in range(3) :
        if board[i][0] == board[i][1] == board[i][2] :
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] :
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] :
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] :
        return board[0][2]

    return 0

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
    
    stat = check_win(board)
    if stat == -1 :
        print("-"*20)
        print("Winner is player1")
        print("-"*20)
        break
    if stat == 1 :
        print("-"*20)
        print("Winner is player2")
        print("-"*20)
        break

