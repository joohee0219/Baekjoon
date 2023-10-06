# 이차원 배열과 연산
# 구현
'''
시간복잡도: answer * R * C
'''
import sys
from collections import defaultdict

sys.stdin = open("testcase/17140.txt", "r")

def print_mat(A):
    for a in A:
        print(a)
    print("-----")

def main():
    R, C, K = map(int, sys.stdin.readline().split())
    A = [list(map(int, sys.stdin.readline().split())) for _ in range(3)] # 3x3으로 시작
    # print_mat(A)
    row = 3
    col = 3
    answer = 0

    while (True):
        if (R-1 < row and C-1 < col and A[R-1][C-1] == K) or answer>100:
            break

        if row < col: # R연산
            max_row = 0
            temp_A = []
            # 들어갈 수 계산
            for j in range(col):
                num_dict = defaultdict(int)
                for i in range(row):
                    if A[i][j] != 0:
                        num_dict[A[i][j]] += 1
                num_lst = [[k,v] for k, v in num_dict.items()] # 수, 등장횟수
                num_lst.sort(key=lambda x: (x[1],x[0]))
                new_num_lst = []
                for k, v in num_lst:
                    new_num_lst.append(k)
                    new_num_lst.append(v)
                if len(new_num_lst) > 100:
                    new_num_lst = new_num_lst[:50]
                max_row = max(max_row, len(new_num_lst))
                temp_A.append(new_num_lst)
            # 크기 맞추기
            row = max_row # 행 크기 업데이트
            for line in temp_A:
                if len(line) < max_row:
                    line.extend([0]*(max_row-len(line)))
            A = [[0]*col for _ in range(row)]
            # 뒤집기
            for j in range(col):
                for i in range(row):
                    A[i][j] = temp_A[j][i]

        else: # C연산
            max_col = 0
            temp_A = []
            # 들어갈 수 계산
            for i in range(row):
                num_dict = defaultdict(int)
                for j in range(col):
                    if A[i][j] != 0:
                        num_dict[A[i][j]] += 1
                num_lst = [[k,v] for k, v in num_dict.items()] # 수, 등장횟수
                num_lst.sort(key=lambda x: (x[1],x[0]))
                new_num_lst = []
                for k, v in num_lst:
                    new_num_lst.append(k)
                    new_num_lst.append(v)
                if len(new_num_lst) > 100:
                    new_num_lst = new_num_lst[:50]
                max_col = max(max_col, len(new_num_lst))
                temp_A.append(new_num_lst)
            # 크기 맞추기
            col = max_col # 행 크기 업데이트
            for line in temp_A:
                if len(line) < max_col:
                    line.extend([0]*(max_col-len(line)))
            A = temp_A
        
        answer += 1
        # print(row, col)
        # print_mat(A)
 
    if answer == 101:
        answer = -1 

    print(answer)

    return

# main()
for _ in range(6):
    main()
