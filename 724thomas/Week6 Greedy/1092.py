# https://www.acmicpc.net/problem/1092

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''

import sys
input = sys.stdin.readline

def solution(cranes, boxes):
    cranes.sort(reverse=True)
    boxes.sort(reverse=True)

    if boxes[0] > cranes[0]:
        return -1

    time = 0
    positions = [0] * len(cranes)
    checked = [False] * len(boxes)
    moved_boxes = 0

    while moved_boxes < len(boxes):

        for i in range(len(cranes)):
            while positions[i] < len(boxes):
                if not checked[positions[i]] and cranes[i] >= boxes[positions[i]]:
                    checked[positions[i]] = True
                    moved_boxes += 1
                    break
                print(checked)
                print(positions)
                positions[i] += 1
        time += 1

    return time


n = int(input())
cranes = list(map(int, input().strip().split()))
m = int(int(input()))
boxes = list(map(int, input().strip().split()))
print(solution(cranes, boxes))


