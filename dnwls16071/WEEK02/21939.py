import sys, heapq
from collections import defaultdict, deque
input = sys.stdin.readline

N = int(input())
minH = []; maxH = []
proHash = defaultdict(list)
lvHash = defaultdict(int)
for _ in range(N):
    # P : 문제 번호, L : 난이도
    # 가장 어려운 문제 번호 출력을 위해 첫 번째에 난이도, 두 번째에 문제 번호
    P, L = map(int, input().split())
    heapq.heappush(minH, [L, P])
    heapq.heappush(maxH, [-L, -P])
    proHash[L].append(P)
    lvHash[P] = L

M = int(input())
for _ in range(M):
    commands = input().split()
    if commands[0] == "add":
        P = int(commands[1]); L = int(commands[2])
        heapq.heappush(minH, [L, P])
        heapq.heappush(maxH, [-L, -P])
        proHash[L].append(P)
        lvHash[P] = L
    # 문제를 추가 (+),  문제를 해결 (-)
    elif commands[0] == "solved":
        P = int(commands[1])                   # 문제 번호 P
        lv = lvHash[P]                         # 해당 문제 난이도
        del proHash[lv][proHash[lv].index(P)]  # 문제에서 lv에 해당하는 레벨 문제 중에서 P번 문제를 제거
        lvHash[P] = None
    elif commands[0] == "recommend":
        if commands[1] == "1":
            for lv in range(100, 0, -1):
                if len(proHash[lv]):
                    print(max(proHash[lv]))
                    break
        elif commands[1] == "-1":
            for lv in range(1, 101):
                if len(proHash[lv]):
                    print(min(proHash[lv]))
                    break