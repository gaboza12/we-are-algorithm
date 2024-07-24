# https://www.acmicpc.net/problem/9655

'''
1. 아이디어 :
    짝수면 "CY", 홀수면 "SK"가 이긴다
2. 시간복잡도 :
    O( 1 )
3. 자료구조 :
    -
'''

print("SK" if int(input()) % 2 else "CY")
