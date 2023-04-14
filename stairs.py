hopper = [1, -4, -1, -7 , 3]
steps = 1
sum = 0
for i in range(len(hopper)):
    sum = sum + hopper[i]
    while sum < 1:
        steps += 1
        sum += 1
print(steps)