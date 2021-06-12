input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26
    start_index = ord('a')

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - start_index
        alphabet_occurrence_array[arr_index] += 1

    max_num = alphabet_occurrence_array[0]
    for arr in alphabet_occurrence_array:
        if max_num < arr:
            max_num = arr

        arr_index =start_index - alphabet_occurrence_array[max_num]

    return chr(arr_index)


result = find_max_occurred_alphabet(input)
print(result)
