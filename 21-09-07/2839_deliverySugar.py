# # 작성일 : 21-09-07
# # 난이도 : 브론즈 1
#
# # 백준 코드번호 :2839
# url: https://www.acmicpc.net/problem/2839
# # 문제명 : 설탕 배달
# # 문제설명 :
# 3kg과 5kg 단위로 설탕을 배달할 수 있다. N kg의 설탕을 배달해야할 때 최소한의 봉지 개수는 몇개인가?
# 만약 정확하게 3과 5로 나눌 수 없다면 -1를 출력한다.

# 해결방법
# 1. 1차적으로 5kg으로 나눈 후 나머지는 3kg으로 나눈다.


import sys
n = int(sys.stdin.readline())
cnt = 0
while n != 0:
    if n % 5 == 0:
        cnt = n / 5 + cnt  
        break 
    elif  n % 5 != 0 and n % 3 != 0 and n < 3: 
        cnt = -1
        break

    n -= 3  # 5의 배수가 될 때까지 계속 3을 빼준다.
    cnt += 1

print(int(cnt))