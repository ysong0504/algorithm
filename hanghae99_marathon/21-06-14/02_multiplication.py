# 작성일 : 21-06-14
# 229
# 문제 : 세 자릿수의 두개 값을 입력받아 곱할 때의 각 과정을 출력한다.
# 참고!!!!! 백준 입력 기준을 따라야한다. 예를 들어 다중값이더라도 한번에 입력하는 경우가 있고 두세번 나누어 입력하는 경우가 있으니 '예제 입력'을 잘 볼 것!!

num_1 = input()
num_2 = input()

num_1 = int(num_1)
num_2 = int(num_2)

# 마지막 자릿수
output_1 = num_1 * (num_2 % 10)
# 두번째 자릿수
output_2 = num_1 * int((num_2 / 10) % 10)
# 첫번재 자릿수
output_3 = num_1 * int((num_2 / 100) % 10)

print(output_1)
print(output_2)
print(output_3)
print(num_1 * num_2)







