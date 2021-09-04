# 작성일 : 21-06-14
# 문제 : 10000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 출력하는 프로그램을 작성하시오.
# 셀프 넘버란,  인도 수학자 D.R. Kaprekar가 붙인 이름으로 아래와 같은 숫자를 생성자라고 한다면 생성자가 없는 숫자
# 예) 33으로 시작한다면 다음 수는 33 + 3 + 3 = 39이고, 그 다음 수는 39 + 3 + 9 = 51, 다음 수는 51 + 5 + 1 = 57
# 백준 코드번호 : 4673

# 배운점


#셀프넘버는 11씩 올라간다.

i = 1
while i < 500:
    if i < 9:
        i += 2
    else:
        i += 11
    print(i)




# def self_number(number):
#     # if number > 10:
#     #     ""
#         # 홀수 반환..?
#
#     first_num = number // 10
#     second_num = number % 10
#     total_sum = first_num + second_num + number
#
#     print(total_sum)
#
#     # 숫자가 10000이하까지만 출력
#     if number > 100:
#         return ""
#
#     return self_number(total_sum)
#
#
# print(self_number(20))

