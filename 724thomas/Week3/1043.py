# https://www.acmicpc.net/problem/1043

'''
1. 아이디어 :
    union-find
    진실을 아는 사람들을 묶는다.
    파티에 참석한 사람들끼리 모두 묶는다.
    진실을 아는 사람들을 모두 truth 해시셋에 넣는다
    파티를 순회하면서 인원중 한명이라도 truth에 존재하면 카운트.
2. 시간복잡도 :
    O( n )
3. 자료구조 :
    해시셋, 배열
'''

import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def solution(n, m, told, parties):
    def find(x):
        if x != par[x]:
            par[x] = find(par[x])
        return par[x]

    def union(a, b):
        ra = find(a)
        rb = find(b)

        if ra != rb:
            par[rb] = ra

    par = [i for i in range(n + 1)]

    base = told[0] if told else None
    for person in told:
        union(base, person)
    for party in parties:
        if len(party) > 1:
            base = party[0]
            for person in party[1:]:
                union(base, person)

    truth = set(find(person) for person in told)

    count = m
    for party in parties:
        for person in party:
            if find(person) in truth:
                count -= 1
                break

    return count


n, m = list(map(int, input().split()))
told = list(map(int, input().split()))[1:]
parties = []
for _ in range(m):
    parties.append(list(map(int, input().split()))[1:])

print(solution(n, m, told, parties))
