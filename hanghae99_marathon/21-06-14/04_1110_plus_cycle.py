# 작성일 : 21-06-14
# 문제 : 주어진 수의 가장 오른쪽 자리 수와 주어진 수를 더해 가장 오른쪽 자리 수를 이어 붙이면 새로운 수를 만들 수 있다.
# 처음 주어진 수가 다시 나올 때까지 위 과정을 반복한 횟수를 반환하르아
# 백준 코드번호 : 1110

number = input()
origin_num = number
if len(number) < 2:
    origin_num = '0'+number
new_num = 0
count = 0

while count < 70:
    number = int(number)
    first_num = number // 10
    second_num = number % 10    #

    total_sum = first_num + second_num

    new_num = str(second_num) + str(total_sum % 10)
    count += 1
    if new_num == origin_num:
        break
    number = new_num

print(count)



