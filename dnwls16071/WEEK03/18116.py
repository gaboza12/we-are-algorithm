import sys
input = sys.stdin.readline


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        robot[x] += robot[y]
        robot[y] = 0
        parent[y] = x
    elif x > y:
        robot[y] += robot[x]
        robot[x] = 0
        parent[x] = y
    else:
        pass

N = int(input())
parent = [i for i in range(10**6+1)]
robot = [1 for _ in range(10**6+1)]
for _ in range(N):
    commands = list(map(str, input().split()))
    if commands[0] == "I":
        x, y = int(commands[1]), int(commands[2])
        union(x, y)
    elif commands[0] == "Q":
        print(robot[find(int(commands[1]))])