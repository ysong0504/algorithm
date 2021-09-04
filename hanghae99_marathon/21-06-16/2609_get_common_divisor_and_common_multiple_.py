# 작성일 : 21-06-16
# 주제 : 정수론 및 조합론
# 난이도 : 하

# 문제명 : 최대공약수와 최소공백수
# 문제설명 : 주어진 숫자의 최대공약수와 최소공백수 출력
# 백준 코드번호 : 2609

# 1. 최대공약수 - 유클리드 호제법 사용

num_list = list(map(int, input().split()))
# 큰 순자가 나머지 진행 시 앞에 올 수 있도록 오름차순으로 정렬
num_list.sort()

num1 = num_list[1]
num2 = num_list[0]
remainder = 1

while remainder != 0:
    remainder = num1 % num2
    num1 = num2
    num2 = remainder

# num1 : 나머지가 0을 나누어지는 수
divisor = num1

# 2. 최대공배수
# - 최대공배수는 앞서 구한 최대공약수와 주어진 숫자들을 나눠 곱한여 구한다.
multiple = divisor * (num_list[1]/divisor) * (num_list[0]/divisor)

# 3. 결과 출력 sep='\n'를 사용하여 여러줄로 결과 출력
print(int(divisor), int(multiple), sep='\n')

