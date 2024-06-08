# https://www.acmicpc.net/problem/2800

'''
1. 아이디어 :
    스택을 사용해서 pairs를 구하고, 백트래킹으로 모든 생성가능한 string를 만듬
2. 시간복잡도 :
    O ( n + 2**n )
3. 자료구조 :
    스택
'''

from collections import deque
import heapq
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def solution(s):
    ans = set()

    def find_pairs(s):
        pairs = {}
        stack = []
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                pairs[stack.pop()] = i
        return pairs

    pairs = find_pairs(s)

    def backtrack(idx, string, remove_set):
        if idx == len(s):
            ans.add(string)
            return

        if s[idx] == "(":
            remove_set.add(pairs[idx])
            backtrack(idx+1, string+s[idx], remove_set)
            remove_set.remove(pairs[idx])
            backtrack(idx+1, string, remove_set)

        elif s[idx] == ")":
            if idx not in remove_set:
                backtrack(idx+1, string, remove_set)
            elif idx in remove_set:
                backtrack(idx+1, string+s[idx], remove_set)

        else:
            backtrack(idx+1, string+s[idx], remove_set)


    backtrack(0, "", set())
    return sorted(ans)





s = input().strip()
ans = solution(s)[1:]
for a in ans:
    print(a)





