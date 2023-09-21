# 연산자 끼워넣기
# =>완전 탐색
# 1. brute force
# 2. 백트래킹 (dfs)
import sys
from itertools import permutations

sys.stdin = open("testcase/14888.txt", "r")

min_res = 1e6 # sys.maxsize 
max_res = -1e6 # -sys.maxsize - 1

def main():
    global min_res, max_res
    N = int(sys.stdin.readline().strip())
    A = list(map(int, sys.stdin.readline().split(" ")))
    func = list(map(int, sys.stdin.readline().split(" "))) # + - x / : 0 1 2 3
    func_in_num = ""
    for i in range(4):
        for _ in range(func[i]):
            func_in_num += str(i)
    
    # 가능한 모든 연산자 조합
    perm = set(permutations(func_in_num, len(func_in_num)))

    def div(a, b):
        if a < 0 and b > 0:
            a *= -1
            return a // b * (-1)
        return a// b
    
    def calc_with_func(func):
        res = A[0]
        for i in range(N-1): # 연산자 배치할 수 있는 칸의 수: N-1
            if func[i] == 0:
                res += A[i+1]
            elif func[i] == 1:
                res -= A[i+1]
            elif func[i] == 2:
                res *= A[i+1]
            elif func[i] == 3:
                res = div(res, A[i+1])
        return res
            
    for p in perm:
        res = calc_with_func(list(map(int, p)))
        min_res = min(min_res, res)
        max_res = max(max_res, res)
    
    print(max_res)
    print(min_res)
    return (max_res, min_res)

def main2():
    N = int(sys.stdin.readline().strip())
    A = list(map(int, sys.stdin.readline().split(" ")))
    func = list(map(int, sys.stdin.readline().split(" "))) # + - x / : 0 1 2 3 

    def divide(a, b):
        if a < 0 and b > 0:
            a *= -1
            return a // b * (-1)
        return a // b
    
    def dfs(depth, res, plus, minus, mult, div):
        global max_res, min_res

        if depth == N-1:
            max_res = max(res, max_res)
            min_res = min(res, min_res)
            return

        if plus:
            dfs(depth+1, res + A[depth+1], plus-1, minus, mult, div)
        if minus:
            dfs(depth+1, res - A[depth+1], plus, minus-1, mult, div)
        if mult:
            dfs(depth+1, res * A[depth+1], plus, minus, mult-1, div)
        if div:
            dfs(depth+1, divide(res, A[depth+1]), plus, minus, mult, div-1)
    
    dfs(0, A[0], func[0], func[1], func[2], func[3])
    print(max_res)
    print(min_res)

# main()
main2()
