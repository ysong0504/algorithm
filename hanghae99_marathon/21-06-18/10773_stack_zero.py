# 작성일 : 21-06-18
# 주제 : 스택
# 난이도 : 하

# 문제명 : 제로
# 문제설명 : 0 입력값이 들어올 때마다 가장 마지막에 입력한 값을 삭제한다.
# 백준 코드번호 : 10773
# url : https://www.acmicpc.net/problem/10773


n = int(input())
arr = []
for _ in range(n):
    num = int(input())
    if num == 0:
        arr.pop()
    else:
        arr.append(num)

print(sum(arr))
