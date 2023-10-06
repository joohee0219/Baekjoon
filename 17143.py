# 낚시왕
# 구현
'''
시간복잡도: R*C*M = 10^8 = 1억 = 1초
pypy3로만 통과
최적화해보면 좋을듯
'''
import sys

sys.stdin = open("testcase/17143.txt", "r")

def print_mat(board):
    for b in board:
        print(b)
    print("-----")

def main():
    R, C, M = map(int, sys.stdin.readline().split()) # 격자판 크기, 상어 개수
    board = [[-1 for _ in range(C+1)] for _ in range(R+1)] # 상어의 idx 저장
    shark_info = {} # 상어 정보 저장. key: 크기, val: (r,c,v,d)
    for i in range(M):
        r, c, v, d, s = map(int, sys.stdin.readline().split())
        shark_info[s] = (r,c,v,d)
        board[r][c] = s # 상어 크기를 idx로
    # print_mat(board)
    # print("shark", shark_info)

    # d: 1~4 위, 아래, 오, 왼
    dc = [2, 0, 0, 1, -1]
    dr = [2, -1, 1, 0, 0]

    def move_shark():
        board = [[-1 for _ in range(C+1)] for _ in range(R+1)] # 초기화
        for s, (r,c,v,d) in shark_info.items():
            if r==-1: # 이미 죽은 상어
                continue 
            # 1초후 상어 최종 위치, 방향 계산
            step = 0
            fc = c
            fr = r
            fd = d
            if fd==3 or fd==4: # 오른쪽, 왼쪽
                while (step < v):
                    if fc==C:
                        fd = 4
                    elif fc==1:
                        fd = 3
                    fc += dc[fd]
                    step += 1
                    
            elif fd==1 or fd==2: # 위, 아래
                while (step < v):
                    if fr==R:
                        fd = 1
                    elif fr==1:
                        fd = 2
                    fr += dr[fd]
                    step += 1
            # 상어 위치가 겹칠 경우
            if board[fr][fc] != -1: #비어 있지 않다면
                shark_size = board[fr][fc]
                if s > shark_size:
                    shark_info[shark_size] = (-1,-1,-1,-1)
                    board[fr][fc] = s # 상어 idx 새로 새기기
                    shark_info[s] = (fr,fc,v,fd)
                else:
                    shark_info[s] = (-1,-1,-1,-1)
            else: # 비어 있으면
                board[fr][fc] = s # 상어 크기 새로 새기기
                shark_info[s] = (fr,fc,v,fd)

        return board

    answer = 0 # 잡은 상어 크기의 합
    for j in range(1, C+1):
        for i in range(1,R+1):
            if board[i][j] != -1: # 가장 가까운 상어
                size = board[i][j]
                answer += size
                board[i][j] = -1 # 상어 없애기
                shark_info[size] = (-1,-1,-1,-1)
                break
        # 상어 이동
        # print_mat(board)
        board = move_shark()
        # print_mat(board)
        # print(shark_info)
        # break

    print(answer)


    return
for _ in range(4):
    main()
# main()
