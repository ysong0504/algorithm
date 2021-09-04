# 작성일 : 21-06-14
# 주제 : 문자열
# 난이도 : 하

# 문제 : 대소문자 상관없이 입력값에서 제일 많이 사용된 알파벳을 반환하셈
# 백준 코드번호 : 1157

# 배운점
#
# # 알파벳을 우선 소문자로 통일시킨다.
# input_text = input().upper()
#
# # 알파벳 사용 빈도수를 저장할 수 있는 배열을 만든다.
# occurrence_list = [0] * 26
# start_index = ord('A')
#
# # 문자가 사용된 횟수을 배열에 저장한다.
# for char in input_text:
#     index = ord(char) - start_index
#     # print(index)
#     occurrence_list[index] += 1
#
# # 중복된 횟수의 문자열 검사
# count = 0
# max_number = max(occurrence_list)
# for number in occurrence_list:
#     if number == max_number:
#         count += 1
#
# if count > 1:
#     print('?')
# else:
#     max_index = occurrence_list.index(max_number)
#     print(chr(start_index + max_index))



# # 알파벳을 우선 소문자로 통일시킨다. (다시 풀어보자)
input_text = input().upper()
c
# 알파벳 순으로 정렬
input_text = ''.join(sorted(input_text))
count = 0
max_used_char = ""
max_num = 0
prev_char = input_text[1]

for index in range(len(input_text)):
    cur_char = input_text[index]

    if cur_char != prev_char:
        print(cur_char, prev_char, count)
        # print(prev_char, count)
        if max_num < count:
            max_num = count
            max_used_char = prev_char
        elif max_num == count:
            "중복이구만"
            break
        count = 0
    prev_char = cur_char
    count += 1

# print(max_used_char)
