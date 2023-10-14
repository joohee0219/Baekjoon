"""
[24, 23, 22, 21, 20]
[9, 8, 7, 6, 19]
[10, 1, 0, 5, 18]
[11, 2, 3, 4, 17]
[12, 13, 14, 15, 16]
"""
# 각 방향마다 이동한 칸 수
# 1,1,2,2,3,3,4,4,5
N = 5
board = [[0]*N for _ in range(N)]
start = (2,2)
dy = [0,1,0,-1] # 좌하우상
dx = [-1,0,1,0]

def init():
    direction = 0  # 방향
    num = 0  # 보드판에 박을 숫자
    dist = 1  # 같은 dist만큼 2번 움직이는 것을 완료할 때마다 +1 해주기
    move_cnt = 0  # 방향으로 움직인 횟수
    fx = start[0]
    fy = start[1]
    while True:
        move_cnt += 1 # dist 바뀌기 전까지
        for _ in range(dist): # 해당 방향으로 dist만큼 움직이기
            fx = fx + dx[direction]
            fy = fy + dy[direction]
            if fx == -1 and fy == 0:
                return
            num += 1
            board[fy][fx] = num

        direction = (direction + 1) % 4
        if move_cnt == 2:
            move_cnt = 0
            dist += 1


init()
for b in board:
    print(b)





