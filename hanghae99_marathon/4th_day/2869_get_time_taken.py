# 작성일 : 21-06-17
# 주제 : 기본 수학 1
# 난이도 : 하

# 문제명 : 달팽이는 올라가고 싶다.
# 문제설명 : 달팽이는 낮에 A미터 올라가고 밤 동안 B미터 미끄러진다. 달팽이가 올라가야하는 나무의 높이가 V 라면
#           나무에 도착할 때까지 총 걸리는 시간은?
# 백준 코드번호 : 2869

# 배운점
import math

up, down, height = map(int, input().split())

# up - down 은 하루에 총 올라가는 높이다.
# 달팽이가 정상에 올라간 후에는 no more down 이기 때문에 height 에 -down 을 해준다.
day = (height - down) / (up - down)
print(math.ceil(day))



############ 초반 풀이
# cur = 0
# count = 0
# while True:
#     cur += up   # 2 3 5
#     count += 1  # 1  2
#     if cur > height or cur == height:  # 1 2
#         break
#     cur -= down
#
# print(count)
