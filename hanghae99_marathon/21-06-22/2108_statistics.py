# # 작성일 : 21-06-21
# # 주제 : 정렬
# # 난이도 : 중
# # 담당자 : 윤송
#
# # 백준 코드번호 : 2108
# url: https://www.acmicpc.net/problem/2108
# # 문제명 : 통계학
# # 문제설명 :
# 수를 처리하는 것은 통계학에서 상당히 중요한 일이다. 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. 단, N은 홀수라고 가정하자.
# 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이
# N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.
#
# # 해결 방법

# 해결 전 생각할 것
import sys
from collections import Counter

result_arr = []
lists = []

n = int(sys.stdin.readline())
count_arr = [0] * n
for _ in range(n):
    num = int(sys.stdin.readline())
    lists.append(num)


# 1. 산술 평균 출력
result_arr.append(sum(lists) // n)

# 2. 중앙값 출력
lists.sort()
mid_index = len(lists) // 2
result_arr.append(lists[mid_index])

# 3. 최빈값 출력
cnt = Counter(lists)
count = 0
for k, v in cnt.most_common():
    print(k, v)
    if v > count:


# 4. 범위 출력
result_arr.append(max(lists) - min(lists))

# for i in result_arr:
#     print(i)
