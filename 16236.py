# 아기상어

import sys
from collections import deque

sys.stdin = open("testcase/16236.txt", "r")

def main():
    N = int(sys.stdin.readline())
    board = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(N)]
    baby_size = 2
    baby_eat = 0 
    # baby_y; baby_x
    for i in range(N):
        for j in range(N):
            if board[i][j] == 9:
                baby_y = i
                baby_x = j
                board[i][j] = 0

    # fishes = dict()
    # for i in range(1, 7):
    #     fishes[i] = []
    # for i in range(N):
    #     for j in range(N):
    #         if 1 <= board[i][j] <= 6:
    #             fishes[board[i][j]].append((i,j))
    #         if board[i][j] == 9:
    #             baby_y = i
    #             baby_x = j
    #             board[i][j] = 0

    dx = [0, -1, 0, 1] # 북 서 남 동
    dy = [-1, 0, 1, 0]

    # 아기상어가 먹을 물고기의 후보 리스트 반환
    def bfs(y0, x0): # 처음 위치
        dq = deque()
        dq.append((y0, x0, 0))
        visited = [[0]*N for _ in range(N)]
        min_dist = N*N+1
        while dq:
            y, x, cur_dist = dq.popleft()
            if cur_dist > min_dist:
                break
            visited[y][x] = 1
            # print(y, x)
            for i in range(4):
                fx = dx[i] + x
                fy = dy[i] + y
                if fx<0 or fy<0 or fx>=N or fy>=N:
                    continue
                if visited[fy][fx] or board[fy][fx] > baby_size:
                    continue
                if 1 <= board[fy][fx] < baby_size: # eat
                    min_dist = cur_dist + 1
                    eat_cand.append((fy, fx))
                    # print("eat_cand!!", eat_cand)
                else:
                    dq.append((fy, fx, cur_dist + 1))
            

        
        return min_dist

    answer = 0

    while (1):
        print("baby y,x:", baby_y, baby_x)
        print("baby size, eat:", baby_size, baby_eat)
        eat_cand = []
        dist = bfs(baby_y, baby_x)
        if len(eat_cand) == 0:
            break
        
        eat_cand.sort(key=lambda x: (x[0],x[1]))
        print("dist:",dist)
        print("eat_cand:", eat_cand)
        answer += dist
        baby_y, baby_x = eat_cand[0]
        baby_eat += 1
        if baby_eat == baby_size:
            baby_size += 1
            baby_eat = 0
        board[baby_y][baby_x] = 0

    print(answer)


main()
   