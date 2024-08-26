# https://www.acmicpc.net/problem/19539

'''
1. 아이디어 :
    나무들을 모두 2로 나누고 몫과 나머지를 각각 저장한다.
    그러면 나무들을 만들기 위해 필요한 2와 1이 나오는데,
    2와 1의 갯수를 2에서는 1차감, 1에서는 2 증가(또는 반대로) 했을때 1과 2가
2. 시간복잡도 :
    O( n )
3. 자료구조 :
    배열
'''

import sys

# sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def solution(n, arr):
    if sum(arr) % 3 != 0:
        return "NO"

    counter = [0, 0, 0]
    for i in range(len(arr)):
        counter[2] += arr[i] // 2
        counter[arr[i] % 2] += 1

    if counter[2] > counter[1]: #32, 5
        diff = counter[2] - counter[1]
        steps = diff // 3
        counter[2] -= steps
        counter[1] += steps * 2

    return "YES" if counter[1] == counter[2] else "NO"


n = int(input())
arr = list(map(int, input().strip().split()))
print(solution(n, arr))
