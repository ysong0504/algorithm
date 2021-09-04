array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]


def merge(array1, array2):
    new_arr = []
    arr1_index = 0
    arr2_index = 0

    # 두개의 int 변수중 하나가 배열의 개수와 동일하다는 뜻은 배열 한개는 다 정리되었다는 뜻
    while arr1_index < len(array1) and arr2_index < len(array2):
        if array1[arr1_index] < array2[arr2_index]:
            # 만약 arr1 값이 더 작다면
            new_arr.append(array1[arr1_index])
            arr1_index += 1
        else:
            # 만약 arr2 값이 더 작다면
            new_arr.append(array2[arr2_index])
            arr2_index += 1

    if arr1_index == len(array1):
        while arr2_index < len(array2):
            new_arr.append(array2[arr2_index])
            arr2_index += 1
    return new_arr


print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!