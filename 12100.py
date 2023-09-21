# 2048 (Easy)
# 백트래킹 완전탐색
# 보드판 움직이는거 구현하는게 어려웠음
# 백트래킹시 보드 깊은복사하기, 원본 안 바꿔야지 계속 갈래로 탐색가능

import sys
from copy import deepcopy

sys.stdin = open("testcase/12100.txt", "r")

def print_mat(board):
    for i in range(len(board)):
        print(board[i])
    print(" ")

answer = 0

def main():
    N = int(sys.stdin.readline())
    board = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(N)]

    def move_board(board, dir):
        if dir == 0: # 동
            for i in range(N):
                p = N - 1
                for j in range(N-2, -1, -1):
                    if p < 0:
                        break
                    if board[i][j] != 0:
                        temp = board[i][j]
                        board[i][j] = 0
                        if board[i][p] == 0: # 옆에 숫자 당겨오기
                            board[i][p] = temp
                        elif board[i][p] == temp: # 머지
                            board[i][p] = temp * 2
                            p -= 1
                        else: 
                            p -= 1
                            board[i][p] = temp
                        
        elif dir == 1: # 서
            for i in range(N):
                p = 0
                for j in range(1, N):
                    if p >= N:
                        break
                    if board[i][j] != 0:
                        temp = board[i][j]
                        board[i][j] = 0
                        if board[i][p] == 0: # 옆에 숫자 당겨오기
                            board[i][p] = temp
                        elif board[i][p] == temp: # 머지
                            board[i][p] = temp * 2
                            p += 1
                        else: 
                            p += 1
                            board[i][p] = temp
        elif dir == 2: # 남
            for j in range(N):
                p = N - 1
                for i in range(N-2, -1, -1):
                    if p < 0:
                        break
                    if board[i][j] != 0:
                        temp = board[i][j]
                        board[i][j] = 0
                        if board[p][j] == 0: # 옆에 숫자 당겨오기
                            board[p][j] = temp
                        elif board[p][j] == temp: # 머지
                            board[p][j] = temp * 2
                            p -= 1
                        else: 
                            p -= 1
                            board[p][j] = temp
                    
        elif dir == 3: #북
            for j in range(N):
                p = 0
                for i in range(1, N):
                    if p >= N:
                        break
                    if board[i][j] != 0:
                        temp = board[i][j]
                        board[i][j] = 0
                        if board[p][j] == 0: # 옆에 숫자 당겨오기
                            board[p][j] = temp
                        elif board[p][j] == temp: # 머지
                            board[p][j] = temp * 2
                            p += 1
                        else: 
                            p += 1
                            board[p][j] = temp
        return board
        
    def dfs(step, board):
        global answer
        if step == 5:
            answer = max(answer, max(map(max, board)))
            return
        for i in range(4):
            temp_board = deepcopy(board)
            dfs(step + 1, move_board(temp_board, i))
            # print_mat(temp_board)
    
    # print_mat(board)
    dfs(0, board)
    print(answer)

main()
