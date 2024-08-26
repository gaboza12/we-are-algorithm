import sys
input = sys.stdin.readline

def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    if a < b:
        parent[b] = a
        network[a] += network[b]
    else:
        parent[a] = b
        network[b] += network[a]

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

T = int(input())
for _ in range(T):
    F = int(input())
    parent = dict()
    network = dict()
    for _ in range(F):
        f1, f2 = input().split()
        if f1 not in parent:
            parent[f1] = f1
            network[f1] = 1
        if f2 not in parent:
            parent[f2] = f2
            network[f2] = 1
        union(f1, f2)
        print(network[find(f1)])