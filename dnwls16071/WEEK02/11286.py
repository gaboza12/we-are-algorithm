import heapq
import sys
input = sys.stdin.readline

heap = []
N = int(input().strip())
for _ in range(N):
    val = int(input().strip())
    if val != 0:
        heapq.heappush(heap, (abs(val), val))
    else:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])