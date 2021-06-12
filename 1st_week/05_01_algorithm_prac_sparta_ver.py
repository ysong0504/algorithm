input = [0, 3, 5, 6, 1, 2, 4]

#곱하기와 더하기를 이용하여 최댓값 추출하기
#여기서 명심할 것! 무조건 곱하기가 좋은게 아니얌!!
# 0과 1은 더하는 게 낫다구!

#시간복잡도: O(N) - 1차 배열 반복문

def find_max_plus_or_multiply(array):
    sum = 1
    for element in array:
        #소수점 등이 나올것을 대비해 비교 연산자가 좋다 , 합계도 고려해야함 (sum이 0인데 곱하면 으잉..)
        if element <= 1 or sum <= 1:
            sum += element
        else:
            sum *= element

    return sum


print("정답 = 728 현재 풀이 값 =", find_max_plus_or_multiply([0, 3, 5, 6, 1, 2, 4]))
print("정답 = 8820 현재 풀이 값 =", find_max_plus_or_multiply([3, 2, 1, 5, 9, 7, 4]))
print("정답 = 270 현재 풀이 값 =", find_max_plus_or_multiply([1, 1, 1, 3, 3, 2, 5]))
