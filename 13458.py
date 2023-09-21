# 시험장
# 단순 계산, 구현..

import sys
import math

sys.stdin = open("13458.txt", "r")

def main():
    N = int(sys.stdin.readline()) # 시험장 개수
    students = list(map(int, sys.stdin.readline().split(" "))) # 각 시험장에 있는 응시자 수
    B, C = map(int, sys.stdin.readline().split(" ")) # 총감독, 부감독

    teacher = N # 각 시험장에 총감독관 1명씩 배치
    students_left = students[:]
    for i in range(N):
        students_left[i] = max(students_left[i] - B, 0)
    for i in range(N):
        teacher += math.ceil(students_left[i] / C)

    print(teacher)

main()



