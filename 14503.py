# 로봇 청소기 (구현)

import sys

sys.stdin = open("14503.txt", "r")

def print_mat(room):
    for i in range(len(room)):
        print(room[i])
    print(" ")

def main():
    N, M = map(int, sys.stdin.readline().split(" "))
    r, c, d = map(int, sys.stdin.readline().split(" "))

    room = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(N)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    cnt_cleaned = 0
    
    # 북 동 남 서 0 1 2 3

    # 주변 4칸에 청소하지 않은 빈칸이 있으면, true
    def is_around_nc(r, c):
        for i in range(4):
            fx = c + dx[i]
            fy = r + dy[i]
            if room[fy][fx] == 0:
                return True
        return False
    
    def go_one(r, c, d, is_back=False):
        one = 1
        if is_back: # 후진
            one = -1
        if d == 0:
            return (r-one, c)
        elif d == 1:
            return (r, c+one)
        elif d == 2:
            return (r+one, c)
        elif d == 3:
            return (r, c-one)

    def turn_counter(d):
        dd = d - 1
        if dd == -1:
            dd = 3
        return dd

        
    while (1):
        if room[r][c] == 0:
            room[r][c] = 2 # 청소한 상태: 2
            cnt_cleaned += 1
        
        if not is_around_nc(r, c):
            # 방향 유지한채 1칸 후진
            rr, cc = go_one(r, c, d, True)
            if room[rr][cc] != 1:
                r = rr
                c = cc
            else: # 후진 불가능하면 작동 멈추기
                break
        else:
            # 반시계방향 회전
            d = turn_counter(d)
            # 앞쪽 칸 청소 안된 빈칸이면 전진
            rr, cc = go_one(r, c, d)
            if room[rr][cc] == 0:
                r = rr
                c = cc
    
    #print_mat(room)
    print(cnt_cleaned)
    return cnt_cleaned

main()
