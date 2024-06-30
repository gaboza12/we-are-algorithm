# https://www.acmicpc.net/problem/17255

'''
1. 아이디어 :
    백트래킹으로 풀었다
2. 시간복잡도 :
    O( n * 2^n )
3. 자료구조 :
    배열
'''


import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def solution(n):
    ans = set()
    def backtrack(curr, left, right, path):
        if len(curr) == len(n):
            ans.add(tuple(path))
            return

        if left >= 0:
            backtrack(n[left] + curr, left-1, right, path + [n[left]+curr])
        if right < len(n):
            backtrack(curr + n[right], left, right+1, path + [curr+n[right]])

    for i in range(len(n)):
        backtrack(n[i], i-1, i+1, [n[i]])
    return len(ans)

n = str(input().strip())
print(solution(n))


