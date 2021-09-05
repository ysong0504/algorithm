# # 작성일 : 21-09-05
# # 난이도 : 실버 4

#
# # 백준 코드번호 : 4673
# url: https://www.acmicpc.net/problem/4673
# # 문제명 : 셀프 넘버
# # 문제설명 :
# n 을 d(n)의 생성자라고 할 때, 생성자가 없는 숫자를 셀프넘버라고한다.
# d(n) 은 n과 n의 각 자리숫를 더한 숫자 ex. d(31) = 31 + 3 + 1 = 35
# 10000 보다 작은 셀프넘버를 구하라
# n, d(n), d(d(n)), ...

# 해결방법
# 1. 규칙을 찾기위해 1부터 20까지의 셀프넘버를 구해본다.
# 2. 첫번째 숫자는 1로 지정
# 10000 개의 배열 생성


number_list = set(range(1, 10001))
result = set()
for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    result.add(i)

ans = sorted(number_list - result)

for i in ans:
    print(i)

    


    


# for i in range(len(number_list)):
#     print(number_list[i],i)
#     # if (number_list[i] == False):
#     #     print(i)
