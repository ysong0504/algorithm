# 첫 도착지
# 짝수: 1 -> 2
# 홀수: 1 -> 3

# 두번째 도착지

# 짝수: 1 -> 3
# 홀수: 1 -> 2

# 3번째 도착지
# 작은 아이가 두번째 아이에게 얹힌다. (마지막을 제외하고 다시 뭉친다.)

# 4번째
# 3번째로 큰 아이가 빈 곳으로 간다. 

# 5번째
# 작은 아이가 두번째 + 3번째 아이에게 얹힌다. (마지막을 제외하고 다시 뭉친다.)

import sys
n = int(sys.stdin.readline())
count = 0

# 매개변수 : 총 개수, 시작, 목표, other,...?
def hanoi(total, start, destination, other, count):
    # base Case - 남은 원반의 개수가 없을 시 종료한다.
    if total == 1:
        count += 1
        return
    print(start , '->' , destination)
    hanoi(total-1, start, other, destination)
    print(start ,'-->', destination)
    hanoi(total-1, other, destination, start)
    print(start, '--->', destination)




hanoi(n, 1, 3, 2, 0)