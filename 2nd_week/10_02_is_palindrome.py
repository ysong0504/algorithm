input = "소주만병만주소"


def is_palindrome(string):
    #문자열이 1보다 작을 시 함수 종료
    if len(string) < 1:
        return True

    if string[0] != string[-1]:
        return False

    return is_palindrome(string[1:-1])




print(is_palindrome(input))