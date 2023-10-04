# 아기상어
# 구현, 그래프탐색 (BFS)
# 최소 거리인 상어 찾는 과정에서 헤맴

import sys
from collections import deque

sys.stdin = open("testcase/16236.txt", "r")

def print_mat(board):
    for b in board:
        print(b)


def main():
    N = int(sys.stdin.readline())
    board = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(N)]
    baby_size = 2
    baby_eat = 0 
    for i in range(N):
        for j in range(N):
            if board[i][j] == 9: # 아기상어 위치 저장 후, 칸을 0으로 바꾸기
                baby_y = i
                baby_x = j
                board[i][j] = 0
    # print_mat(board)

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
            if cur_dist > min_dist: # 먹은 물고기의 거리와 같은 거리에 있는 것들만 조사하면 됨
                break
            visited[y][x] = 1
            # print("(y,x):",y, x)
            for i in range(4):
                fx = dx[i] + x
                fy = dy[i] + y
                if fx<0 or fy<0 or fx>=N or fy>=N: # 범위초과
                    continue
                if visited[fy][fx] or board[fy][fx] > baby_size: # 이미 탐색했거나, 먹을 수 없음
                    continue
                if 1 <= board[fy][fx] < baby_size: # 이동하고 먹음
                    if cur_dist + 1 <= min_dist: # 이 조건문 안 추가해서 헤멤!
                        eat_cand.append((fy, fx))
                        visited[fy][fx] = 1
                        min_dist = cur_dist + 1
                    # print("eat_cand!!", eat_cand)
                else: # 칸이 비어있거나 물고기 크기 같은 경우, 이동만 함
                    dq.append((fy, fx, cur_dist + 1))
                    visited[fy][fx] = 1
                # print("DQ:", dq)
            
        return min_dist

    answer = 0

    while (1):
        # print("횟수:", answer)
        # print("baby (y,x), size, eat:", (baby_y, baby_x), baby_size, baby_eat)
        eat_cand = []
        dist = bfs(baby_y, baby_x)
        if len(eat_cand) == 0:
            break
        # print_mat(board)
        # print("eat_cand:", eat_cand)
        eat_cand.sort(key=lambda x: (x[0],x[1]))
        # print("dist:",dist)
        
        answer += dist
        baby_y, baby_x = eat_cand[0]
        baby_eat += 1
        if baby_eat == baby_size:
            baby_size += 1
            baby_eat = 0
        board[baby_y][baby_x] = 0
        # break

    print(answer)

# for _ in range(6):
#     main()
main()
   