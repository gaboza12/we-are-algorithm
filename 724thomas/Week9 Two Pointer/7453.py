# https://www.acmicpc.net/problem/7453

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''

n = int(input())
nums = [list(map(int, input().strip().split())) for _ in range(n)]
AB = []
CD = {}

for i in range(len(nums)):
    for j in range(len(nums)):
        AB.append(nums[i][0] + nums[j][1])
        temp = -(nums[i][2] + nums[j][3])
        CD[temp] = CD.get(temp, 0) + 1

ans = 0
for n in AB:
    ans += CD.get(n, 0)
print(ans)
