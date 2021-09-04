input = [4, 6, 2, 9, 1]


def selection_sort(array): #O(N^2) - 배열반복문 두번진행됐다.
    n = len(array)
    # 이 부분을 채워보세요!
    for i in range(n-1):   #-1를 함으로서 마지막에 남은 한개의 원소는 비교하지 않는다. 왜냐 그전에 이미 정렬이 마무리되었을 거니까!
        for j in range(n-i): # -i는 정렬이 끝난 애들은 다시 보기 않기 때무넹
            # 현재보고 있는 인덱스
            if array[i+j] < array[i]:
                array[i + j], array[i] = array[i], array[i + j]

    return array


print(selection_sort(input))
# print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!

