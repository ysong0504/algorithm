# 작성일 : 21-06-14
# 주제 : 문자열
# 난이도 : 하

# 문제 : 특수문자와 여러개의 알파벳이 하나의 문자로 이루어진 크로아티아 알파벳의 입력 개수를 구해라
# 백준 코드번호 : 2941

# 배운점
# 1. Replace. 바꾸고자하는 단어가 있을 시 단어들은 배열에 넣고 for문과 replace를 통해 변경가능하다.
# 2. 나는 두개이상의 문자를 하나로 취급하기위해서는 그 문자들을 따움표로 묶어줄 생각만 했었다.
#     하지만 따움표처리대신 다른 특수기호 (예를 들어 *)로 replace하면 하나로 취급된다는 것을 배웠다.
# 3. 또한 배열에 미리 단어들을 저장해 놓는 것은 하드코딩같아 지양하고 있었는데 이것또한 나의 편견임을 알았다.
#    무엇이든 간에 '적절히' 사용할 줄 알아야되겠다.

############################# 자료를 본 후 다시 짠 코드 ###################################
input_text = input()
words = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for letter in words:
    # 특정 알파벳을 * 대체함으로서 하나의 문자로 취급한다.
    input_text = input_text.replace(letter, '*')

print(len(input_text))








############################# 1차로 내가 짠 코드 ###################################
# input_text = input()
# alphabets_arr = []
#
# for i in range(len(input_text)):
#
#     if input_text[i] in ('=', '-'):
#         alphabets_arr.pop()
#
#         if input_text[i] == '=' and input_text[i - 2] == 'd':
#             alphabets_arr.pop()
#             alphabets_arr.append(input_text[i - 2:i + 1])
#         else:
#             alphabets_arr.append(input_text[i - 1:i + 1])
#
#     elif input_text[i] == 'j' and input_text[i - 1] in ('l', 'n'):
#         alphabets_arr.pop()
#         alphabets_arr.append(input_text[i - 1:i + 1])
#
#     else:
#         alphabets_arr.append(input_text[i])
#
# print(len(alphabets_arr))
