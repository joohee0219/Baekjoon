# 톱니바퀴
# 구현
# 문제 제대로 읽기

import sys
from copy import deepcopy

sys.stdin = open("14891.txt", "r")

def main():
    wheels = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(4)]
    K = int(sys.stdin.readline())
    turn_info = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(K)]
    # print(wheels)

    def turn_wheel(w_num, dir):
        temp = wheels[w_num][:]
        if dir == 1: # 시계
            wheels[w_num][0] = temp[7]
            for i in range(1, 8):
                wheels[w_num][i] = temp[i-1]
        elif dir == -1: # 반시계
            wheels[w_num][-1] = temp[0]
            for i in range(7):
                wheels[w_num][i] = temp[i+1]
        return


    for w_num, dir in turn_info:
        w_num -= 1
        # 각 바퀴의 회전 방향 조사하기
        dir_lst = [0]*4
        dir_lst[w_num] = dir
        if w_num == 1 or w_num == 2:
            if wheels[w_num][2] != wheels[w_num+1][6]: # 오 
                dir_lst[w_num+1] = dir * -1
                if w_num == 1 and wheels[2][2] != wheels[3][6]:
                    dir_lst[3] = dir_lst[2] * -1
            if wheels[w_num][6] != wheels[w_num-1][2]: # 왼
                dir_lst[w_num-1] = dir * -1
                if w_num == 2 and wheels[0][2] != wheels[1][6]:
                    dir_lst[0] = dir_lst[1] * -1
            
        elif w_num == 0:
            for i in range(3):
                if wheels[i][2] != wheels[i+1][6]:
                    dir_lst[i+1] = dir_lst[i] * (-1)

        elif w_num == 3:
            for i in range(3, 0, -1):
                if wheels[i][6] != wheels[i-1][2]:
                    dir_lst[i-1] = dir_lst[i] * (-1)
        
        # print(dir_lst)
        # 동시에 회전시키기
        for i in range(4):
            turn_wheel(i, dir_lst[i])
        # print(wheels)
    
    # 점수 계산
    answer = 0
    for i in range(4):
        answer += wheels[i][0] * (2**i)
    print(answer)

for _ in range(4):
    main()
