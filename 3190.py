# 뱀
# 구현
# 시간 세는거 조심하기
import sys
from collections import deque

sys.stdin = open("testcase/3190.txt", "r")

def print_mat(board):
    for i in range(len(board)):
        print(board[i])
    print(" ")

def main():
    N = int(sys.stdin.readline())
    K = int(sys.stdin.readline())
    apples = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(K)]
    L = int(sys.stdin.readline())
    snake_info = []
    for _ in range(L):
        temp = sys.stdin.readline().split(" ")
        snake_info.append((int(temp[0]), temp[1].strip()))
    snake_info = dict(snake_info)

    board = [[0]*N for _ in range(N)]

    for y, x in apples:
        board[y-1][x-1] = 2 # 사과

    board[0][0] = 1 # 뱀

    # for t, dir in snake_info:

    time = 1
    time_key = snake_info.keys()
    dx = [1, 0, -1, 0] # 동남서죽
    dy = [0, 1, 0, -1]
    dir = 0 # 처음에 오른쪽 바라봄
    x = 0
    y = 0
    snake_body = deque()
    snake_body.append((0,0)) # (y,x)

    while (1):
        # 뱀 머리를 다음 칸에 위치
        ny = y + dy[dir]
        nx = x + dx[dir]
        if ny < 0 or ny >= N or nx < 0 or nx >= N or board[ny][nx] == 1:
            break # 게임 끝
        
        # 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워줌
        if board[ny][nx] != 2:
            tail = snake_body.popleft()
            board[tail[0]][tail[1]] = 0
        
        board[ny][nx] = 1
        snake_body.append((ny, nx))
        y = ny
        x = nx

        # 뱀 방향 돌려야하는지 확인
        if time in time_key:
            if snake_info[time] == 'D': # 오른쪽으로 회전
                # dir = (dir+1) % 4
                dir += 1
                if dir == 4:
                    dir = 0
            else: # 왼쪽
                dir -= 1
                if dir == -1:
                    dir = 3

        time += 1
        # print(time - 1, "초 후", dir)
        # print_mat(board)
    
    print(time)

main()
