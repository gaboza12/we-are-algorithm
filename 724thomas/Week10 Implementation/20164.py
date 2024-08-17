# https://www.acmicpc.net/problem/20164

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


import sys

input = lambda: sys.stdin.readline().rstrip()

def solution(n):
    odds = {'1', '3', '5', '7', '9'}
    cmax = [0]
    cmin = [float('inf')]
    def count_odds(n):
        count = 0
        for c in str(n):
            if c in odds:
                count += 1
        return count

    def dfs(n, odd_n):
        if len(n) == 1:
            cmin[0] = min(cmin[0], odd_n)
            cmax[0] = max(cmax[0], odd_n)
        elif len(n) == 2:
            total = str(int(n[0]) + int(n[1]))
            dfs(total, odd_n + count_odds(total))
        else:
            for i in range(len(n)-2):
                for j in range(i+1, len(n)-1):
                    total = str(int(n[:i+1]) + int(n[i+1: j+1]) + int(n[j+1:]))
                    dfs(total, odd_n + count_odds(total))

    dfs(n, count_odds(n))
    return (cmin[0], cmax[0])

if __name__ == '__main__':
    print(*solution(input()))


