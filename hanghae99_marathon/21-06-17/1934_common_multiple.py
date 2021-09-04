# 작성일 : 21-06-17
# 주제 : 정수론 및 조합론
# 난이도 : 하

# 문제명 : 최소공배수
# 문제설명 : 주어진 숫자들의 최소 공배수 구하기
# 백준 코드번호 : 1934


count = int(input())
for _ in range(count):
    numbers = list(map(int, input().split()))
    numbers.sort()
    num1 = numbers[1]
    num2 = numbers[0]
    # 최대공약수 :
    remainder = 1

    while remainder != 0:
        remainder = num1 % num2
        num1 = num2
        num2 = remainder
    # 최소공배수(주어진 값1 // 최대공약수 * 주어진 값2 // 최대공약수 * 최대공약수) :
    result = num1 * (numbers[1] // num1) * (numbers[0] // num1)

    print(result)
