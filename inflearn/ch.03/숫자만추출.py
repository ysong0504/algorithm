# 작성일: 21.09.06
# 문자와 숫자가 섞여있는 문자열이 주어지면 그 중 숫자만 추출하여 그 순서대로 자연수를 만
# 듭니다. 만들어진 자연수와 그 자연수의 약수 개수를 출력합니다.

# 1. 전체 문자열 중 re.sub()를 이용하여 숫자만 추출할 것이다.


import sys
import re
n = sys.stdin.readline().rstrip()

num = int(re.sub(r'[^0-9]','',n))


# 약수 출력
cnt = 0
for i in range(1, num+1):
    if (num % i == 0):
        cnt += 1

print(num)

