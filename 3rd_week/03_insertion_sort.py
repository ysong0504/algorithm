# 삽입 정렬
# 날짜 : 21-06-15

input = [4, 6, 2, 9, 1]


def insertion_sort(array):  # 0(N) but 버블과 선택 정렬과는 다르다. 왜냐 break가 있어 불필요한 스텝을 줄여줬더.
    n = len(array)
    for i in range(1, n):   # range를 1부터 시작하는 이유: 삽입정렬에서는 첫번째 숫자는 이미 정렬되었다는 전제하에 진행됌
        for j in range(i):  # 첫번째 인덱스을 찍은 후 마지막 인덱스에서 첫 인덱스로 이동
            if array[i - j - 1] > array[i - j]:    # 앞에 있는 인덱스가 뒤에 인덱스보다 '클' 시 변경
                array[i - j - 1], array[i - j] = array[i - j], array[i - j - 1]
            else: # 앞에 있는 인덱스가 뒤에 인덱스보다 작을 경우 인덱스 교환없이 해당 루프는 종료
                break




    return array


insertion_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!