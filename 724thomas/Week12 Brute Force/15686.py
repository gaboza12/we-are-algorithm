from itertools import combinations

def solution(n, m, arr):
    chickens = []
    houses = []
    for row in range(n):
        for col in range(n):
            if arr[row][col] == 2:
                chickens.append((row, col))
            elif arr[row][col] == 1:
                houses.append((row, col))

    # 각 집에서 모든 치킨집까지의 거리를 미리 계산
    dist = []
    for hx, hy in houses:
        dist.append([abs(hx - cx) + abs(hy - cy) for cx, cy in chickens])
    print(*dist, sep='\n')

    # 치킨집의 m개 조합에 대해 최소 거리 계산
    ans = float('inf')
    for comb in combinations(range(len(chickens)), m):
        total = 0
        for d in dist:
            total += min([d[c] for c in comb])
        ans = min(ans, total)

    return ans

if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    print(solution(n, m, arr))
