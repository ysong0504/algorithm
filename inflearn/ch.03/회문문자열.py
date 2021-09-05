# 작성일: 21.09.06
# 앞에서 읽을 때나 뒤에서 읽을 때나 같은 경우(회문 문자열)
# 이면 YES를 출력하고 회문 문자열이 아니면 NO를 출력하는 프로그램을 작성한다.

import sys
n = int(sys.stdin.readline())

for _ in range(n):
    result = 'YES'
    s = sys.stdin.readline().rstrip().upper()
    for i in range(len(s)):
        # print(s[i], s[-(i+1)])
        if(s[i] != s[-(i+1)]):
            result = 'NO'
            break;

    print(result)
