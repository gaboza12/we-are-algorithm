# https://www.acmicpc.net/problem/8980

'''
1. 아이디어 :
    도착 마을을 기준으로 오른차순을 한다.
    free = 마을마다 실을 수 있는 박스의 수를 초기화한다.
    시작마을, 도착마을, 배송수를 순회하면서
    시작마을부터 도착마을까지 실을 수 있는 무게 (cmin)를 구하고,
    시작마을부터 도착마을까지 free 배열을 차감하고, 정답을 갱신한다.
2. 시간복잡도 :
    O( n ** 2 )
3. 자료구조 :
    배열
'''

import sys

# sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def solution(n, limit, towns, arr):
    arr.sort(key=lambda x: (x[1], x[0]))
    free = [limit] * (n + 1)
    ans = 0
    for start, end, weight in arr:
        cmin = min(free[start: end])
        for i in range(start, end):
            free[i] -= min(cmin, weight)
        ans += min(cmin, weight)

    return ans


n, limit = list(map(int, input().split()))
towns = int(input())
arr = []
for _ in range(towns):
    arr.append(list(map(int, input().split())))
print(solution(n, limit, towns, arr))
