# 사다리 조작
# 구현 + 백트래킹 dfs (브루트포스)
# python3 로는 시간초과 pypy로 통관
# 시간 초과 안나도록 나중에 다시 시도해보기

import sys

sys.stdin = open("15684.txt", "r")

def print_mat(board):
    for b in board:
        print(b)
    print("")

answer = 4

def main():
    N, M, H = map(int, sys.stdin.readline().split(" "))
    line_info = [tuple(map(int, sys.stdin.readline().split(" "))) for _ in range(M)]
    board = [[0]* (N-1) for _ in range(H)]
    for a, b in line_info:
        board[a-1][b-1] = 1  # bridge 표시
        if 0<=b<N-1: # bridge 못 세우는 곳 표시
            board[a-1][b] = -1
        if 0<=b-2<N-1:
            board[a-1][b-2] = -1
    
    cand = []
    for i in range(H):
        for j in range(N-1):
            if board[i][j] == 0:
                cand.append((i,j))

    def check():
        for i in range(N):
            line_y = 0
            line_x = i
            for line_y in range(H):
                # print(line_x, line_y)
                if line_x-1 >= 0 and board[line_y][line_x-1] == 1: # 왼쪽 방향 확인
                    line_x -= 1
                elif line_x < N-1 and board[line_y][line_x] == 1: # 오른쪽 방향 확인
                    line_x += 1
            if line_x != i:
                return False
        return True

    def dfs(step, idx):
        # print("step:", step, "cand:", cand)
        global answer
        if step >= answer or step > 3:
            return
        if check():
            answer = min(answer, step)
            return
        for i in range(idx, len(cand)):
            board[cand[i][0]][cand[i][1]] = 1
            dfs(step+1, i+1)
            board[cand[i][0]][cand[i][1]] = 0  


    # print(line_info)
    # print_mat(board)
    dfs(0, 0)

    if answer == 4:
        print(-1)
    else:
        print(answer)

for i in range(7):
    answer = 4
    main()
