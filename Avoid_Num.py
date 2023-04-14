steps = int(input("Enter the number of steps"))
avoidNum = int(input("Enter the number you want to avoid"))
sum = 0
j = 1
flag = 0

for inc in range(0, steps):
    sum = sum + j
    if sum == avoidNum:
        flag = 1
    j = j + 1
    
if flag == 1:
    sum = sum - 1
    print(sum)
