import sys, heapq
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    Q = int(input())
    minH = []; maxH = []
    visited = [False] * Q
    for i in range(Q):
        commands = list(map(str, input().split()))
        if commands[0] == "I":
            heapq.heappush(minH, [int(commands[1]), i])
            heapq.heappush(maxH, [-int(commands[1]), i])
        else:
            if int(commands[1]) == 1:
                while maxH and visited[maxH[0][1]]:
                    heapq.heappop(maxH)            
                if maxH:
                    visited[maxH[0][1]] = True
                    heapq.heappop(maxH)
            else:
                while minH and visited[minH[0][1]]:
                    heapq.heappop(minH)
                if minH:
                    visited[minH[0][1]] = True
                    heapq.heappop(minH)

    while maxH and visited[maxH[0][1]]:
        heapq.heappop(maxH)
    while minH and visited[minH[0][1]]:
        heapq.heappop(minH)
    
    if not minH or not maxH:
        print("EMPTY")
    else:
        print(-maxH[0][0], minH[0][0])