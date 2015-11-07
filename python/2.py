x,y = 1,1
aggregate = 0

for i in range(0, 4000000):
    while x < 4000000:
        x,y = y,x+y
        if x%2 == 0:
            aggregate = aggregate + x
        i += 1
print(aggregate)
