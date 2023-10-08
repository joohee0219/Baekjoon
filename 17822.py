# 원판 돌리기
# 구현

import sys
from collections import deque

sys.stdin = open("testcase/17822.txt", "r")

def print_mat(board):
    for b in board:
        print(b)
    print("----")


def main():
    N, M, T = map(int, sys.stdin.readline().split()) # 원판 개수, 원판에 적힌 숫자 개수, 원판 회전 횟수
    disk = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    turn_info = [list(map(int, sys.stdin.readline().split())) for _ in range(T)] # x,d,k: 번호가 x의 배수인 원판을, d방향으로, k칸 회전
    # d=0 시계, d=1 반시계

    def turn_disk(idx, d, k): # 번호가 idx인 디스크를 d 방향으로 k 칸 회전한 결과 출력
        k %= M
        if d == 1:
            k = M-k
        new_disk = [0]*M
        for i, num in enumerate(disk[idx]):
            new_disk[(i+k)%M] = num
        return new_disk
    
    def adj_num(i, j): # i번 원판의 j번째 수와 인접한 숫자 위치 리스트 반환 [(i,j)]
        adj_lst = []
        if j==0:
            adj_lst.append((i,j+1))
            adj_lst.append((i,M-1))
        elif j==M-1:
            adj_lst.append((i,j-1))
            adj_lst.append((i,0))
        else:
            adj_lst.append((i,j-1))
            adj_lst.append((i,j+1))

        if i==0:
            adj_lst.append((i+1,j))
        elif i==N-1:
            adj_lst.append((i-1,j))
        else:
            adj_lst.append((i-1,j))
            adj_lst.append((i+1,j))
        
        return adj_lst
    
    num_cnt = M*N # 원판에 남아있는 숫자 개수
    # 원판 T번 회전
    for x, d, k in turn_info:
        for idx in range(N):
            if (idx+1) % x == 0: # x의 배수인 원판 돌리기
                disk[idx] = turn_disk(idx, d, k)

        # 인접하면서 수가 같은 것을 지우기
        is_same = 0 # 인접 같은 수 있는지
        for i in range(N):
            for j in range(M):
                target_num = disk[i][j]
                if target_num == 0: # 이미 지워진 숫자
                    continue
                # BFS로 같은 숫자 찾기
                # same_num = []
                visited = [[0]*M for _ in range(N)]
                dq = deque()
                dq.append((i,j))
                while dq:
                    root_i, root_j = dq.pop()
                    for ai, aj in adj_num(root_i,root_j):
                        if visited[ai][aj] == 0:
                            if disk[ai][aj] == target_num:
                                # same_num.append((ai,aj))
                                disk[ai][aj] = 0 # 숫자 지우기
                                num_cnt -= 1
                                dq.append((ai,aj))
                                visited[ai][aj] = 1
                                is_same = 1

        if is_same == 0: # 원판에 적힌 수의 평균을 구하고, 평균보다 큰 수에서 1을 빼고, 작은 수에는 1을 더한다
            avg = sum(sum(disk[i]) for i in range(N)) / num_cnt
            for i in range(N):
                for j in range(M):
                    if disk[i][j] > avg:
                        disk[i][j] -= 1
                    elif 0< disk[i][j] < avg:
                        disk[i][j] += 1

        if num_cnt == 0: # 원판에 남아있는 수 없으면 즉시 종료
            break

    answer = sum(sum(disk[i]) for i in range(N))
        
    # print_mat(disk)
    print(answer)

# main()

for _ in range(5):
    main()

        
