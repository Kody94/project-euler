def diff_sumsquare(n):
    result_sum = 0
    result_square = 0
    tmp = 0
    for i in range(0, n):
        result_sum = result_sum + i*i
    for i in range(0, n):
        tmp = tmp + i
    result_square = tmp*tmp
    return result_square - result_sum

print(diff_sumsquare(101))
