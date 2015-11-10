# def palin(x):
#    if int(str(x)[::-1]) == x:
#        for i in range(100,999):
#            if x%i == 0:
#                y = x/i
#                return y, i



# print(palin(9009))



# def palin():
#    palindromes = []
#    for i in range(100,20000000):
#        if int(str(i)[::-1]) == i:
#            palindromes.append(i)
#    for i in palindromes:
        

# print(palin())



def mult_palin():
    palindromes = []
    for i in range(100,999):
        for e in range(100,999):
            x = i * e
            if is_palindrome(x):
                palindromes.append(x)
    return max(palindromes)


def is_palindrome(n):
    return int(str(n)[::-1]) == n

print(mult_palin())

# preserved previous attempts so I can remember my thought process
