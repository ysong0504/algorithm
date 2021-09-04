# # 작성일 : 21-09-05
# # 난이도 : 브론즈 3

#
# # 백준 코드번호 : 10818
# url: https://www.acmicpc.net/problem/10818
# # 문제명 : 최소, 최대
# # 문제설명 :
# 주어진 숫자의 최솟값과 최댓값 구하기
import sys

n = int(sys.stdin.readline())
m = list(map(int, sys.stdin.readline().split()))
print(min(m), max(m))
