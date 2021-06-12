finding_target = 14
finding_numbers = [1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16]

#선행 탐색 O(N) - 배열 크기만큼 다 돌기 때문에
#이진 탐색 O(logN) -

def is_existing_target_number_binary(target, array):
    start_index = 0
    end_index = len(array) - 1
    count = 0
    #나는 for문을 썼다. 어쨌든 range를 사용하면 무한루프까지는 아니니까 하지만 이 방법은 false일때를 고려하지 못한 반복문이다.
    # 만약 값이 존재하지 않을 시 루프는 숫자 개수만큼 돌것이다.
    # 하지만 while문으로 조건을 둘 시 없으면 바로 멈출수있게 효율적으로 만들 수 있따.
    while start_index <= end_index:
        mid_index = (start_index + end_index) // 2
        print(start_index, end_index)
        count += 1
        if array[mid_index] == target:
            return True
        elif array[mid_index] > target:
            end_index = mid_index - 1
            #왼쪽 탐색
        elif array[mid_index] < target:
            # 오른쪽 탐색
            start_index = mid_index + 1

    return False


    # 구현해보세요!



result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)
