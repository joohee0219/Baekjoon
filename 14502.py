# 연구소
'''
왜 헤맸나
1. 2d array의 shallow copy는 단순히 lab[:] 으로 안됨 -> [row[:] for row in lab] 식으로 해야함
2. 함수 내 for loop argument 중복 사용함
'''
import sys
from collections import deque

def main():
    #sys.stdin = open("14502.txt", "r")
    N, M = map(int, sys.stdin.readline().split(" "))
    lab = [[0 for _ in range(M)] for _ in range(N)]
    empty = []
    virus = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(N):
        line = list(map(int, sys.stdin.readline().split(" ")))
        for j in range(M):
            lab[i][j] = line[j]
            if line[j] == 0:
                empty.append((i,j))
            elif line[j] == 2:
                virus.append((i,j))
            else:
                continue

    # def print_mat(mat):
    #     for m in mat:
    #         print(m)
    #     print(" ")

    
    def can_spreadto(x, y):
        if (x>=0 and x<M and y>=0 and y<N):
            if lab[y][x] == 0:
                return True
        return False


    def bfs(root_x, root_y, visited):
        queue = deque()
        queue.append((root_x, root_y))
        while (len(queue)>0):
            x, y = queue.popleft()
            for i in range(4):
                fx = x + dx[i]
                fy = y + dy[i]
                if can_spreadto(fx, fy) and visited[fy][fx] == 0:
                    visited[fy][fx] = 2
                    queue.append((fx, fy))
                
    # 벽 세우기
    max_safe = -1
    for i in range(len(empty)):
        for j in range(i):
            for k in range(j):
                lab[empty[i][0]][empty[i][1]] = 1
                lab[empty[j][0]][empty[j][1]] = 1
                lab[empty[k][0]][empty[k][1]] = 1

                # 바이러스 퍼뜨리기
                # visited = [row[:] for row in lab] # shallow copy..
                visited = [[0]*M for _ in range(N)]
                for vy, vx in virus:
                    bfs(vx, vy, visited)
                
                # 안전영역 크기 계산
                safe_cnt = 0
                for a in range(N):
                    for s in range(M):
                        if visited[a][s]==0 and lab[a][s] == 0 :
                            safe_cnt += 1
                
                max_safe = max(max_safe, safe_cnt)

                # 벽 원상복구
                lab[empty[i][0]][empty[i][1]] = 0
                lab[empty[j][0]][empty[j][1]] = 0
                lab[empty[k][0]][empty[k][1]] = 0


    return max_safe
                    
print(main())



        

            
            