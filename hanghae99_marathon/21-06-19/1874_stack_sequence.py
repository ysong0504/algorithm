# # 작성일 : 21-06-19
# # 주제 : 스택
# # 난이도 : 중상
# # 담당자 : 윤송
#
# 백준 코드번호 : 1874
# url : https://www.acmicpc.net/problem/1874
# 문제명 : 스택 수열
# 문제설명 : 일렬의 


import sys
from collections import deque

n = int(sys.stdin.readline())

stack = deque()
result = list()
answer = ""
max_num = 0

for _ in range(n):
    num = int(sys.stdin.readline().rstrip())

    i = max_num + 1     
    # stack 에 숫자 추가
    while i <= num:
        stack.append(i)
        result.append('+')
        if i > max_num: # 이미 한번 추가된 숫자는 중복으로 쌓이지 않도록 확인해주는 변수
            max_num = i
        i += 1

    # i = 1
    # while i <= num:
    #     print(i)
    #     if i not in stack and i > used_num:         # used_num : 이전에 사용된 숫자를 중복으로 stack 에 넣지않기위한 비교용 변수
    #         stack.append(i)
    #         result.append('+')
    #         used_num = i
    #     i += 1
    # 만약 마지막 값이 입력된 숫자와 동일하다면 pop() 진행
    if num == stack[-1]:
        stack.pop()
        result.append('-')
    else:
        answer = 'NO'
        break
    # count += 1

if answer == 'NO':
    print('NO')
else:
    for i in result:
        print(i)














