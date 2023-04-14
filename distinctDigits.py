low = int(input("Enter low"))
high = int(input("Enter high"))

distinct = [x for x in range(low, high + 1) if len(set(str(x))) == len(str((x)))]
print(len(distinct))