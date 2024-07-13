# https://www.acmicpc.net/problem/2138

'''
1. 아이디어 :
    0번쨰 스위치를 누른 경우와 누르지 않은 경우에서 시작한다.
    1번쨰 스위치부터 i-1번쨰 스위치와 같게 만들어준다.
2. 시간복잡도 :
    O( n )
3. 자료구조 :
    배열
'''

import sys

# sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def solution(n, start, e):
    def switch(state, index):
        for i in range(index - 1, index + 2):
            if 0 <= i < n:
                state[i] = 1 - state[i]

    s1 = start.copy()
    switch(s1,  0)
    count1 = 1 #0번째 스위치를 누른경우
    s2 = start
    count2 = 0

    for i in range(1, len(start)):
        if s1[i-1] != e[i-1]:
            count1 += 1
            switch(s1, i)
        if s2[i-1] != e[i-1]:
            count2 += 1
            switch(s2, i)
    if s1 == end and s2 == end:
        return min(count1, count2)
    elif s1 == end:
        return count1
    elif s2 == end:
        return count2
    else:
        return -1


n = int(input())
start = list(map(int, list(input().strip())))
end = list(map(int, list(input().strip())))
print(solution(n, start, end))
