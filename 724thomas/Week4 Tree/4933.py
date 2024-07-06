# https://www.acmicpc.net/problem/4933

'''
1. 아이디어 :
    스택을 사용해서 PostOrder Traversal을 트리로 만든다.
    dfs를 통해서 Tree1의 왼쪽 == Tree2의 왼쪽 AND Tree2의 오른쪽 == Tree2의 오른쪽을 확인하고,
    Tree1의 왼쪽 == Tree2의 오른쪽 AND tree1의 오른쪽 == Tree2의 왼쪽을 확인한다.
2. 시간복잡도 :
    O(
3. 자료구조 :

'''


import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def solution(a, b):
    def to_tree(s):
        stack = []
        for w in s:
            if w == 'nil':
                stack.append(None)
            else:
                left = stack.pop()
                right = stack.pop()
                stack.append((w, left, right))
        return stack[0]

    def check(tree1, tree2):
        if tree1 is None and tree2 is None:
            return True
        if tree1 is None or tree2 is None:
            return False
        if tree1[0] != tree2[0]:
            return False

        return (check(tree1[1], tree2[1]) and check(tree1[2], tree2[2])) or (check(tree1[2], tree2[1]) and check(tree1[1], tree2[2]))

    return "true" if check(to_tree(a), to_tree(b)) else "false"

for _ in range(int(input())):
    a = list(map(str, input().split()))[:-1]
    b = list(map(str, input().split()))[:-1]
    print(solution(a, b))


