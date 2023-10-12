"""
코드트리 채점기
23 상 오후 2번
구현, priority qyeye
시간 초과 헬..
heapq
    - heappush O(logN)
    - heappop O(logN)
"""


import sys
from collections import defaultdict
import heapq
sys.stdin = open("./코드트리채점기.txt", "r")


def main():
    Q = int(sys.stdin.readline())
    _, N, u0 = sys.stdin.readline().split()  # 채점기 개수, 초기 url
    N = int(N)

    # 채점기 준비
    waiting_q = defaultdict(list)  # key: domain, value: heapq (원소: [p,요청시간t, id])
    num_task_waiting = 1
    resting_judger = [i for i in range(1,N+1)] # 채점기 번호 heapq
    judging = defaultdict(list) # key: jid, val:[start, domain] 채점 중인 task 정보 저장.
    # judging_domain = []
    domain_lock = defaultdict(int)
    # history = defaultdict(list) # key: domain, value: [start, s+3(e-s)]
    # 처음 입력값
    d, id = u0.split("/")
    heapq.heappush(waiting_q[d], [1,0,id])

    # 명령
    orders = [list(sys.stdin.readline().split()) for _ in range(Q - 1)]

    for order in orders:
        t = int(order[1])

        if order[0] == "200":  # 채점요청: O(한 도메인에 있는 태스크 수) + O(log D)
            p = int(order[2])
            domain, id = order[-1].split("/")
            if id in [i for _,_,i in list(waiting_q[domain])]:  # 같은 문제 있는지 확인
                continue
            heapq.heappush(waiting_q[domain], [p, t, id])
            num_task_waiting += 1

        elif order[0] == "300":  # 채점시도
            if len(resting_judger) == 0:  # 비는 채점기 없으면 무시
                continue
            cand = [] # [[p,요청시간t, id],domain]
            for key, val in waiting_q.items():  # 도메인 거르기
                if len(val) == 0: # 해당 도메인에 대해 채점 가능한 문제 없으면 스킵
                    continue
                if t < domain_lock[key]:
                    continue
                # if key in set([sd[1] for sd in judging.values() if len(sd) > 0]):
                #     continue
                '''
                시간초과 해결 포인트)
                이 부분을 채점에 들어가면 domain_lock을 inf로 걸어주는 것으로 대체함. 그러면 t < domain_lock[key]로 확인을 대신할 수 있음
                '''
                cand.append([heapq.heappop(val), key])
            # domain별 후보 정렬해서 task 고르기
            if cand:
                cand.sort(key = lambda x: [x[0]])
                for i in range(1, len(cand)):
                    heapq.heappush(waiting_q[cand[i][1]], cand[i][0])
                # 선택된 task 채점기에 배정
                jid = heapq.heappop(resting_judger)
                judging[jid] = [t, cand[0][1]]
                # judging_domain.append(d)
                domain_lock[cand[0][1]] = 1e7
                num_task_waiting -= 1

        elif order[0] == "400":  # 채점종료
            jid = int(order[-1])
            if len(judging[jid]) == 0:
                continue
            else:
                s, d = judging[jid]
                domain_lock[d] = s + 3*(t-s)
                judging[jid] = []
                heapq.heappush(resting_judger, jid)

        elif order[0] == "500": # 채점 조회
            print(num_task_waiting)

        # print("시간:", t, "대기큐:", waiting_q, "쉬는채점기:", resting_judger, "채점중:", judging, "기록:", domain_lock)

main()
