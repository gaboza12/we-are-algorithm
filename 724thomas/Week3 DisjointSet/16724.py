# https://www.acmicpc.net/problem/16724

'''
1. 아이디어 :
    dfs를 사용한다.
    (0,0,1) - row, col, cycle 을 통해서, 사잌클이 존재하는지 찾는다.
    사이클이 존재하는지 확인하러 가는 길에다가 값을 1로 바꾼다.

    사이클이 존재하고, 다음 (1,1,2)를 통해서 사이클이 존재하는지 찾는다.
    똑같이 존재하는지 확인하러 가는 길에다가 값을 2로 바꾼다.
    만약 다른 사이클(값 1)과 만나게 되면 지금 찾고 있는 두번째 사이클은 1 사이클의 일부이므로 2 사이클로 표시를 하지 않는다.
    값을 -2로 표시할건데, 음수로 표시 된거는 2번쨰 사이클을 찾으려고 했지만 찾지 못했고, 이 방향으로 가게되면 다른 사이클과 만나게된다의 뜻이 된다.
    그러므로 음수를 만나게되면 불필요한 연산을 할 필요가 없어진다.
2. 시간복잡도 :
    O( n )
3. 자료구조 :
    배열
'''

import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def solution(n, m, graph):
    def dfs(row1, col1, cycle):
        if cycles[row1][col1] != 0:
            return cycles[row1][col1] == cycle

        cycles[row1][col1] = cycle
        row2, col2 = dirs[graph[row1][col1]]
        nrow, ncol = row1 + row2, col1 + col2

        if dfs(nrow, ncol, cycle):
            return True

        cycles[row1][col1] = -cycle
        return False

    dirs = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
    cycles = [[0 for _ in range(m)] for _ in range(n)]

    cycle = 0
    for row in range(n):
        for col in range(m):
            if cycles[row][col] == 0:
                if dfs(row, col, cycle + 1):
                    cycle += 1
            for c in cycles:
                print(c)
            print()
    return cycle


n, m = list(map(int, input().split()))
graph = []
for _ in range(n):
    graph.append([d for d in input().rstrip()])
print(solution(n, m, graph))

'''
3 4
DULL
DLLU
RRRU
'''