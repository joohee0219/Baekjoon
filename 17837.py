# 새로운 게임 2
# 구현

import sys

sys.stdin = open("testcase/17837.txt", "r")

def print_mat(board):
    for b in board:
        print(b)
    print("----")

# 움직일 수 없으면 스킵하는 코드 추가하기 -> 필요없었음!

def main():
    N, K = map(int, sys.stdin.readline().split()) # 체스판 크기, 말 개수
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] # 0,1,2: 흰,빨,파
    horses = [list(map(int, sys.stdin.readline().split())) for _ in range(K)] # 행 열 방향. 1234: 오왼상하
    for i in range(K):
        horses[i][0] -= 1
        horses[i][1] -= 1

    board_status = [[[] for _ in range(N)] for _ in range(N)] # 말의 위치. 리스트 가장 앞이 바닥에 있는 말

    dx = [0, 1, -1, 0, 0]
    dy = [0, 0, 0, -1, 1]

    def change_dir(d):
        if d==1: return 2
        elif d==2: return 1
        elif d==3: return 4
        elif d==4: return 3
        return -1
    
    for i, (y, x, d) in enumerate(horses):
        board_status[y][x] = [i]

    def move_horse(k,y,x,fy,fx):
        if fy<0 or fy>=N or fx<0 or fx>=N or board[fy][fx]==2:
            horses[i][2] = change_dir(horses[i][2])
            fy = y + dy[horses[i][2]]
            fx = x + dx[horses[i][2]]
            if 0<=fy<N and 0<=fx<N and board[fy][fx]!=2: # 또 파란칸이면 움직이지 않기
                move_horse(k,y,x,fy,fx)

        elif 0 <= board[fy][fx] <= 1: # 흰빨
            horse_idx = board_status[y][x].index(k)
            moving_part = board_status[y][x][horse_idx:] # 움직일 부분
            if board[fy][fx]==1: # 빨간색이면, 순서 뒤집기
                moving_part.reverse()

            if len(board_status[fy][fx]) > 0: # 이미 말이 있는 경우
                board_status[fy][fx].extend(moving_part)
            else:
                board_status[fy][fx] = moving_part
            for h in moving_part: # 움직인 말들 정보 업데이트
                horses[h][0] = fy
                horses[h][1] = fx
            for _ in range(len(moving_part)): # 전칸의 움직인 말 비우기
                board_status[y][x].pop() 

        # 종료조건 확인
        if 0<=fy<N and 0<=fx<N and len(board_status[fy][fx]) >= 4:
            return 1
        
        return 0

    # print_mat(board_status)
    turn = 1
    is_end = 0
    while True:
        for i in range(K): # 0~K-1 말 이동
            y, x, d = horses[i]
            is_end = move_horse(i, y, x, y + dy[d], x + dx[d]) # 1이면 말이 4개 이상 쌓임
            if is_end:
                break
        # print_mat(board_status)
        if is_end:
            break
        turn += 1
        if turn >= 1000:
            turn = -1
            break

    print(turn)

# main()

for _ in range(5):
    main()




            




