import sys
from itertools import combinations

sys.stdin = open("testcase/15686.txt", "r")

def main():
    N, M = map(int, sys.stdin.readline().split(" "))
    city = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(N)]
    chicken = []
    house = []
    for i in range(N):
        for j in range(N):
            if city[i][j] == 2:
                chicken.append((i,j))
            elif city[i][j] == 1:
                house.append((i,j))

    min_dist = 1e9
    for chi in combinations(chicken, M):
        # 각 집에서의 치킨거리 구하기
        sum_dist = 0
        for y, x in house:
            sum_dist += min(map(lambda c: abs(c[0]-y) + abs(c[1]-x), chi))
        min_dist = min(min_dist, sum_dist)

    print(min_dist)

main()
