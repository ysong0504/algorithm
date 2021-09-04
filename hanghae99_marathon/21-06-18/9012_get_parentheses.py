# 작성일 : 21-06-18
# 주제 : 스택
# 난이도 : 중

# 문제명 : 괄호
# 문제설명 : VPS
# 백준 코드번호 : 9012
import sys

n = int(input())
temp_arr = []
for _ in range(n):
    input_value = list(sys.stdin.readline().rstrip())

    for i in range(len(input_value)):
        print(input_value[i], 'test')
        if input_value[i] == "(":
            temp_arr.append(input_value[i])
            del input_value[i]
        else:
            continue

        print(input_value)
        print(temp_arr)


    # for i in temp_arr:
    #     for j in input_value:
    #         if j == ")":
    #             input_value.pop()
    #             break

    # if len(input_value) > 0:
    #     print('NO', input_value)
    # else:
    #     print('YES', input_value)

