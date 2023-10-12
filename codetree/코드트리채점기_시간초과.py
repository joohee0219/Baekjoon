# 코드트리 채점기
# 23 상 오후 2번

import sys
from collections import defaultdict
sys.stdin = open("./코드트리채점기.txt", "r")


def main():
    Q = int(sys.stdin.readline())
    _, N, u0 = sys.stdin.readline().split()  # 채점기 개수, 초기 url
    N = int(N)
    # 채점기 준비
    waiting_q = []  # p순(그다음t순)으로 항상 정렬하기. [p,t,u].
    judging = [[-1] for _ in range(N+1)]  # 인덱스 jid. [start, domain, 문제번호]. -1이면 쉬는중
    history = defaultdict(list)  # key: domain; val: [start, s+3(e-s)]
    waiting_q.append([1, 0, u0])
    next_jid = 1  # 쉬고 있는 가장 작은 번호의 채점기

    orders = [list(sys.stdin.readline().split()) for _ in range(Q-1)]

    def pick_task(curr_t):  # 현재 대기큐에 있는 문제 중 채점 가능하면서, 우선순위 가장 높은 문제 idx, domain 반환
        for i, (_, _, u) in enumerate(waiting_q):
            domain = u.split("/")[0]
            if domain in [task[0] for task in judging]:
                continue
            if (history[domain] and curr_t < history[domain][1]):
                continue
            return i, domain
        return -1, -1  # 채점 가능한 문제가 없는 경우

    for order in orders:
        # print(order)
        if order[0] == "200":  # 채점요청, t,p,u
            _, t, p, u = order
            t = int(t); p = int(p)
            # 만약 u와 같은 문제가 이미 있으면 추가x
            if u in [u for _, _, u in waiting_q]:
                continue
            waiting_q.append([p, t, u])
            waiting_q.sort(key=lambda x: [x[0], x[1]]) # 넣을때마다 정렬

        elif order[0] == "300":  # 채점시도 t
            t = int(order[1])
            # 채점 할 문제 고르기
            idx = -1
            domain = ""
            for i, (_, _, u) in enumerate(waiting_q):
                domain = u.split("/")[0]
                if domain in set([task[0] for task in judging]):
                    continue
                if history[domain] and t < history[domain][1]:
                    continue
                idx = i
                break

            if idx == -1:  # 채점 가능한 문제 없는 경우
                continue
            del waiting_q[idx]  # 대기큐에서 삭제
            # 비어 있는 가장 작은번호 채점기 찾기
            # for jid in range(1, N+1):
            #     if judging[jid][0] == -1:
            #         judging[jid] = [t, domain]
            #         break
            if next_jid <= N:
                judging[next_jid] = [t, domain]
                next_jid += 1
                while next_jid <= N and judging[next_jid][0] != -1:
                    next_jid += 1

        elif order[0] == "400":  # 채점종료 t, jid
            _, t, jid = order
            t = int(t); jid = int(jid)
            # t초에 Jid번 채점기의 채점이 종료됨
            if judging[jid][0] != -1:
                start, domain = judging[jid]
                judging[jid] = [-1]  # 채점기 상태 변환
                if jid < next_jid:
                    next_jid = jid
                if history[domain]:  # 채점기 히스토리 업데이트
                    if history[domain][0] < start:  # 방금 채점종료된 문제가 더 최근에 채점이 진행됨
                        history[domain] = [start, start + 3 * (t-start)]
                else:
                    history[domain] = [start, start + 3 * (t - start)]

        elif order[0] == "500":  # 조회
            t = int(order[1])
            print(len(waiting_q))

        # if order[0] != "500":
        #     print("t:",t,"대기큐:",waiting_q,"채점기:", judging, "기록:", history)

main()
