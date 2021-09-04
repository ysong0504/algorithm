# 작성일 : 21-06-14
# 문제 : 주어진 시간에서 45분을 뺀 시간을 출력한다.
# 백준 코드번호 : 2884

hour, minute = map(int, input().split())

# 45분보다 분이 크다면
if minute >= 45:
    print(hour, minute-45)
# 45분보다 분이 낮다면 15를 더해준다.
elif minute < 45:
    if hour == 0:
        hour = 24
    print(hour-1, minute+15)

