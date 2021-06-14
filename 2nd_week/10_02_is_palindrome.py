# Recursive Function Example,
# make sure to add a code which prevent a infinite loop
# 재귀함수,
# 무한루프가 되지않도록 탈출 조건도 같이 명시하자

input = "소주만병만주소"


def is_palindrome(string):
    #문자열이 1보다 작을 시 함수 종료
    if len(string) < 1:
        return True

    if string[0] != string[-1]:
        return False

    return is_palindrome(string[1:-1])




print(is_palindrome(input)
