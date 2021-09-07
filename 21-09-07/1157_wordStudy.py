# # 작성일 : 21-09-07
# # 난이도 : 브론즈 1

#
# # 백준 코드번호 : 1157
# url: https://www.acmicpc.net/problem/1157
# # 문제명 : 단어 공부
# # 문제설명 :
# 알파벳이 대소문자로 주어진다면 해당 단어에서 가장 많이 사용된 알파벳이 무엇인지 구하라
# 대소문자 구분 x
# 글자수가 모두 동일할 시 ? 출력

# 해결방법
# 0. 알파벳별 빈도수를 저장할 수 있는 배열 생성
# 1. 받는 단어를 대문자로 변경
# 2. for문을 이용하여 글자를 아스키로 변경
# 3. 배열에 빈도수 저장
# 4. 중복 빈도수 확인
# 5. 결과 출력

import sys
s = sys.stdin.readline().rstrip().upper()   # 대문자로 변경
alpha = 26*[0]
# A는 65 부터 시작
for i in s:
    m = ord(i) - 65     # 아스키코드로 변경
    alpha[m] = alpha[m] + 1 # 빈도수 체크

if (alpha.count(max(alpha)) > 1):   # 빈도수가 제일 많은 글자가 한개 이상 존재한다면 물음표 출력
    print("?")
else:
    print(chr(alpha.index(max(alpha)) + 65))    # 아스키 코드를 문자로 변환







