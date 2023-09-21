# 경사로

import sys
sys.stdin = open("testcase/14890.txt", "r") #

def main():
    N, L = map(int, sys.stdin.readline().split(" "))
    table = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(N)]
    answer = 0

    def is_road(road):
        p1 = 0
        p2 = 1

        cnt = 1
        ll = [] # (높이, 개수))
        while (p2 < N):
            if road[p1] == road[p2]:
                cnt += 1
                p2 += 1
            else:
                ll.append((road[p1], cnt))
                cnt = 1
                p1 = p2
                p2 += 1
        ll.append((road[p2-1], cnt))
        
        # print(ll)

        if len(ll) == 1: # 모두 높이가 같음
            return True
        
        avail = L # 경사로를 놓을 수 있는 남은 칸 수
        flag = 0
        for i in range(len(ll)-1):
            if ll[i][0] - ll[i+1][0] == -1: # 낮은 층 -> 높은 층
                # print("up")
                low_floor = ll[i][1]
                if flag: #  높->낮->높 경우, 이미 설치한 경사로 칸수만큼 빼주기
                    low_floor -= L
                if low_floor >= L:
                    flag = 0
                    continue
                else:
                    return False
    
            elif ll[i][0] - ll[i+1][0] == 1: # 높은 층 -> 낮은 층
                # print("down")
                if ll[i+1][1] >= L:
                    flag = 1
                    continue
                else:
                    return False
            else:
                return False

    
        return True
    
    for row in table:
        t = is_road(row)
        # print(t)
        if t:
            answer += 1

    rev_table = []
    for i in range(N):
        col = []
        for j in range(N):
            col.append(table[j][i])
        rev_table.append(col)
    
    for col in rev_table:
        t = is_road(col)
        # print(t)
        if t:
            answer += 1
    
    print(answer)


for i in range(4):
    main()
