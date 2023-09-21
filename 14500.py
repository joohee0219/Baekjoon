# 테트로미노
# dfs, 구현

# 시간 초과로 꽤나 애먹음
# ㅏ의 케이스를 따로 계산하는게 아니라 dfs 안에서 계산할 방법을 찾는 것이 핵심
# visited 리스트를 이중 for loop안에서 매번 새로 만들어주기보다는, 그렸다가 지웠다가 하는 방법 (재활용)이 시간 효율이 더 좋다
import sys

sys.stdin = open("testcase/14500.txt", "r")

def main():
    N, M  = map(int, sys.stdin.readline().split(" "))
    board = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(N)]

    dx = [0, 0, 1, -1] # 북 남 동 서 
    dy = [1, -1, 0, 0]

    global answer
    answer = 0

    def dfs(y, x, cur_sum, step):
        global answer
        # print(x, y, cur_sum, step)
        if step == 4:
            answer = max(answer, cur_sum)
            return
        for k in range(4):
            fx = x + dx[k]
            fy = y + dy[k]
            if fx<0 or fx>=M or fy<0 or fy>=N:
                continue
            if visited[fy][fx] == 0:
                if step == 2:
                    # ㅏ 모양인 경우 3번째 선택에 대해 더하되, 현재 칸에 대해 재귀 반복
                    visited[fy][fx] = 1
                    dfs(y, x, cur_sum + board[fy][fx], step + 1)
                    visited[fy][fx] = 0
                visited[fy][fx] = 1
                dfs(fy, fx, cur_sum + board[fy][fx], step + 1)
                visited[fy][fx] = 0

    visited = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            visited[i][j] = 1
            dfs(i, j, board[i][j], 1)
            visited[i][j] = 0
    
    # # ㅏ 모양일 경우
    # t1 = [[1, 0],[1, 1],[1, 0]] # ㅏ
    # t2 = [[0, 1], [1, 1], [0, 1]] # ㅓ
    # t3 = [[0, 1, 0], [1, 1, 1]] # ㅗ
    # t4 = [[1, 1, 1], [0, 1, 0]] # ㅜ

    # max_sum = 0
    # for i in range(N-2):
    #     for j in range(M-1):
    #         cur_sum1 = 0
    #         cur_sum2 = 0
    #         for k in range(3):
    #             for l in range(2):
    #                 cur_sum1 += board[i+k][j+l] * t1[k][l]
    #                 cur_sum2 += board[i+k][j+l] * t2[k][l]
    #         max_sum = max(max_sum, cur_sum1, cur_sum2)

    # for i in range(N-1):
    #     for j in range(M-2):
    #         cur_sum1 = 0
    #         cur_sum2 = 0
    #         for k in range(2):
    #             for l in range(3):
    #                 cur_sum1 += board[i+k][j+l] * t3[k][l]
    #                 cur_sum2 += board[i+k][j+l] * t4[k][l]
    #         max_sum = max(max_sum, cur_sum1, cur_sum2)

    # answer = max(answer, max_sum)
    print(answer)

main()
