# https://www.acmicpc.net/problem/

'''
1. 아이디어 :
    dfs로 풀 수 있다
2. 시간복잡도 :
    O( n )
3. 자료구조 :
    해시맵
'''

import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def solution(n, nodes):
    tree = [[-1, -1, -1] for x in range(n + 1)]
    for node, left_child, right_child in nodes:
        if left_child != -1:
            tree[node][1] = left_child
            tree[left_child][0] = node
        if right_child != -1:
            tree[node][2] = right_child
            tree[right_child][0] = node

    root = -1
    for i in range(1, n + 1):
        if tree[i][0] == -1:
            root = i
            break

    col = [1]
    level_min = {}
    level_max = {}

    def dfs(node, level):
        if node == -1:
            return

        dfs(tree[node][1], level + 1)

        if level not in level_min:
            level_min[level] = col[0]
        level_max[level] = col[0]
        col[0] += 1

        dfs(tree[node][2], level + 1)

    dfs(root, 1)

    max_width = 0
    best_level = 0
    for level in range(1, max(level_max.keys()) + 1):
        width = level_max[level] - level_min[level] + 1
        if width > max_width:
            max_width = width
            best_level = level

    return best_level, max_width

n = int(input())
nodes = []
for _ in range(n):
    nodes.append(list(map(int, input().strip().split())))
print(*solution(n, nodes))