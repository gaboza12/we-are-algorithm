# https://www.acmicpc.net/problem/12919

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''

def solution(s1, s2):
    def dfs(curr):
        if curr == s1:
            return True
        if len(curr) < len(s1):
            return False

        if curr[-1] == "A":
            if dfs(curr[:-1]):
                return True
        if curr[0] == "B":
            if dfs(curr[1:][::-1]):
                return True

        return False

    return 1 if dfs(s2) else 0

if __name__ == '__main__':
    s1 = input().strip()
    s2 = input().strip()
    print(solution(s1, s2))

