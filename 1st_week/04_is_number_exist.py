input = [3, 5, 6, 1, 2, 4]


def is_number_exist(number, array):
    for element in array:           # N 만큼
        if element == number:       # 1만큼 비교연산 실행
            return True             # N * 1

    return False

    # if number in array:
    #     return True


result = is_number_exist(3, input)
print(result)