# 삼성 23년도 상반기 오전 1번
# 포탑 부수기
# 구현, BFS

import sys
from collections import deque

sys.stdin = open("포탑부수기.txt", "r")

def print_mat(board):
    for b in board:
        print(b)
    print("----")

def main():
    N, M, K = map(int, sys.stdin.readline().split())
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    attacker_time = [[0 for _ in range(M)] for _ in range(N)]
    dr = [0, 1, 0, -1] # 우하좌상
    dc = [1, 0, -1, 0]

    def choose(): # 공격자 행열, 공격대상자 행열
        attacker_cand = []
        target_cand = []
        min_score = 5000
        max_score = 1
        for i in range(N): # 후보들 구하기
            for j in range(M):
                if 0 < board[i][j] < min_score:
                    min_score = board[i][j]
                    attacker_cand = [(i,j)]
                elif board[i][j] == min_score:
                    attacker_cand.append((i,j))
                if board[i][j] > max_score:
                    max_score = board[i][j]
                    target_cand = [(i,j)]
                elif board[i][j] == max_score:
                    target_cand.append((i,j))

        final_attacker = attacker_cand[0]
        final_target = target_cand[0]

        if len(attacker_cand) > 1: # 동률이라면
            recent_attack = 0
            attacker_cand2 = []
            # 가장 최근에 공격한 포탑 고르기 (첫 공격자 선정에서는 이 조건이 무조건 동률)
            for idx, (i, j) in enumerate(attacker_cand):
                if idx == 0:
                    recent_attack = attacker_time[i][j]
                    attacker_cand2 = [(i, j, i+j)]
                    continue
                if time == 0:
                    attacker_cand2.append((i, j, i+j))
                    continue
                if attacker_time[i][j] > recent_attack:
                    recent_attack = attacker_time[i][j]
                    attacker_cand2 = [(i, j, i+j)]
                elif attacker_time[i][j] == recent_attack:
                    attacker_cand2.append((i, j, i+j))
            attacker_cand2.sort(key=lambda x: [-x[2], -x[1]])
            final_attacker = attacker_cand2[0][:2]

        if len(target_cand) > 1:
            oldest_attack = 0
            target_cand2 = []
            # 가장 오래된 공격한 포탑 고르기 (첫 공격자 선정에서는 이 조건이 무조건 동률)
            for idx, (i, j) in enumerate(target_cand):
                if idx == 0:
                    oldest_attack = attacker_time[i][j]
                    target_cand2 = [(i, j, i+j)]
                    continue
                if time == 0:
                    target_cand2.append((i, j, i+j))
                    continue
                if attacker_time[i][j] < oldest_attack:
                    oldest_attack = attacker_time[i][j]
                    target_cand2 = [(i, j, i+j)]
                elif attacker_time[i][j] == oldest_attack:
                    target_cand2.append((i, j, i+j))
            target_cand2.sort(key=lambda x: [x[2], x[1]])
            final_target = target_cand2[0][:2]

        return final_attacker, final_target

    def move(r, c, dir): # dir방향으로 1칸 움직인 최종 좌표
        fr = r + dr[dir]
        fc = c + dc[dir]
        if fr == -1:
            fr = N - 1
        elif fr == N:
            fr = 0
        if fc == -1:
            fc = M - 1
        elif fc == M:
            fc = 0
        return fr, fc

    def raser_attack(att_r, att_c, tar_r, tar_c): # 공격성공여부 반환. dfs
        visited = [[0 for _ in range(M)] for _ in range(N)]
        dq = deque()
        dq.append((att_r, att_c, [])) # r, c, 이동거리, 이동방향들(0~4)
        is_success = 0 # 레이저공격 성공 여부
        while dq:
            r, c, directions = dq.popleft()
            if r == tar_r and c == tar_c: # 공격대상에 도착함 (공격력 까기)
                # print(directions)
                attacker_score = board[att_r][att_c]
                next_r = att_r
                next_c = att_c
                for dir in directions: # 공격 경로에 있는 포탑들(+공격대상자) 점수 까기
                    next_r, next_c = move(next_r, next_c, dir)
                    if next_r == tar_r and next_c == tar_c:
                        board[next_r][next_c] -= attacker_score
                    else:
                        board[next_r][next_c] -= attacker_score // 2
                    if board[next_r][next_c] > 0:
                        attack_relevant.append((next_r, next_c))
                is_success = 1
                break
            # DFS
            visited[r][c] = 1
            for i in range(4):
                fr, fc = move(r, c, i)
                if visited[fr][fc] == 0 and board[fr][fc] > 0:
                    new_directions = directions[:]
                    new_directions.append(i)
                    dq.append((fr, fc, new_directions))

        return is_success

    def around(tar_r, tar_c): # 주변 8칸의 좌표 반환 (가장자리 상황 고려해서)
        points = []
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                if i == 0 and j == 0:
                    continue
                fr = tar_r + i
                fc = tar_c + j
                if fr == -1:
                    fr = N - 1
                elif fr == N:
                    fr = 0
                if fc == -1:
                    fc = M - 1
                elif fc == M:
                    fc = 0
                points.append((fr,fc))
        return points

    def throw_attack(att_r, att_c, tar_r, tar_c):
        attacker_score = board[att_r][att_c]
        board[tar_r][tar_c] -= attacker_score # 공격 대상자
        if board[tar_r][tar_c] > 0:
            attack_relevant.append((tar_r, tar_c))
        for r, c in around(tar_r, tar_c): # 대상자 주위
            if r == att_r and c == att_c: # 공격자는 영향받지 x
                continue
            if board[r][c] > 0:
                board[r][c] -= attacker_score // 2
            if board[r][c] > 0:
                attack_relevant.append((r, c))
        return
    #
    # print("초기 상태")
    # print_mat(board)

    for time in range(K):
        # print("시간:", time+1)
        attack_relevant = [] # 공격 피해 입은 포탄 중 공격력 양수인 포탄 (공격대상자 포함)
        # 공격자 선정
        attacker, target = choose()
        board[attacker[0]][attacker[1]] += N+M
        # print("공격자:", attacker, "공격대상:", target)
        # print_mat(board)
        # 포탄 공격
        if not raser_attack(attacker[0], attacker[1], target[0], target[1]):
            # print("포탄공격")
            throw_attack(attacker[0], attacker[1], target[0], target[1])
        # else:
        #     print("레이저 공격")
        # print_mat(board)
        attacker_time[attacker[0]][attacker[1]] = time+1 # 가장최근 공격 시간 업데이트
        # 포탑 부서짐
        # 포탑 정비 (+ 종료조건 확인)
        live_cnt = 0

        for i in range(N):
            for j in range(M):
                if board[i][j] > 0:
                    live_cnt += 1
                    if i == attacker[0] and j == attacker[1]:
                        continue
                    if (i,j) in attack_relevant:
                        continue
                    board[i][j] += 1
        # print("포탑 정비 후:", live_cnt)
        # print_mat(board)
        if live_cnt <= 1:
            break

    print(max([max(board[i]) for i in range(N)]))



main()
# for _ in range(2):
#     main()