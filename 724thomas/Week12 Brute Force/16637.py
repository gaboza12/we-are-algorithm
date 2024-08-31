import sys

input = lambda: sys.stdin.readline().rstrip()

def solution(n, s):
    def calc(left, operator, right):
        if operator == "+":
            return left + right
        elif operator == "-":
            return left - right
        else:
            return left * right

    def backtrack(idx, current_value):
        # 수식 끝까지 도달한 경우
        if idx >= len(arr):
            ans[0] = max(ans[0], current_value)
            return

        # 괄호 없이 현재 연산자와 숫자를 사용하는 경우
        next_value = calc(current_value, arr[idx], arr[idx + 1])
        backtrack(idx + 2, next_value)

        # 괄호를 사용하여 다음 연산을 먼저 계산하는 경우 (중첩된 괄호를 방지)
        if idx + 2 < len(arr):
            bracket_value = calc(arr[idx + 1], arr[idx + 2], arr[idx + 3])
            next_value_with_bracket = calc(current_value, arr[idx], bracket_value)
            backtrack(idx + 4, next_value_with_bracket)

    arr = []
    for c in s:
        if c.isdigit():
            arr.append(int(c))
        else:
            arr.append(c)

    ans = [-float('inf')]
    backtrack(1, arr[0])  # 첫 번째 숫자부터 시작
    return ans[0]

if __name__ == '__main__':
    n = int(input())
    s = input().strip()
    print(solution(n, s))
