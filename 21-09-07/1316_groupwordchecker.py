# # 작성일 : 21-09-07
# # 난이도 : 실버 4
#
# # 백준 코드번호 :1316
# url: https://www.acmicpc.net/problem/1316
# # 문제명 : 그룹 단어 체커
# # 문제설명 :
# 그룹 단어란 동일한 문자가 일렬로 나타나는 경우를 말한다. 
# 주어진 단어들 중 그룹단어의 개수를 출력하라

# 해결방법
# 1. 알파벳을 확인 배열에 넣는다.
# 2. for문을 이용하여 만약 일렬된 글자가 아닌 상태에서, 
#   이미 중복된 글자가 배열에 있다면 단어 그룹이 아닌걸로 취급한다.

import sys
n = int(sys.stdin.readline())

for _ in range(n):
    arr = []
    s = sys.stdin.readline().rstrip()
    for i in range(len(s)):
        if s[i-1] != s[i] and s[i] in arr:  # 만약 현재 글자가 이전 글자와 다르지만 이미 배열에 존재한다면,
            n -= 1  # 그룹단어가 아니므로 전체 단어 수에서 1를 뺀다.
            break
        arr.append(s[i])    

print(n)
