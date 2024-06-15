# https://www.acmicpc.net/problem/21944

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :
'''


import sys
from bisect import bisect_left, bisect_right, insort

input = sys.stdin.readline

def solution(initial, commands):
    group_sorted = []  # 그룹별로 정렬된 리스트
    difficulty_sorted = []  # 난이도별로 정렬된 리스트
    groups = {}  # 문제 번호로 문제의 정보(난이도, 알고리즘 분류)를 저장

    def add_problem(p, l, g):
        groups[p] = (l, g)
        insort(group_sorted, (g, l, p))
        insort(difficulty_sorted, (l, p, g))

    def solve_problem(p):
        if p in groups:
            l, g = groups[p]
            groups.pop(p)
            idx = bisect_left(group_sorted, (g, l, p))
            if idx < len(group_sorted) and group_sorted[idx] == (g, l, p):
                group_sorted.pop(idx)
            idx = bisect_left(difficulty_sorted, (l, p, g))
            if idx < len(difficulty_sorted) and difficulty_sorted[idx] == (l, p, g):
                difficulty_sorted.pop(idx)

    def recommend(g, x):
        if x == 1:
            idx = bisect_right(group_sorted, (g, float('inf'), float('inf'))) - 1
            if idx >= 0 and group_sorted[idx][0] == g:
                return group_sorted[idx][2]
        else:
            idx = bisect_left(group_sorted, (g, 0, 0))
            if idx < len(group_sorted) and group_sorted[idx][0] == g:
                return group_sorted[idx][2]
        return -1

    def recommend2(x):
        if x == 1:
            if difficulty_sorted:
                return difficulty_sorted[-1][1]
        else:
            if difficulty_sorted:
                return difficulty_sorted[0][1]
        return -1

    def recommend3(x, L):
        if x == 1:
            idx = bisect_left(difficulty_sorted, (L, 0, 0))
            if idx < len(difficulty_sorted):
                return difficulty_sorted[idx][1]
            else:
                return -1
        else:
            idx = bisect_left(difficulty_sorted, (L, 0, 0)) - 1
            if idx >= 0:
                return difficulty_sorted[idx][1]
            else:
                return -1

    for P, L, G in initial:
        add_problem(P, L, G)

    result = []
    for command in commands:
        cmd = command[0]
        if cmd == 'add':
            add_problem(command[1], command[2], command[3])
        elif cmd == 'solved':
            solve_problem(command[1])
        elif cmd == 'recommend':
            result.append(recommend(command[1], command[2]))
        elif cmd == 'recommend2':
            result.append(recommend2(command[1]))
        elif cmd == 'recommend3':
            result.append(recommend3(command[1], command[2]))

    return result

initial = []
for _ in range(int(input())):
    initial.append(list(map(int, input().split())))
commands = []
for _ in range(int(input())):
    command = input().split()
    command[1:] = list(map(int, command[1:]))
    commands.append(command)

result = solution(initial, commands)
for r in result:
    print(r)
