# 드래곤 커브
# 구현
# 규칙성 찾는 아이디어가 정말 중요 (큐)

import sys
from collections import deque

sys.stdin = open("testcase/15685.txt", "r")

def print_mat(board):
    for b in board:
        print(b)
    print("")

def main():
    N = int(sys.stdin.readline())
    info = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(N)]

    size = 101
    board = [[0]*size for _ in range(size)]

    # 0 1 2 3 동 북 서 남
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    def turn(dir): # 피봇을 기준으로 (x,y) 시계방향으로 회전시키기
        if dir == 0:
            return 1
        elif dir == 1:
            return 2
        elif dir == 2:
            return 3
        elif dir == 3:
            return 0
        
    global max_x, max_y
    max_x = 0
    max_y = 0
    def draw_dragon(x, y, d, g): # 시작점, 방향, 세대
        global max_x, max_y
        dq = [d]
        for i in range(g):
            dq_ = dq[:]
            for j in range(len(dq_)-1, -1, -1):
                dq.append(turn(dq_[j]))
        
        board[y][x] = 1
        sx = x
        sy = y
        max_x = max(max_x, sx)
        max_y = max(max_y, sy)
        for dir in dq:
            ex = sx + dx[dir]
            ey = sy + dy[dir]
            board[ey][ex] = 1
            sx = ex
            sy = ey
            max_x = max(max_x, ex)
            max_y = max(max_y, ey)
    #draw_dragon(3, 3, 0, 3)
    
    for x, y, d, g in info:
        draw_dragon(x, y, d, g)
    # print_mat(board)

    # 정사각형 개수 구하기
    cnt = 0
    for i in range(max_y):
        for j in range(max_x):
            if board[i][j] == 1 and board[i+1][j] == 1 and board[i][j+1] == 1 and board[i+1][j+1] == 1:
                cnt += 1

    print(cnt)

for _ in range(4):
    main()
            
