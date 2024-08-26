# https://www.acmicpc.net/problem/2233

'''
1. 아이디어 :
    bin으로 트리와 각 노드의 입장, 퇴장을 저장한다.
    dfs로 공통 부모를 찾는다.
2. 시간복잡도 :
    O( n )
3. 자료구조 :
    해시맵, 해시셋, 배열
'''

import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

from collections import defaultdict


def solution(n, binary, rot):
    def make_edges(s):
        stack = [0]
        rot_node = set()
        c = 0
        for i in range(len(s)):
            if i in rot:
                rot_node.add(c)
            if s[i] == "0":
                c += 1
                stack.append(c)
                in_out[c][0] = i + 1
            else:
                val = stack.pop()
                children[stack[-1]].append(val)
                in_out[val][1] = i + 1
        return rot_node

    def dfs(node):
        count = 1 if node in rot_node else 0

        for child in children[node]:
            count += dfs(child)

        if count == 2:
            ans[0] = node
            return False
        elif count == 1:
            return True
        else:
            return False

    ans = [0]
    children = defaultdict(list)
    in_out = [[0, 0] for _ in range(n + 1)]
    rot_node = make_edges(binary)

    if len(rot_node) == 1:
        return in_out[list(rot_node)[0]]
    dfs(0)
    return in_out[ans[0]]


n = int(input())
binary = str(input().strip())
rot = list(map(int, input().strip().split()))
print(*solution(n, binary, rot))
