# 작성일 : 21-06-17
# 주제 : 함수
# 난이도 : 하
# 담당자 : 윤송

# 문제명 : 셀프 넘버
# 문제설명 : 양의 정수 n이 주어졌을 때, 이 수를 시작해서 n, d(n), d(d(n)), d(d(d(n))), ...과 같은 무한 수열을 만들 수 있다. 
# d(n) = sum(n의 각 자릿수) = m 이며
# n의 생성자는 m 일 때, 1 부터 10000까지 생성자가 없는 숫자를 출력하라.
# 백준 코드번호 : 4673


# 해결 방법
# # 1. 셀프 넘버를 True라고 할 때,
# # 2. 10000개의 True 배열을 임의로 생성한다. (10000 까지의 값을 출력해야함으로)
# # 3. 1부터 10000까지 모든 수를 루프를 돌려 d(n)으로 계산한다.
# # 4. 3에서 출력된 결과는 셀프넘버가 아니므로 2에서 생성한 배열에서 해당 인덱스는 False로 전환한다.
# # 5. True로 남아있는 배열의 인덱스를 순차적으로 출력한다. (인덱스값 = 셀프넘버)


self_number = [True] * 10000
self_number[0] = False      # 1로 시작하는 숫자와 인덱스를 동일하게 맞추기 위해서 0번째 인덱스는 None으로 처리한다.

for num in range(1, 10000):
    total = num + sum(map(int, str(num)))   # 숫자를 string형으로 변환하여 map을 통해 한 자릿수씩 쪼갠 후 int형으로 다시 바꿔 sum을 구한다.
    # print(total, num)
    if total < 10000:
        print(total, num)
        self_number[total] = False          # 생성자로 출력된 결과는 False

# for i in range(len(self_number)):
#     if self_number[i]:          # True 만 반환해준다.
#         print(i)


