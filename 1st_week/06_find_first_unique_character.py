
def find_not_repeating_character(string):
    occurrence_arr = [0] * 26
    alphabet_arr = [0] * 26
    index = 0                               #3

    for char in string:                     #N
        if char not in alphabet_arr:
            alphabet_arr[index] = char
            index += 1
        arr_index = alphabet_arr.index(char)
        occurrence_arr[arr_index] += 1

    for index in range(len(occurrence_arr)):        #N
        if occurrence_arr[index] == 1:
            return alphabet_arr[index]

    return "_"              #2N + n


print("정답 = d 현재 풀이 값 =", find_not_repeating_character("abadabac"))
print("정답 = c 현재 풀이 값 =", find_not_repeating_character("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", find_not_repeating_character("aaaaaaaa"))