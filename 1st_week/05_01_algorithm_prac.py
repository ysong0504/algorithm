input = [0, 3, 5, 6, 1, 2, 4]

#곱하기와 더하기를 이용하여 최댓값 추출하기
#여기서 명심할 것! 무조건 곱하기가 좋은게 아니얌!!
# 0과 1은 더하는 게 낫다구!

def find_max_plus_or_multiply(array):
    sum = 1
    for element in array:
        #base case (1 또는 0일 시 + 진행)
        if element in (0, 1):
            sum += element
        else:
            sum *= element

    return sum


print("정답 = 728 현재 풀이 값 =", find_max_plus_or_multiply([0, 3, 5, 6, 1, 2, 4]))
print("정답 = 8820 현재 풀이 값 =", find_max_plus_or_multiply([3, 2, 1, 5, 9, 7, 4]))
print("정답 = 270 현재 풀이 값 =", find_max_plus_or_multiply([1, 1, 1, 3, 3, 2, 5]))
