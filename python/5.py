def smallest_multiple():
    x = 1
    while True:
        if is_mult(x):
            return x
            break
        else:
            x += 1


def is_mult(n):
    if all(n % i == 0 for i in xrange(1,20)):
        return True

print(smallest_multiple())

# todo: optimize
