# 스타트와 링크
# 완전탐색
import sys
from itertools import combinations

sys.stdin = open("14889.txt", "r")

answer = 1e9

def main():
    global answer
    N = int(sys.stdin.readline())
    S = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(N)]

    def calc(team):
        cap = 0
        for m1 in team:
            for m2 in team:
                cap += S[m1][m2]
        return cap

    all_mem = [i for i in range(N)]
    all_mem_set = set(all_mem)
    for teamA in combinations(all_mem, N//2):
        teamB = list(all_mem_set - set(teamA))
        teamA = list(teamA)
        answer = min(answer, abs(calc(teamA) - calc(teamB)))

    print(answer)

main()
