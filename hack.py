list = [x for x in range(0, 401)]
num = [ x for x in list if ((x % 3 == 0 and x % 5 == 0 and x % 2 !=0))]
print(num)
