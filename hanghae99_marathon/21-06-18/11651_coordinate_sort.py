# 작성일 : 21-06-18
# 주제 : 정렬
# 난이도 : 중
# 담당자 : 윤송

# 문제명 : 좌표 정렬하기
# 문제설명 : 2차원 평면위에 점 N개가 주어진다. y 좌표가 증가하는 순으로, y 좌표가 동일할 시 x 좌표가 증가하는 순서로 정렬하라
# 백준 코드번호 : 11651
# url : https://www.acmicpc.net/problem/11651


# 해결 방법

import sys

n = int(input())
arr = list()
for _ in range(n):
    x, y = list(map(int, sys.stdin.readline().split()))     # x, y값을 받는다.
    arr.append([y,x])   # y 값을 기준으로 정렬할 수 있도록 배열에 y 값을 첫번째로 저장한다.
arr.sort()

for y, x in arr:
    print(x, y)         # y, x의 순서를 바꿔 좌표를 x,y로 출력한다.
