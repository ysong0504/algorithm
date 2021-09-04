# 작성일 : 21-06-15
# 주제 : 기본 수학 1

# 문제 : Fly me to the Alpha Centauri
# 문제 : 내가 온 지점이 K광년이라면 다음 지점까지 K, K-1, K+1 만큼 이동할 수 있다. 목적지까지 도달하기 위해서 걸리는 이동횟수를 반환하라
# 난이도 : 중
# 백준 코드번호 : 1011

# 배운점

lists = int(input())

for i in range(lists):
    input_value = input().split()
    start_point = input_value[0]
    final_point = input_value[1]

    # 지점 갯수파악 후 마지막 정거장은 1 광년만 움직일 수 있도록 미리 빼놓는다.
    total_point = final_point - start_point - 1 # 3

    for index in range(total_point):
        start_point += index



