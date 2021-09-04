# numbers = [1, 1, 1, 1, 1]
numbers = [2, 3, 4]
#3이 가능한지 아닌지 역시 확인
target_number = 3


def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    count = 0
    result = 0

    for num in numbers:


    #만약 타겟변수와 연산자 결과가 같다면 카운트업!
    if target == result:
        count += 1

    # 구현해보세요!
    return count


print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))  # 5를 반환해야 합니다!