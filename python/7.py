def is_prime(n):
    if n%2 == 0:
        return False

    for x in xrange(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

def calc_prime_pos():
    prime_numbers = []
    i = 0
    answer = 0
    while True:
        if is_prime(i):
            prime_numbers.append(i)
            i += 1
            if len(prime_numbers) == 100001:
                return prime_numbers[100001]
                break

print(calc_prime_pos())
