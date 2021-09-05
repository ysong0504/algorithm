# # 작성일 : 21-09-05
# # 난이도 : 인프런 - 코드구현능력 기르기

# # 문제설명 :
# n과 k가 주어졌을 때 k번째로 작은 n의 약수를 구하라
# 만약 n 약수의 개수가 k 보다 작을 경우 -1를 출력한다.

# 해결방법
import sys

n,k = map(int, sys.stdin.readline().split())

i = 0 
result = 0
while i < n:
    i += 1
    if (n % i == 0 and k == i):
        print(i)
        break;
    
if (k < i):
    print(-1)
