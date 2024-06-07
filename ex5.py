import random

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



# 最初に見つけた場所に置く
def think_seq(board) :
    pos = []
    for i in range(3):
        for j in range(3) :
            if board[i][j] == 0 : return (j, i)
        
    return (0,0)

# ランダムに置く場所を決める
def think_random(board) :
    pos = []
    for i in range(3):
        for j in range(3) :
            if board[i][j] == 0 : pos.append((j, i))
        
    sel = random.randint(0, len(pos)-1)
    return pos[sel]


# 負けない様ににする
def think_stop2(board, turn) :
    pos = []
    for i in range(3):
        for j in range(3) :
            if board[i][j] != 0 : continue
            board[i][j] = -turn
            if  check_win(board) == -turn :
                board[i][j] = 0
                return (j, i)

            board[i][j] = 0
            pos.append((j, i))
        
    sel = random.randint(0, len(pos)-1)
    return pos[sel]



# 負けない様ににする
def think_stop2(board, turn) :
    pos = []
    for i in range(3):
        for j in range(3) :
            if board[i][j] != 0 : continue
            board[i][j] = -turn
            if  check_win(board) == -turn :
                board[i][j] = 0
                return (j, i)

            board[i][j] = 0
            pos.append((j, i))
        
    sel = random.randint(0, len(pos)-1)
    return pos[sel]

# 深さ優先探索で、最終的な勝者を返す
def think(board, turn) :
    # 9マス全てが埋まっているかどうか確認
    cnt = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0 : cnt += 1
    if cnt == 0 : 
        return -1, -1, 0  # 全て埋まっていればDRAW

    x, y = 0,0
    win = False
    res = -turn
    for i in range(3) :
        for j in range(3) :
            if board[i][j] != 0 : continue # 既に置かれている場合はスキップ

            board[i][j] = turn
            winner = check_win(board)
            if winner == turn : 
                board[i][j] = 0
                return j, i, turn # 置いて勝てば勝者はturnの人
            
            # 次の手を考える
            _, _, r = think(board, -turn)
            board[i][j] = 0

            if r == turn: # 自分が勝つ場合は、その手を覚える
                win = True
                x, y = j, i
                res = turn
            if win == False: # 自分の価値が決定してない場合
                if r == 0 : # 引き分けの場合は、手を覚える
                    x, y = j, i
                    res = 0
                if r == -turn and res == -turn: # 現在まだ引き分け以上の手が見つかっていなければ、場所を記録
                    x, y = j, i         

    return x, y, res



board = [[0,0,0] for _ in range(3)]

# x, y, ret = think(board, -1)
# print(x, y, ret)

# exit(0)

for i in range(9) :
    print_board(board)

    stat = check_win(board)
    if stat == -1 :
        print("-"*20)
        print("Winner is player1")
        print("-"*20)
        exit(0)
    if stat == 1 :
        print("-"*20)
        print("Winner is player2")
        print("-"*20)
        exit(0)


    if i%2 == 0:
        print("Enter position(ex. 1a):", end="")
        while(1) :
            x, y = get_input()
            if board[y][x] != 0 :
                print("already occupied. try again.")
            else:
                break
        # x, y, _ = think(board, 1)
    else:
        # x, y, _ = think(board, 1)
        # x, y = think_random(board)
        # x, y = think_seq(board)
        x, y = think_stop2(board, 1)

    if i%2 == 0 :
        board[y][x] = -1
    else :
        board[y][x] = 1
    
print_board(board)
print("-"*20)
print("Draw")
print("-"*20)

