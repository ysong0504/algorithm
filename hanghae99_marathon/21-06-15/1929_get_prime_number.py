


# # 에라스토테네스의 채를 이용한 소수 구하는 함수
# def get_prime(min_num, max_num):
#     primes = [True] * max_num  # 주어진 개수만큼 배열 생성 (임의로 전부다 프라임으로 취급한다.)
#     m = int(max_num ** 0.5)  # 제곱글응 이용하여 작은 수로 만든다.
#     for i in range(2, m + 1):  # 1과 2는 소수이니 그 다음 숫자부터 주어진 숫자까지 반복문을 돈다.
#         if primes[i]:
#             for j in range(i + i, max_num, i):  # i의 배수부터 주어진 숫자까지 i만큼 반복한다.
#                 primes[j] = False
#     return [i for i in range(min_num, max_num) if primes[i] == True]
#
#
# num1, num2 = map(int, input().split())
# for prime in get_prime(num1, num2+1):
#     if prime > 0:
#         print(prime)

m, n = map(int, input().split())
exp = set()
primes = []
for i in range(2, n+1):
    if i in exp:
        continue
    if i >= m:
        primes.append(i)
    j = 1
    while i * j <= n:
        exp.add(i*j)
        j+=1
print("\n".join(map(str, primes)))

