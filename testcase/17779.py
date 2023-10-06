# 게리맨더링 2
# 구현

import sys

sys.stdin = open("testcase/17779.txt", "r")

def print_mat(board):
    for b in board:
        print(b)
    print("----")

def main():
    N = int(sys.stdin.readline().split()[0])
    A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    # 좌표 1,1 부터 시작
    '''
        u
    l       r
        b
    '''
    def draw_area(y,x,d1,d2):
        lx, ly = x, y
        ux, uy = x+d1, y-d1
        rx, ry = x+d1+d2, y-d1+d2
        bx, by = x+d2, y+d2
        # print(lx,ly)
        # print(ux,uy)
        # print(rx,ry)
        # print(bx,by)

        # 5번 경계 그리기
        for k in range(d1+1):
            board[lx+k][ly-k] = 5
            board[bx+k][by-k] = 5
        for k in range(d2+1):
            board[lx+k][ly+k] = 5
            board[ux+k][uy+k] = 5
        
        # 5번 경계 채우기
        for r in range(N):
            is_five = []
            for c in range(N):
                if board[r][c] == 5:
                    is_five.append(c)
            if len(is_five) == 2:
                for i in range(is_five[0]+1, is_five[1]):
                    board[r][i] = 5
        # print_mat(board)

        # 나머지 구역
        for r in range(N):
            for c in range(N):
                if board[r][c] == 5:
                    continue
                if 0<=r<ux and 0<=c<=ly:
                    board[r][c] = 1
                elif 0<=r<=bx and ly-1<c<=N-1:
                    board[r][c] = 2
                elif ux<=r<=N-1 and 0<=c<ry:
                    board[r][c] = 3
                elif bx<r<=N-1 and ry<=c<=N-1:
                    board[r][c] = 4

        # print_mat(board)
        ppl_dict = {1:0, 2:0, 3:0, 4:0, 5:0}
        for r in range(N):
            for c in range(N):
                ppl_dict[board[r][c]] += A[r][c]
        # print(ppl_dict)
        
        return max(ppl_dict.values()) - min(ppl_dict.values())
    
    
    answer = 1e5
    for y in range(1, N-1):
        for x in range(1, N):
            for d1 in range(1, y):
                for d2 in range(1, min(N-y, N-x-d1)):
                    # print(y,x,d1,d2)
                    board = [[0]*N for _ in range(N)]
                    answer = min(answer, draw_area(y,x,d1,d2))

    print(answer)

for _ in range(3):
    main()
# main()
# 
