# 나무 재테크
# 자료구조, 구현

'''
시간초과 헬인 문제 - pypy3로 통과함
1. for문 개수 최대한 줄이기 (봄-여름, 가을-겨울 결합)
2. 리스트 대신 deque 사용하기
    - 처음에는 딕셔너리 (y,x):age 리스트 사용했으나, deque가 원소인 2d array 사용해야함
    - 더 줄이기 위해서 dict이 원소인 2d array 도 나중에 시도해보자 (key 나무 나이, val 그 개수)
3. 정렬을 유지한다
4. 리스트에서 del by index 보다는, 새로운 리스트를 만들어 제거할 원소 이외의 원소들을 추가하는 방법? 어차피 리스트 참조해서 나이도 하나 늘려줘야하기 때문에 이 방법이 더 효율적이었던 듯 
'''
# reversed(lst): 새로운 리스트를 메모리에 만들지 않음. reverse object여서 그냥 기존 리스트를 역순으로 순회함

import sys
from collections import deque

sys.stdin = open("testcase/16235.txt", "r")

def print_mat(board):
    for b in board:
        print(b)
    print("=======")

def main():
    N, M, K = map(int, sys.stdin.readline().split(" ")) # NxN, 나무 M개, K년 후 나무 개수
    A = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(N)] # 로봇이 추가하는 위치별 양분 양
    trees = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(M)] # 나무 위치(x,y), 나무 나이

    tree_board = [[deque() for _ in range(N)] for _ in range(N)]
    for y, x, age in trees: # 나무 좌표 1,1 에서 시작
        tree_board[y-1][x-1].append(age)

    nut_board = [[5]*N for _ in range(N)] # 각 위치별 양분

    dy = [-1,-1,-1,0,0,1,1,1]
    dx = [-1,0,1,-1,1,-1,0,1]

    def one_year():
        for i in range(N):
            for j in range(N):
                added_nut_by_dead = 0 # summer
                new_trees = deque()
                for tree_age in tree_board[i][j]:
                    if nut_board[i][j] < tree_age: 
                        added_nut_by_dead += tree_age//2 # summer: 봄에 죽은 나무들 -> 양분
                    else:
                        nut_board[i][j] -= tree_age
                        new_trees.append(tree_age+1)
                tree_board[i][j] = new_trees
                nut_board[i][j] += added_nut_by_dead

        # fall: 나무 번식
        for i in range(N):
            for j in range(N):
                for age in tree_board[i][j]:
                    if age % 5 == 0:
                        for k in range(8):
                            fy = i + dy[k]
                            fx = j + dx[k]
                            if fy>=0 and fx>=0 and fy<N and fx<N:
                                tree_board[fy][fx].appendleft(1)
                nut_board[i][j] += A[i][j]


    year = 0
    while (year < K):
        one_year()
        year += 1

    answer = 0
    for i in range(N):
        for j in range(N):
            answer += len(tree_board[i][j])

    print(answer)
    return

for _ in range(8):
    main()
# main()
