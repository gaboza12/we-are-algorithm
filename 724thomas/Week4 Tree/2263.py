# https://www.acmicpc.net/problem/2263

'''
1. 아이디어 :
    시간초가가 나서 인덱스 기반으로 풀었다
2. 시간복잡도 :
    O( n )
3. 자료구조 :
    해시맵, 배열
'''


import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def solution(n, inorder, postorder):
    inorder_index = {num: idx for idx, num in enumerate(inorder)}
    preorder_list = []

    def dfs(inorder_start, inorder_end, postorder_start, postorder_end):
        if inorder_start > inorder_end or postorder_start > postorder_end:
            return

        root_val = postorder[postorder_end]
        preorder_list.append(root_val)
        root_index = inorder_index[root_val]

        left_tree_size = root_index - inorder_start

        dfs(inorder_start, root_index - 1, postorder_start, postorder_start + left_tree_size - 1)
        dfs(root_index + 1, inorder_end, postorder_start + left_tree_size, postorder_end - 1)

    dfs(0, len(inorder) - 1, 0, len(postorder) - 1)
    return preorder_list

n = int(input().strip())
in_order = list(map(int, input().strip().split()))
post_order = list(map(int, input().strip().split()))
print(*solution(n, in_order, post_order))


