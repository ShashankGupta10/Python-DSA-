ids = [1, 2, 3, 2, 4, 3, 2, 5]
ids_count = []
m = 2
for i in range(0, m):
    for i in set(ids):
        ids_count.append(ids.count(i))

    min_count = min(ids_count)
    element_to_remove = None
    for i, element in enumerate(set(ids)):
        if ids.count(element) == min_count:
            element_to_remove = element
            break

    if element_to_remove is not None:
        ids.remove(element_to_remove)

print(list(set(ids)))