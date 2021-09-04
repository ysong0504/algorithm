input = [4, 6, 2, 9, 1]

#O(N^2)
def bubble_sort(array): #O(N^2)
    n = len(array)
    # 배열 수만큼 돌며
    for i in range(n - 1):          #n의 길이만큼 반복
        for j in range(n - i - 1):  #n의 길이

            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]


bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!