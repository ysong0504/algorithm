def hash_fucntion_multiplication (key, array_size, a):
    temp = a * key  # a (0과 1사이의 자연수)와 key를 곱한다.
    temp = temp - int(temp) # 위에서 나온결과의 소숫점만 구한다.

    return int(array_size * temp) #소수점과 배열크기를 곱한 후 자연수만 반환한다.

print(hash_fucntion_multiplication(2509, 40, 0.6666))