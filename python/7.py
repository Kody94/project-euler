def is_prime(n):
    if n%2 == 0:
        return False

    for x in xrange(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

def calc_prime_pos(x):
    prime_numbers = []
    i = 0
    answer = 0
    while len(prime_numbers) < x:
        if is_prime(i):
            prime_numbers.append(i)
        i += 1
    return prime_numbers[len(prime_numbers) - 1]

print(calc_prime_pos(10001))
