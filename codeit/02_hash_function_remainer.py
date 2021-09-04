def hash_fucntion_remainder (key, array_size):
    # 나누기 몫을 이용하여 key를 0 ~ array_size ~ 1 범위의 자연수로 바꿔주는 함수
    return key % array_size

print(hash_fucntion_remainder(2509, 40))