# # 작성일 : 21-06-21
# # 주제 : 큐
# # 난이도 : 중상
# # 담당자 : 윤송
#
# # 백준 코드번호 : 1021
# url: https://www.acmicpc.net/problem/1021
# # 문제명 : 회전하는 큐
# # 문제설명 :지민이는 이 큐에서 다음과 같은 3가지 연산을 수행할 수 있다.
# 1. 첫 번째 원소를 뽑아낸다. 이 연산을 수행하면, 원래 큐의 원소가 a1, ..., ak이었던 것이 a2, ..., ak와 같이 된다.
# 2. 왼쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 a2, ..., ak, a1이 된다.
# 3. 오른쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 ak, a1, ..., ak-1이 된다.
# 큐의 크기, 뽑아내려는 수의 위치가 주어질 때 2와 3를 연산하는 최소 횟수를 구하라.
#
# # 해결 방법

# 해결 전 생각할 것
# 인덱스에 위치에 따라 원소가 오른쪽으로 이동할 지 왼쪽으로 이동할 지 결정

import sys
from collections import deque
size, num = map(int, sys.stdin.readline().split())
idx = list(map(int, sys.stdin.readline().split()))

# 입력값으로 주어진 사이즈에 맞춰 큐를 생성한다.
# (추출해야하는 인덱스을 큐에 담긴 숫자와 비교하며 진행)
queue = deque([i for i in range(1, size+1)])
count = 0

for i in idx:
    while True:
        # 뽑아내려는 인덱스와 현재 큐의 인덱스가 동일하다면 pop 진행
        if i == queue[0]:
            queue.popleft()
            break

        # 찾고자하는 인덱스의 위치가 중간 인덱스보다 작다면 앞 -> 뒤로 원소를 보내준다.
        if queue.index(i) <= len(queue) // 2:
            while i != queue[0]:
                queue.append(queue.popleft())
                count += 1

        # 찾고자하는 인덱스의 위치가 중간 인덱스보다 크다면 뒤 -> 앞으로 원소를 보내준다.
        else:
            while i != queue[0]:
                queue.appendleft(queue.pop())
                count += 1

print(count)





