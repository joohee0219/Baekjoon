import sys

sys.stdin = open("14499.txt", "r")

def main():
    N, M, y, x, K = map(int, sys.stdin.readline().split(" "))
    jido = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(N)]
    order = list(map(int, sys.stdin.readline().split(" ")))

    dice = [0]*7 # 첫번째는 더미, 인덱스 1 이 윗면, 6이 아랫면

    # 동서북남 1234
    def turn_dice(dir):
        dice_ = dice[:]
        if dir == 1: # 동
            dice[1] = dice_[4]
            dice[3] = dice_[1]
            dice[4] = dice_[6]
            dice[6] = dice_[3]
        elif dir == 2: #서
            dice[1] = dice_[3]
            dice[3] = dice_[6]
            dice[4] = dice_[1]
            dice[6] = dice_[4]
        elif dir == 3: #북
            dice[1] = dice_[5]
            dice[2] = dice_[1]
            dice[5] = dice_[6]
            dice[6] = dice_[2]
        elif dir == 4: #남
            dice[1] = dice_[2]
            dice[2] = dice_[6]
            dice[5] = dice_[1]
            dice[6] = dice_[5]

    # 동서북남 1234 (첫번쨰는 더미)
    dx = [0, 1, -1, 0, 0]
    dy = [0, 0, 0, -1, 1]
    # 처음 시작에는 무조건 주사위 바닥면 -> 지도 칸
    jido[y][x] = dice[6]

    for dir in order:
        fx = x + dx[dir]
        fy = y + dy[dir]
        if fx < 0 or fx >= M or fy < 0 or fy >= N:
            continue
        x = fx
        y = fy
        turn_dice(dir)
        # 칸이 0이면, 주사위의 바닥면에 쓰여 있는 수가 칸에 복사
        if jido[y][x] == 0:
            jido[y][x] = dice[6]
        # 0이 아닌 경우, 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사, 칸에 쓰여 있는 수는 0이 된다
        else:
            dice[6] = jido[y][x]
            jido[y][x] = 0
        # 이동할때마다 주사위 윗면 출력
        print(dice[1]) 

main()
