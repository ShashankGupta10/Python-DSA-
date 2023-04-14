list_given = [7, 8, 6, 5]
list_binary = [str(bin(x)) for x in list_given]
sorted_list = []
new_new_list = []

for i in list_binary:
    ones = i.count("1")
    sorted_list.append((ones, int(i, 2)))
    new_list = sorted(sorted_list)
    
for i in new_list:
    new_new_list.append(i[1])

print(new_new_list)