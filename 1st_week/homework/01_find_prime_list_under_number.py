#prime = 소수 (1과 자기자신만 약수로 가지고있는 숫자)

input = 20


def find_prime_list_under_number(number):
    prime_number = []

    prime_number.append(2)
    prime_number.append(3)
    for num in range(number):
        if num % 2 != 0 and num % 3 != 0 and num > 1:
            prime_number.append(num)
    return(prime_number)


result = find_prime_list_under_number(input)
print(result)