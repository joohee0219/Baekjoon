"""
메이즈러너
삼성 23 상 오후 2번
구현

"""

import sys
from copy import deepcopy

sys.stdin = open("./메이즈러너.txt", "r")

def print_mat(board):
    for b in board:
        print(b)
    print("----")

def main():
    N, M, K = map(int, sys.stdin.readline().split())
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    runners = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
    # board_runner = [[[] for _ in range(N)] for _ in range(N)]
    for r, c in runners:
        board[r-1][c-1] -= 1 # 인원수의 음수로 표시

    exit_r, exit_c = map(int, sys.stdin.readline().split())
    exit_r -= 1
    exit_c -= 1
    board[exit_r][exit_c] = -20
    # print("처음 상태")
    # print_mat(board)

    dr = [1,-1,0,0] # 상하좌우
    dc = [0,0,-1,1]

    def move(r, c):  # 도착한 최종 좌표 반환
        dist_exit = abs(exit_r - r) + abs(exit_c - c)
        for i in range(4):
            fr = dr[i] + r
            fc = dc[i] + c
            if 0<=fr<N and 0<=fc<N:
                if board[fr][fc] > 0: # 벽인 경우
                    continue
                if abs(exit_r - fr) + abs(exit_c - fc) > dist_exit:
                    continue
                return fr, fc
        return -1, -1

    def turn_miro(r, c, size): # 돌리려는 정사각형 좌상단의 좌표, 크기
        board_refer1 = deepcopy(board)
        exit_r_ = -1
        exit_c_ = -1
        for i in range(size):
            for j in range(size):
                if board_refer1[r+i][c+j] > 0: # 벽 내구도 깎기
                    board[r+j][c+size-1-i] = board_refer1[r+i][c+j] - 1
                elif board_refer1[r+i][c+j] == -20: # 출구인 경우
                    exit_r_ = r+j
                    exit_c_ = c+size-1-i
                    board[exit_r_][exit_c_] = -20
                else:
                    board[r + j][c + size - 1 - i] = board_refer1[r + i][c + j]
        return exit_r_, exit_c_

    def select_square(): # 좌상단 점의 좌표, 정사각형 크기 반환
        min_size = N # 정사각형 크기 구하기
        cand_runners = [] # 가장 가까운 거리에 위치한 참가자들
        for i in range(N):
            for j in range(N):
                if -20 < board[i][j] < 0:
                    dist = max(abs(i-exit_r), abs(j-exit_c)) + 1
                    if dist <= min_size:
                        min_size = dist
                        cand_runners.append((i,j))
        # 좌상단 점 구하기
        for i in range(exit_r-min_size+1, exit_r+1):
            for j in range(exit_c-min_size+1, exit_c+1):
                if 0<=i<N and 0<=j<N:
                    for r,c in cand_runners:
                        if i<=r<i+min_size and j<=c<j+min_size: # 좌상단점이 i,j인 정사각형에 참가자가 속함
                            return i, j, min_size

        return -1, -1, min_size

    # 자 이제 해보자
    total_dist = 0
    escaped_runners = 0
    for time in range(K):
        board_refer = deepcopy(board)
        # 모든 참가자 동시 이동
        tot_moving_ppl = 0 # 한 타임에 움직이는 인원 계산
        for r in range(N):
            for c in range(N):
                if -20 < board_refer[r][c] < 0: # 참가자
                    fr, fc = move(r, c)
                    if fr == -1: # 움직일 수 없는 경우
                        continue
                    moving_ppl = abs(board_refer[r][c]) # 움직이는 인원
                    tot_moving_ppl += moving_ppl
                    total_dist += moving_ppl  # 이동거리 업데이트
                    board[r][c] += moving_ppl
                    if fr == exit_r and fc == exit_c:  # 탈출
                        escaped_runners += moving_ppl # 탈출한 인원 업데이트
                    elif fr >= 0 and fc >= 0:  # 움직이기
                        board[fr][fc] -= moving_ppl
        # 모두 탈출하면 즉시 종료
        if escaped_runners == M:
            break
        # print("시간:",time+1,"총이동거리:", total_dist, "탈출인원:",escaped_runners)
        # print_mat(board)
        # if tot_moving_ppl == 0:
        #     # print("아무도 움직이지 않음")
        # 미로 돌리기
        r, c, s = select_square()  # 돌릴 정사각혁 고르기
        # print("turn:", r, c, "size:", s)
        if r != -1:
            # print("돌리지 않음")
            exit_r, exit_c = turn_miro(r, c, s) # 돌리기
        # print_mat(board)
    print(total_dist)
    print(exit_r+1, exit_c+1)

main()