# https://www.acmicpc.net/problem/2302

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


import sys
#sys.setrecursionlimit(1000000)
# input = sys.stdin.readline
input = lambda: sys.stdin.readline().rstrip()

def solution(n, m, arr):
    fixed = set(arr)
    arrs = []
    temp = []
    for i in range(1,n+1):
        if i not in fixed:
            temp.append(i)
        else:
            if temp:
                arrs.append(temp[:])
                temp = []
    if temp:
        arrs.append(temp[:])
    dp = [1,2,3,5,8]
    for i in range(5, n):
        dp.append(dp[i-1] + dp[i-2])
    ans = 1
    for arr in arrs:
        ans *= dp[len(arr)-1]
    return ans

if __name__ == '__main__':
    n = int(input())
    m = int(input())
    arr = []
    for _ in range(m):
        arr.append(int(input()))
    print(solution(n, m, arr))


'''
1
1

1 2
2 1
2

1 2 3
1 3 2
2 1 3
3

1 2 3 4
1 2 4 3
1 3 2 4
2 1 3 4
2 1 4 3
5

1 2 3 4 5
1 2 3 5 4
1 2 4 3 5
1 3 2 4 5 
1 3 2 5 4
2 1 3 4 5
2 1 3 5 4
2 1 4 3 5
8
'''