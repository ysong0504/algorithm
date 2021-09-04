from collections import deque


def is_correct_parenthesis(string):
    str_arr = deque()

    for char in string:
        str_arr.append(char)

    while len(str_arr) > 1:
        if str_arr[0] != str_arr[-1]:
            str_arr.pop()
            str_arr.popleft()
        else:
            break

    if len(str_arr):
        return False
    # 구현해보세요!
    return True


print("정답 = True / 현재 풀이 값 = ", is_correct_parenthesis("(())"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis(")"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())))"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("())()"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())"))