# 연구소 3
# 완전탐색, bfs

import sys
from itertools import combinations
from collections import deque
from copy import deepcopy

sys.stdin = open("testcase/17142.txt", "r")

def print_mat(board):
    for b in board:
        print(b)
    print("-----")

def main():
    N, M = map(int, sys.stdin.readline().split())
    board_org = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] # 0:빈칸 1:벽 2:비활성
    viruses = []
    dx = [0,0,-1,1] # 상하좌우
    dy = [-1,1,0,0]
    tot_empty_cnt = 0
    for i in range(N):
        for j in range(N):
            if board_org[i][j] == 0: # 빈칸
                tot_empty_cnt += 1
            elif board_org[i][j] == 2:
                board_org[i][j] = -2 # 비활성 바이러스
                viruses.append((i,j))
            else: # 벽
                board_org[i][j] = -1


    # 빈칸 모두 사라지면 끝
    # 비활성 -> 활성
    answer = -1
    for act_viruses in list(combinations(viruses, M)):
        board = deepcopy(board_org)
        empty_cnt = tot_empty_cnt # 남아있는 빈칸 개수
        visited = [[0]*N for _ in range(N)]
        dq = deque()
        for act_y, act_x in act_viruses: # 선택된 M개의 바이러스
            board[act_y][act_x] = -3 # 활성 바이러스
            dq.append((act_y, act_x))

        # print("Start")
        # print_mat(board)
        time = 0
        while dq:
            if empty_cnt == 0:
                break
            y, x = dq.popleft()
            visited[y][x] = 1
            if board[y][x] > 0:
                time = board[y][x] + 1
            else:
                time = 1

            for i in range(4):
                fy = y + dy[i]
                fx = x + dx[i]
                if fy<0 or fy>=N or fx<0 or fx>=N:
                    continue
                if visited[fy][fx]==0 and (board[fy][fx]==-2 or board[fy][fx]==0): # 비활성 바이러스, 빈칸
                    if board[fy][fx] == 0: # 빈칸
                        empty_cnt -= 1
                    board[fy][fx] = time
                    dq.append((fy,fx))
                    # visited[fy][fx] = 1
            # print_mat(board)

        if empty_cnt > 0:
            time = -1

        if answer >= 0 and time >= 0:
            answer = min(answer, time)
        elif answer < 0 and time >= 0:
            answer = time

        # print(time)
        # print_mat(board)
        # break

    print(answer)
    return

for _ in range(7):
    main()

