# 어항 정리
# 구현, 시뮬레이션
# 디버깅 쉽게 보드 10으로 놓고 했다가 indexError 나서 찾는데 시간 걸림 (원래 100으로 해야하는데)

import sys
from copy import deepcopy

sys.stdin = open("testcase/23291.txt", "r")

def print_mat(board):
    for b in board:
        print(b)
    print(" ")

def move_fish(board, row, col):
    board_ = deepcopy(board)
    # 가로 확인 후 세로 확인하기
    for i in range(row):
        for j in range(col-1):
            if board_[i][j+1] == -1:
                break
            d = abs(board_[i][j] - board_[i][j+1])//5
            if d > 0:
                if board_[i][j] > board_[i][j+1]:
                    board[i][j] -= d
                    board[i][j+1] += d
                else:
                    board[i][j] += d
                    board[i][j+1] -= d
    for j in range(col):
        for i in range(row-1,0,-1):
            if board_[i-1][j] == -1:
                break
            d = abs(board_[i][j] - board_[i-1][j])//5
            # print(i, j, d)
            if d > 0:
                if board_[i][j] > board_[i-1][j]:
                    board[i][j] -= d
                    board[i-1][j] += d
                else:
                    board[i][j] += d
                    board[i-1][j] -= d
    # print("물고기 이주 후")
    # print_mat(board)
    return board

def main():
    N, K = map(int, sys.stdin.readline().split(" "))
    fishes = list(map(int, sys.stdin.readline().split(" ")))
    max_num = max(fishes)
    min_num = min(fishes)
    answer = 0
    fishes_ = fishes[:]
    while (max_num - min_num > K):
        # 물고기의 수가 최소인 어항 모두에 한 마리씩 넣기
        for i in range(N):
            if fishes_[i] == min_num:
                fishes_[i] += 1
        # print("initial", fishes_)
        board = [[-1]*100 for _ in range(100)]
        board[0][1] = fishes_[0]
        board[0][0] = fishes_[1]
        board[1][0] = fishes_[2]
        board[1][1] = fishes_[3]
        row = 2
        col = 2
        next_id = 4
        while row <= N-next_id:
            board_ = deepcopy(board)
            # 오른쪽으로 90도 돌리기: 원점 대칭 + y축 대칭
            for i in range(row):
                for j in range(col):
                    new_i = j
                    new_j = row - i -1
                    board[new_i][new_j] = board_[i][j]
            row_copy = row # swap
            row = col
            col = row_copy
            row += 1
            # 밑 부분 추가해주기
            for j in range(col):
                board[row-1][j] = fishes_[next_id]
                next_id += 1

        for i in range(col, N):
            if next_id >= N:
                break
            board[row-1][i] = fishes_[next_id]
            next_id += 1
            col += 1
            
        # print_mat(board) # 꼬리 형태??
        # print(row, col)
        # 인접 물고기들 동시에 이동
        board = move_fish(board, row, col)
        #어항 일렬로 내려놓기
        idx = 0
        for j in range(col):
            for i in range(row-1, -1, -1):
                if board[i][j] == -1:
                    break
                fishes_[idx] = board[i][j]
                idx += 1
        # print(fishes_)
        # 두번째 공중부양
        board = [[-1]*100 for _ in range(100)]
        for j in range(N//4):
            board[3][j] = fishes_[N-N//4+j]
        for i in range(2, -1, -1):
            if i%2==0:
                for j in range(N//4-1, -1, -1):
                    board[i][j] = fishes_[N//4-1-j + N//4*(2-i)]
            else:
                for j in range(N//4):
                    board[i][j] = fishes_[j + N//4* (2-i)]
        row = 4
        col = N // 4
        # print("두번쨰")
        # print_mat(board)
        board = move_fish(board, row, col)
        #어항 일렬로 내려놓기
        idx = 0
        for j in range(col):
            for i in range(row-1, -1, -1):
                if board[i][j] == -1:
                    break
                fishes_[idx] = board[i][j]
                idx += 1
        # print(fishes_)
        max_num = max(fishes_)
        min_num = min(fishes_)
        answer += 1
        # print("max:", max_num, "min:", min_num)
        
    print(answer)

main()

