# 작성일 : 21-06-14
# 주제 : 1차원 배열
# 문제 : 주어진 학생의 전체 수와 각 학생들의 점수들을 합산하여 평균을 내리고, 그 평균이 넘는 학생들의 비율을 반올림하여 반환하라.
# 백준 코드번호 : 4344

# 배운점
# 1. 다중 input값을 받을 시 리스트에 넣어 for문으로 처리가 가능핟.
# 2. 배열 내 합계는 for문을 사용하지않더라도 sum으로 계산이 가능하다.
# sum은 숫자로만 이루어져 있는 iterable 자료형 (인덱스나 튜플처럼 인덱스 순환 접근이 가능한) 의 합계를 반환한다.
# 3. round는 소수점이 .0 일 시 길이 조절이 안되지만 f-string을 이용하면 가능하다.

# 1. 여러줄의 input값을 받을 때는 아래와 같이 list에 넣어주고
lists = int(input())

# 2. for문을 이용하여 한 줄씩 처리해준다.
for i in range(lists):
    input_value = list(map(int, input().split()))
    if len(input_value) > 1:
        student = input_value[0]
        scores = input_value[1:]
        student_count = 0

        # 평균 점수 구하기
        score_avg = sum(scores)/student  # 배열의 합은 sum으로 계산 가능하다.

        # 평균 이상인 학생 비율 구하기
        for score in scores:
            if score > score_avg:
                student_count += 1

        student_avg = student_count/student * 100

        # f-string을 이용하여 소수점 3자릿수까지 출력
        print("{:.3f}%".format(student_avg))






