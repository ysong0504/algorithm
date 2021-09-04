# 작성일 : 21-06-15
# 주제 : 기본 수학 2
# 난이도 : 하

# 문제명 : 베르트랑 공준
# 문제설명 : 베르트랑 공준은 임의의 자연수 n에 대하여, n보다 크고, 2n보다 작거나 같은 소수는 적어도 하나 존재한다는 내용을 담고 있다.
#            주어지는 자연수 n 보다 크고 2n 보다 작거나 같은 소수의 개수를 구해랑
# 소수란, 1과 자기 자신으로만 나누어 떨어진 숫자
# 백준 코드번호 : 4948

# 배운점
# prime number , 약수 구하기
# p에라스토테네스의 체 이용

# 단순한 방법
# 1부터 주어진 숫자까지 아래 for문을 돌며 하나씩 약수를 체크해주는 것
# 주어진 숫자까지 진행되기 때문에 O(N)의 시간 복잡도를 가짐
# def get_prime(n):
#     n = int(n)
#     prime_num = []
#
#     for i in range(1, n+1):
#         if n % i == 0:
#             prime_num.append(i)
#     return prime_num

# 효율적인 풀이방법 (에라스토테네스의 체 이용)
# seive = 체
# def sieve(n):
#     #주어진 숫자에서 최대만큼 배열 생성
#     primes = [True] * n
#
#     m = int(n ** 0.5)   #n의 제곱근를 이용하여 작은 수들만으로도 소수을 판별하기
#     for i in range(2, m+1):
#         if primes[i]:
#             for j in range (i+i,n,i):
#                 primes[j] = False
#     return [i for i in range(2,n) if primes[i] == True]

def sieve(max_num, min_num):
    primes = [True] * max_num        # 주어진 숫자만큼 배열 생성 (우선은 임의로 True (=소수)로 저장)

    m = int(max_num ** 0.5)  # n의 제곱근를 이용하여 작은 수들만으로도 소수을 판별
    for i in range(2, m + 1): # 1과 2는 이미 소수이므로 3부터 주어진 숫자까지 소수 판별 시작
        if primes[i]:
            for j in range(i + i, max_num, i):  # i의 배수가 되는 값들은 False로 변경
                primes[j] = False
    return [i for i in range(min_num + 1, max_num) if primes[i] == True]    #소수들 중 매개변수로 전달한 max_num과 min_num 사이만 반환


while True:
    min_num = int(input())      #값 입력받기
    if min_num == 0:            # 0 일시 동작 스탑
        break
    max_num = min_num * 2 + 1
    prime_num = sieve(max_num, min_num)     # 앞서 정의한 함수로 소수 get
    print(prime_num)
    print(len(prime_num))               # 소수 개수 반환
