# https://www.acmicpc.net/problem/1744

'''
1. 아이디어 :
    1이상의 수를 갖고 있는 배열(A), 0이하의 수를 갖고 있는 배열(B)로 나눈다.
    A에서 큰 수 두개씩 뺴면서 결과값에 두 수의 합 또는 곱을 더한다
    B도 마찬가지
    마지막 A와 B의 값들을 더하거나 곱해서 답을 갱신
2. 시간복잡도 :
    O( nlogn )
3. 자료구조 :
    배열
'''

import sys

# sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def solution(n, pos, neg):
    pos.sort()
    neg.sort(reverse=True)

    ans = 0
    while len(pos) >= 2:
        val1 = pos.pop()
        val2 = pos.pop()
        if val1 * val2 >= val1+val2:
            ans += val1*val2
        else:
            ans += val1+val2
    while len(neg) >= 2:
        val1 = neg.pop()
        val2 = neg.pop()
        if val1 * val2 >= val1+val2:
            ans += val1*val2
        else:
            ans += val1+val2

    if pos and neg:
        val1 = pos.pop()
        val2 = neg.pop()
        if val1 * val2 >= val1+val2:
            ans += val1*val2
        else:
            ans += val1+val2
    elif pos:
        ans += pos.pop()
    elif neg:
        ans += neg.pop()
    return ans


n = int(input())
pos = []
neg = []
for _ in range(n):
    val = int(input())
    if val > 0:
        pos.append(val)
    else:
        neg.append(val)
print(solution(n, pos, neg))
