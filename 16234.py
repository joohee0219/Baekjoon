# 인구 이동
# 구현

import sys
from collections import deque

sys.stdin = open("16234.txt", "r")

def print_mat(earth):
    for i in range(len(earth)):
        print(earth[i])
    print(" ")


def main():
    N, L, R = map(int, sys.stdin.readline().split(" "))

    earth = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(N)]

    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    #####
    # r,c 에 대한 연합진행
    def bfs(r, c):
        sum_popul = earth[r][c]
        queue = deque()
        queue.append((r,c))
        visited[r][c] = 1
        union = [(r,c)]
        while queue:
            r, c = queue.popleft()
            for i in range(4):
                rr = r + dy[i]
                cc = c + dx[i]
                if rr<0 or rr>=N or cc<0 or cc>=N:
                    continue
                if visited[rr][cc] == 1:
                    continue
                sub = abs(earth[r][c] - earth[rr][cc])
                if sub >= L and sub <= R:
                    queue.append((rr, cc))
                    union.append((rr, cc))
                    sum_popul += earth[rr][cc]
                    visited[rr][cc] = 1

        if len(union) == 1:
            return 1
        # 인구 이동
        after_pop = sum_popul // len(union)
        for r, c in union:
            earth[r][c] = after_pop
        
        return len(union)

    day = 0
    while (1):
        flag = 0
        visited = [[0]*N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if visited[i][j] == 1:
                    continue
                if bfs(i, j) > 1:
                    # print_mat(earth)
                    flag = 1
                    
        # print("ZZZ")
        # print_mat(earth)
                
        if flag == 0: # 연합이동 더 이상 없음
            break

        day += 1
        
    
    print(day)    
    return day
    
main()
