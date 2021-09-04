input = 100
# fibo(100) -> fibo(99)...top down 방식
# fibo(1) -> fibo(2) ... bottom up 방식

# memo 라는 변수에 Fibo(1)과 Fibo(2) 값을 저장해놨습니다!
memo = {
    1: 1,
    2: 1
}

# 1. 만약 메모에 있으면 그 값을 바로 반환
# 2. 없으면 수식대로 구한 후 다시 메모에 기록
# ㅇ dp 기본 ㅜ원칙 - 반복되는 형태로 부분적으로 파생되는 부분이 있다면 dp를 그리고 메모이제이션을 사용한다.

def fibo_dynamic_programming(n, fibo_memo):
    if n in fibo_memo:
        return fibo_memo[n]

    nth_fibo = fibo_dynamic_programming(n - 1, fibo_memo) + fibo_dynamic_programming(n - 2, fibo_memo)
    fibo_memo[n] = nth_fibo

    return  nth_fibo


print(fibo_dynamic_programming(input, memo))
