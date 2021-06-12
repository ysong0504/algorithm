input = "abcba"


def is_palindrome(string):
    last_index = len(string)-1
    for index in range(len(string)):
        #모범 답안
        if string[index] != string[last_index - index]:
            return False

        #내가 푼거
        # if string[index] != string[last_index]:
        #     return False
        # last_index -= 1

    return True


print(is_palindrome(input))