# itertools 이용하지 않고 permutations & combinations 구현하기

from collections import deque

some_list = [1, 2, 3, 4]
N = len(some_list)
M = 3


def do_something(comb):
    print(comb)


# nCm
def comb_dfs(comb: deque, depth: int):
    if len(comb) == M: # m개 고르면 종료
        do_something(comb)
        return
    elif depth == N: # m개 고르기 전에 리스트 끝에 다다르면 그냥 종료
        return
    comb.append(some_list[depth]) # 새로운 원소 넣어주기
    comb_dfs(comb, depth + 1) # 새로운 원소 있는 상태로 재귀
    comb.pop() # 새로운 원소 빼기
    comb_dfs(comb, depth + 1) # 뺀 상태에서 재귀
    return

# nPm
visited = [0] * len(some_list)
result = []

def perm_dfs(perm: deque):
    if len(perm) == M:  # m개 고르면 종료
        result.append(list(perm))
        do_something(perm)
        return

    for i, val in enumerate(some_list):
        if visited[i]:  # 방문한 노드인 경우 제외
            continue
        perm.append(val)
        visited[i] = True
        perm_dfs(perm) # i번째 노드를 포함하여 재귀 호출
        perm.pop() # 원상복구
        visited[i] = False


print("조합")
comb_dfs(deque(), 0)
print("순열")
perm_dfs(deque())
print(len(result)) # 4*3*2 = 24