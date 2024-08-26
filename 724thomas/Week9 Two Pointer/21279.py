# https://www.acmicpc.net/problem/21279

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''
import sys
from collections import defaultdict

# input = sys.stdin.readline
input = lambda: sys.stdin.readline().rstrip()


def solution(n, k, arr):
    MAX_NUM = 100000
    minerals = defaultdict(list)

    for x, y, v in arr:  # y를 기준으로 저장
        minerals[y].append((x, v))

    # x별로 광물 값 저장
    colV = [0] * (MAX_NUM + 1)
    colC = [0] * (MAX_NUM + 1)

    sum_val = 0
    max_val = 0
    count = 0
    y = 0

    for x in range(MAX_NUM, -1, -1):  # x의 최대값부터 0까지 감소하면서 사각형 범위를
        while count < k and y <= MAX_NUM:  # count가 k보다 작고 y가 범위를 벗어나지 않는 동안 y 증가
            if y in minerals:  # y에 해당하는 광물이 있는경우
                for mx, mv in minerals[y]:  # x에 있는 광물들 중, 현재 x보다 작은 x값을 가진 광물들을 사각형에 포함
                    if mx <= x:
                        sum_val += mv
                        count += 1
                        colV[mx] += mv
                        colC[mx] += 1
            y += 1

        if count <= k:
            max_val = max(max_val, sum_val)

        if colC[x] != 0:  # x가 계속 줄어들기 때문에 현재 x가 포함된 광물들을 사각형에서 제외
            sum_val -= colV[x]
            count -= colC[x]

    return max_val


if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = [tuple(map(int, input().split())) for _ in range(n)]
    print(solution(n, m, arr))
