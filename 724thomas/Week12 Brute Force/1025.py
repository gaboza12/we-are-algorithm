# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''

import sys

# sys.setrecursionlimit(1000000)
# input = sys.stdin.readline
input = lambda: sys.stdin.readline().rstrip()


def solution(n, m, arr):
    def is_sqr(s):
        s = int(s)
        return int(s ** 0.5) ** 2 == s

    def get_max(row, col):
        for inc_x in range(-n, n):
            for inc_y in range(-m, m):
                temp_num = ""
                x, y = row, col
                if inc_x == inc_y == 0: continue
                while 0 <= x < n and 0 <= y < m:
                    temp_num += arr[x][y]
                    if is_sqr(temp_num):
                        ans[0] = max(ans[0], int(temp_num))
                    x += inc_x
                    y += inc_y

    ans = [-1]
    for row in range(n):
        for col in range(m):
            get_max(row, col)
    return ans[0]


if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = [list(input().strip()) for _ in range(n)]
    print(solution(n, m, arr))
