# 작성일 : 21-06-14

# 문제 : 두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오.


a,b = input().split()
a = int(a)
b = int(b)

print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)

# 백준 문제 제출은 처음이라.. 입력값 넣는 부분에서 많이 헤맸다..
# input() 메소드를 이용하고
# 다중 입력값 존재 시 split나 map등을 이용해서 넣은 후 분리해주면된다..