array = [5, 3, 2, 1, 6, 8, 7, 4]


def merge_sort(array):
    if len(array) <= 1:
    #merge_sort를 통해 배열들이 반으로 쪼개지다 더 이상 쪼개질 게 없을 때 array를 리턴하여 merge함수가 실행되나..?
        return array
    mid_index = len(array) // 2
    left_array = merge_sort(array[:mid_index])
    right_array = merge_sort(array[mid_index:])
    return merge(left_array, right_array)


def merge(array1, array2):  #O(N)
    result = []
    array1_index = 0
    array2_index = 0
    print(array1, array2)
    while array1_index < len(array1) and array2_index < len(array2):
        if array1[array1_index] < array2[array2_index]:
            result.append(array1[array1_index])
            array1_index += 1
        else:
            result.append(array2[array2_index])
            array2_index += 1

    if array1_index == len(array1):
        while array2_index < len(array2):
            result.append(array2[array2_index])
            array2_index += 1

    if array2_index == len(array2):
        while array1_index < len(array1):
            result.append(array1[array1_index])
            array1_index += 1

    return result


print(merge_sort(array))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!