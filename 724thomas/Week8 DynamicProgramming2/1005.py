# https://www.acmicpc.net/problem/1005

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


import sys
#sys.setrecursionlimit(1000000)
# input = sys.stdin.readline
input = lambda: sys.stdin.readline().rstrip()

from collections import defaultdict, deque
def solution(structures, rules, times, dependencies, target):
    times = [0] + times  # 1-based 인덱싱을 위해 앞에 0 추가
    in_degree = [0] * (structures + 1)
    dp = [0] * (structures + 1)
    adj_list = defaultdict(list)

    for start, end in dependencies:
        adj_list[start].append(end)
        in_degree[end] += 1

    queue = deque()
    for i in range(1, structures + 1):
        if in_degree[i] == 0:
            queue.append(i)
            dp[i] = times[i]

    while queue:
        current = queue.popleft()
        for neighbor in adj_list[current]:
            in_degree[neighbor] -= 1
            dp[neighbor] = max(dp[neighbor], dp[current] + times[neighbor])
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return dp[target]


if __name__ == '__main__':
    for _ in range(int(input())):
        structures, rules = map(int, input().split())
        times = list(map(int, input().split()))
        dependencies = [tuple(map(int, input().split())) for _ in range(rules)]
        target = int(input())
        print(solution(structures, rules, times, dependencies, target))
