# 미세먼지 안녕!
# 구현
# 공기청정기가 1열에 위치한 경우만 고려하면 됨 ㅠㅠ

import sys
from copy import deepcopy 

sys.stdin = open("testcase/17144.txt", "r")

def print_mat(board):
    for b in board:
        print(b)
    print(" ")

def main():
    R, C, T = map(int, sys.stdin.readline().split(" "))
    board = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(R)]
    # print_mat(board)

    dx = [0, 1, 0, -1] # 북 동 남 서
    dy = [-1, 0, 1, 0]
    purif = [] # 공기 청정기 좌표
    for i in range(R):
        if board[i][0] == -1:
            purif.append(i)

    def spread():
        # print("spread initial")
        # print_mat(board)
        board_refer = deepcopy(board)
        for i in range(R):
            for j in range(C):
                if board[i][j] <= 0:
                    continue
                spread = board_refer[i][j] // 5 # 칸 x, y에서 주변에 spread될 양
                spread_cnt = 0
                for k in range(4):
                    fx = j + dx[k]
                    fy = i + dy[k]
                    if fx<0 or fy<0 or fx>=C or fy>=R or board_refer[fy][fx]==-1: # 칸 벗어나거나 공기청정기인 경우, 아무것도 하지 않음
                        continue
                    board[fy][fx] += spread # 인전칸에 전파
                    spread_cnt += 1
                board[i][j] -= spread * spread_cnt # 발원지 빼주기
        return

    def circulate():
        # print("circulte initial")
        # print_mat(board)
        board_refer = deepcopy(board)
        # 위쪽 공기청정기의 바람은 반시계방향
        purif_y = purif[0]
        purif_x = 0
        for j in range(C-1): # 위쪽 부분
            board[0][j] = board_refer[0][j+1]
        for i in range(purif_y): # 오른쪽 세로 부분
            board[i][C-1] = board_refer[i+1][C-1]
        for i in range(1, purif_y): # 왼쪽 세로 부분
            board[i][0] = board_refer[i-1][0]
        for j in range(purif_x+2, C): # 공기청정기 오른쪽 부분
            board[purif_y][j] = board_refer[purif_y][j-1]
        board[purif_y][purif_x+1] = 0

        # print_mat(board)
        # 아래쪽 공기청정기의 바람은 시계방향
        purif_y = purif[1]
        for j in range(C-1): # 아래쪽 부분
            board[R-1][j] = board_refer[R-1][j+1]
        for i in range(purif_y+1, R): # 오른쪽 세로 부분
            board[i][C-1] = board_refer[i-1][C-1]
        for i in range(purif_y+1, R-1): # 왼쪽 세로 부분
            board[i][0] = board_refer[i+1][0]
        for j in range(purif_x+2, C): # 공기청정기 오른쪽 부분
            board[purif_y][j] = board_refer[purif_y][j-1]
        board[purif_y][purif_x+1] = 0
        # print("circulate final")
        # print_mat(board)
        return
    
    # spread()
    # print(purif)
    # print_mat(board)
    # circulate()
    # print_mat(board)
    time = 0
    while time < T:
        spread()
        circulate()
        time += 1

    answer = sum([sum(b) for b in board])
    answer += 2 # 공기청정기 고려
    print(answer)

# for _ in range(8):
#     main()
main()
