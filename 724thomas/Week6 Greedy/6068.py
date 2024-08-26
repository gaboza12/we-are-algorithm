# https://www.acmicpc.net/problem/6068

'''
1. 아이디어 :
    끝내야 하는 시간을 기준으로 내림차순을 한다.
    일들을 순회하면서, 가장 늦게 끝내도 되는 일을 기준으로, 그 업무가 끝나기 위해 가장 늦게 시작되는 시간을 찾는다.
    가장 늦게 시작할 수 있는 시간보다 다음 일의 시간이 더 작으면, 그 일을 기준으로 한다.
    마지막 일을 시작할 수 있는 시간이 음수면 -1, 아니면 해당 시간을 출력
2. 시간복잡도 :
    O( nloogn )
3. 자료구조 :
    배열
'''

import sys

# sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def solution(n, arr):
    arr = [(arr[i][1], arr[i][0]) for i in range(len(arr))]
    arr.sort(reverse=True)
    start = float('inf')
    for dead, dur in arr:
        start = min(start, dead)
        start -= dur

    return -1 if start < 0 else start


n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().strip().split())))
print(solution(n, arr))
