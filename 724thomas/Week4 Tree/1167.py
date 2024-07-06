# https://www.acmicpc.net/problem/

'''
1. 아이디어 :
    bfs를 두번 돌린다.
2. 시간복잡도 :
    O( n )
3. 자료구조 :
    해시맵, 해시셋
'''


import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

from collections import defaultdict, deque
def solution(n, graph):

    def bfs(curr):
        queue = deque()
        queue.append((curr,0))
        visited = set()
        visited.add(curr)
        fur = 0
        fur_dist = 0
        while queue:
            node, total = queue.popleft()
            if total > fur_dist:
                fur = node
                fur_dist = total

            for neighbor, distance in graph[node]:
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                queue.append((neighbor, total + distance))
        return fur, fur_dist

    fur, fur_dist = bfs(1)
    fur, fur_dist = bfs(fur)
    return fur_dist

graph = defaultdict(list)
n = int(input())
for _ in range(n):
    arr = list(map(int, input().strip().split()))
    for i in range(1, len(arr)-1, 2):
        neighbor = arr[i]
        distance = arr[i+1]
        graph[arr[0]].append((neighbor, distance))
print(solution(n, graph))


