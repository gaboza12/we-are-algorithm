# https://www.acmicpc.net/problem/2346

'''
1. 아이디어 :
    힙으로 가장 중요한 문서를 추적하고, 큐로 FIFO 구현
2. 시간복잡도 :
    O( nlogn + n!)
3. 자료구조 :
    힙, 큐
'''

from collections import deque
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def solution(n, arr):
    queue = deque()
    for i in range(len(arr)):
        queue.append((arr[i], i+1))
    ans = []

    while queue:
        val, idx = queue.popleft()
        ans.append(idx)
        if not queue:
            continue
        if val > 0:
            for i in range(val-1):
                queue.append(queue.popleft())
        else:
            for i in range(-val):
                queue.appendleft(queue.pop())
    return ans


n = int(input())
arr = list(map(int, input().strip().split()))
print(" ".join(map(str, solution(n, arr))))


