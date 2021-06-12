def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26
    first_index = ord('a')

    # 이 부분을 채워보세요!
    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - first_index
        alphabet_occurrence_array[arr_index] += 1

    return alphabet_occurrence_array


print(find_alphabet_occurrence_array("hello my name is sparta"))
