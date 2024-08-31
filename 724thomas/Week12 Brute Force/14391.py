def solution(n, m, arr):
    def calc_sum():
        total = 0

        for row in range(n):
            row_total = 0
            for col in range(m):
                if checked[row][col]:
                    row_total = row_total * 10 + arr[row][col]
                else:
                    total += row_total
                    row_total = 0
            total += row_total

        for col in range(m):
            col_total = 0
            for row in range(n):
                if not checked[row][col]:
                    col_total = col_total * 10 + arr[row][col]
                else:
                    total += col_total
                    col_total = 0
            total += col_total
        return total

    def backtrack(row, col):
        if row == n:
            return calc_sum()
        if col == m:
            return backtrack(row+1, 0)

        checked[row][col] = True
        val1 = backtrack(row, col+1)
        checked[row][col] = False
        val2 = backtrack(row, col+1)
        return max(val1, val2)

    checked = [[False] * m for _ in range(n)]

    return backtrack(0, 0)

if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = [list(map(int, list(input().strip()))) for _ in range(n)]
    print(solution(n, m, arr))
