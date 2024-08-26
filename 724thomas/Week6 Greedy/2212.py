# https://www.acmicpc.net/problem/2212

'''
1. 아이디어 :
    차이를 정렬한다.
    가장 큰 m-1개의 차이를 선택하여 그룹으로 나눈다.
2. 시간복잡도 :
    O( nlogn )
3. 자료구조 :
    배열
'''


import sys
#sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def solution(n, m, arr):
    if m >= len(arr):
        return 0
    arr.sort()
    diff = sorted([arr[i+1] - arr[i] for i in range(len(arr)-1)])
    for _ in range(m-1):
        diff.pop()
    return sum(diff)

n = int(input())
m = int(input())
arr = list(map(int, input().strip().split()))
print(solution(n, m, arr))


