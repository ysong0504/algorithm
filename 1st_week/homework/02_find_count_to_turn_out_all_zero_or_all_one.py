input = "011010"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    new_arr = []
    start_num = 0
    #0으로 뒤집기

    count = 0

    #1 -> 0으로 변환
    for index in range(len(string)):
        if string[index] == 0:
            new_arr.append(char)

        else:
            for char in range(index, len(string)):
                new_arr.append('0')

                if char == 0:
                    count += 1
                    continue

    return count


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)

