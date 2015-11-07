def prime_factor(n):
    prime_numbers = []
    while n%2 == 0:
        prime_numbers.append(2)
        n = n/2
        print(prime_numbers)
    i = 3
    while n%i == 0:
        prime_numbers.append(i)
        n = n/i
        print(prime_numbers)

    return prime_numbers

print(prime_factor(600851475143))
