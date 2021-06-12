input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26
    start_index = ord('a')

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - start_index
        alphabet_occurrence_array[arr_index] += 1

    max_occurrence = 0
    max_alpha_index = 0
    for index in range(len(alphabet_occurrence_array)):
        alpha_occurrence = alphabet_occurrence_array[index]
        if alpha_occurrence > max_occurrence:
            max_occurrence = alpha_occurrence
            max_alpha_index = index

    max_num = start_index + max_alpha_index

    return chr(max_num)


result = find_max_occurred_alphabet(input)
print(result)
