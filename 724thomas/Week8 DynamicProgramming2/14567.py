# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''

import sys

# sys.setrecursionlimit(1000000)
# input = sys.stdin.readline
input = lambda: sys.stdin.readline().rstrip()

from collections import defaultdict, deque


def solution(n, m, arr):
    ans = [0] * n
    in_degree = [0] * n
    post = defaultdict(set)

    for u, v in arr:
        post[u].add(v)
        in_degree[v - 1] += 1

    queue = deque()
    for v in range(1, n + 1):
        if in_degree[v - 1] == 0:
            queue.append(v)
            ans[v - 1] = 1

    while queue:
        pre_subject = queue.popleft()

        for post_subject in post[pre_subject]:
            in_degree[post_subject - 1] -= 1
            if in_degree[post_subject - 1] == 0:
                ans[post_subject - 1] = ans[pre_subject - 1] + 1
                queue.append(post_subject)

    return ans


if __name__ == '__main__':
    n, m = list(map(int, input().strip().split()))
    arr = []
    for _ in range(m):
        arr.append(list(map(int, input().strip().split())))
    print(*solution(n, m, arr))
