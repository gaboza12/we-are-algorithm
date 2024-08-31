# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''
import sys

input = lambda: sys.stdin.readline().rstrip()

def solution(n, m, arr):
    from collections import defaultdict

    shapes = defaultdict(list)

    # 막대 모양
    shapes[(0, 3)].append(([0, 0], [0, 1], [0, 2], [0, 3]))
    shapes[(3, 0)].append(([0, 0], [1, 0], [2, 0], [3, 0]))

    # 정사각형 모양
    shapes[(1, 1)].append(([0, 0], [0, 1], [1, 0], [1, 1]))

    # L 모양
    shapes[(2, 1)].append(([0, 0], [1, 0], [2, 0], [2, 1]))
    shapes[(2, 1)].append(([0, 1], [1, 1], [2, 1], [2, 0]))
    shapes[(1, 2)].append(([0, 0], [0, 1], [0, 2], [1, 2]))
    shapes[(1, 2)].append(([0, 0], [0, 1], [0, 2], [1, 0]))
    shapes[(2, 1)].append(([0, 0], [1, 0], [2, 0], [0, 1]))
    shapes[(1, 2)].append(([0, 0], [1, 0], [1, 1], [1, 2]))
    shapes[(1, 2)].append(([0, 2], [1, 0], [1, 1], [1, 2]))
    shapes[(2, 1)].append(([0, 0], [0, 1], [1, 1], [2, 1]))

    # S 모양
    shapes[(2, 1)].append(([0, 0], [1, 0], [1, 1], [2, 1]))
    shapes[(2, 1)].append(([0, 1], [1, 0], [1, 1], [2, 0]))
    shapes[(1, 2)].append(([0, 1], [0, 2], [1, 0], [1, 1]))
    shapes[(1, 2)].append(([0, 0], [0, 1], [1, 1], [1, 2]))

    # T 모양
    shapes[(1, 2)].append(([0, 0], [0, 1], [0, 2], [1, 1]))
    shapes[(2, 1)].append(([0, 1], [1, 0], [1, 1], [2, 1]))
    shapes[(1, 2)].append(([1, 0], [1, 1], [1, 2], [0, 1]))
    shapes[(2, 1)].append(([0, 0], [1, 0], [1, 1], [2, 0]))

    ans = 0
    for row in range(n):
        for col in range(m):
            for offset, shape in shapes.items():
                if row + offset[0] >= n or col + offset[1] >= m: continue
                for s in shape:
                    total = 0
                    for x, y in s:
                        total += arr[row + x][col + y]
                    ans = max(ans, total)
    return ans

if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = [tuple(map(int, input().split())) for _ in range(n)]
    print(solution(n, m, arr))


# n = int(input().rstrip())
#
# n, m = map(int, input().split())
# n, m = list(map(int, input().split()))
# a = [c for c in input().strip()]
#
# s = input().rstrip()

# arr = list(map(int, input().strip().split()))
# arr = tuple(map(int, input().split()))
# integer_list = [int(num) for num in input().split()]
# dp = [[0 for _ in range(n)] for _ in range(n)]
# dp = [[0 for j in range(n)] for i in range(n)]
# grid = [list(input().rstrip()) for _ in range(n)] # "aaa" "bbb"
# grid = list(list(map(int, input().split())) for _ in range(n)) # "0 0 0 0", "0 0 0 0"
