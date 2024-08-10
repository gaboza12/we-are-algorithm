# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''

import sys

# sys.setrecursionlimit(1000000)
# input = sys.stdin.readline
input = lambda: sys.stdin.readline().rstrip()

import re
def solution(s):
    '''
    <main>
        <div title="title_name_1">
            <p>paragraph 1</p>
            <p>paragraph 2 <i>Italic Tag</i> <br > </p>
            <p>paragraph 3 <b>Bold Tag</b> end.</p>
        </div>
        <div title="title_name_2">
            <p>paragraph 4</p>
            <p>paragraph 5 <i>Italic Tag 2</i> <br > end.</p>
        </div>
    </main>
    '''
    # main 태그 내부의 내용을 추출
    main_content = re.findall(r'<main>(.*?)</main>', s, re.DOTALL)[0]
    #print(main_content)
    #print()

    # div 태그의 제목과 내용을 추출
    div_list = re.findall(r'<div title="(.*?)">(.*?)</div>', main_content, re.DOTALL)
    #print(*div_list, sep='\n')
    # 추출된 내용 출력
    for title, paragraph in div_list:
        print('title :', title)
        # 각 p 태그의 내용을 추출
        p_list = re.findall(r'<p>(.*?)</p>', paragraph, re.DOTALL)
        for p in p_list:
            # 태그 제거 및 공백 정리
            p = re.sub(r'<.*?>', '', p)
            p = re.sub(r'\s+', ' ', p.strip())
            print(p)


if __name__ == '__main__':
    s = input().strip()
    #s = '<main><div title="title_name_1"><p>paragraph 1</p><p>paragraph 2 <i>Italic Tag</i> <br > </p><p>paragraph 3 <b>Bold Tag</b> end.</p></div><div title="title_name_2"><p>paragraph 4</p><p>paragraph 5 <i>Italic Tag 2</i> <br > end.</p></div></main>'
    solution(s)
