arr_new = []
i = 1
input_number = 400000
while i < input_number:
    if input_number%i == 0:
        arr_new.append(input_number/i)
    i += 1

arr_new.sort(reverse=True)
print(arr_new[1])
