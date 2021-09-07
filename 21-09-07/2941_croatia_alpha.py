# # 작성일 : 21-09-07
# # 난이도 : 실버 4
#
# # 백준 코드번호 : 2941
# url: https://www.acmicpc.net/problem/2941
# # 문제명 : 크로아티아 알파벳
# # 문제설명 :
# 주어진 글자를 크로아티아 알파벳으로 변환 한 후 총 몇개의 알파벳이 쓰였는지 출력해라

# 해결방법
# 1. 변환 기준을 배열로 저장
# 2. 받은 문자열에 크로아티아 문자가 있는지 확인 후 하나의 글자로 변경
# 3. 전체 글자 길이 출력


import sys
import re

arr = ['c=','c-','dz=','d-','lj','nj','s=','z=']
# s = sys.stdin.readline().rstrip()
s = input()
cnt = 0
for i in arr:
    s = s.replace(i,"_")
    # s = re.sub(i,"_",s)

print(len(s))





