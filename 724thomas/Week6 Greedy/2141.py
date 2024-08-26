# https://www.acmicpc.net/problem/2141

'''
1. 아이디어 :
    누적합이 중앙값을 넘는 곳이 답
2. 시간복잡도 :
    O( n log n)
3. 자료구조 :
    -
'''

n = int(input())
villages = []

for _ in range(n):
    x, a = map(int, input().split())
    villages.append((x, a))

villages.sort()

total_population = sum(a for x, a in villages)

cumulative_population = 0
target = (total_population + 1) // 2
for x, a in villages:
    cumulative_population += a
    if cumulative_population >= target:
        print(x)
        exit()
