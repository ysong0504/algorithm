#factorial(N) = N * factorial(N-1)
# 예 factorial(4) = 4 * factorical(3)
#...
#factoral(1) = 1

def factorial(n):
    if n == 1:
        return 1
    # 이 부분을 채워보세요!
    return n * factorial(n-1)


print(factorial(5))
