# 퇴사
# dp **
import sys

sys.stdin = open("14501.txt", "r")

answer = 0
def main():
    N = int(sys.stdin.readline())
    table = [tuple(map(int, sys.stdin.readline().split(" "))) for _ in range(N)]

    # def dfs(pointer, profit): # 
    #     global answer

    #     duration = table[pointer][0]

    #     if pointer + duration > N:
    #         answer = max(answer, profit)
    #         return
    #     elif pointer + duration == N:
    #         answer = max(answer, profit + table[pointer][1])
    #         return

    #     for next_point in range(pointer + duration, N): 
    #         dfs(next_point, profit + table[pointer][1])
    
    # for start_day in range(N):
    #     dfs(start_day, 0)

    # # print(table)

    dp = [0] * (N+1)
    for i in range(N):
        for j in range(i + table[i][0], N+1):
            dp[j] = max(dp[j], dp[i] + table[i][1])
    answer = dp[-1]
    # print(table)
    # print(dp)
    print(answer)

for _ in range(4):
    answer = 0
    main()
