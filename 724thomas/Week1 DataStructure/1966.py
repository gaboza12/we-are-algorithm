# https://www.acmicpc.net/problem/1966

'''
1. 아이디어 :
    힙으로 가장 중요한 문서를 추적하고, 큐로 FIFO 구현
2. 시간복잡도 :
    O( nlogn + n!)
3. 자료구조 :
    힙, 큐
'''

from collections import deque
import heapq
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def solution(docs, target_idx, arr):
    count = 0
    importances = []
    queue = deque()


    for i in range(len(arr)):
        heapq.heappush(importances, -arr[i])
        if i == target_idx:
            queue.append((arr[i], True))
        else:
            queue.append((arr[i], False))

    while True:
        importance, is_target = queue[0]
        if importance == -importances[0]:
            queue.popleft()
            heapq.heappop(importances)
            count += 1
            if is_target:
                return count
        else:
            queue.append(queue.popleft())
    return count


for _ in range(int(input())):
    docs, target_idx = list(map(int, input().split()))
    arr = list(map(int, input().strip().split()))
    print(solution(docs, target_idx, arr))


