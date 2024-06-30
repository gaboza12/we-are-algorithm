# https://www.acmicpc.net/problem/5430

'''
1. 아이디어 :
    거지같은 문제
2. 시간복잡도 :
    O ( n )
3. 자료구조 :
    큐
'''

from collections import deque
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def solution(commands, queue):
    reversed = False

    for command in commands:
        if command == "R":
            reversed = not reversed
        elif command == "D":
            if not queue:
                return "error"
            if reversed:
                queue.pop()
            else:
                queue.popleft()

    if reversed:
        queue.reverse()

    return "[" + ",".join(queue) + "]"


pairs = []
for _ in range(int(input().strip())):
    commands = input().strip()
    n = int(input().strip())
    arr = input().strip()[1:-1]
    arr = deque(arr.split(",")) if arr else deque()
    print(solution(commands, arr))




