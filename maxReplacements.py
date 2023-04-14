from collections import deque

symbols = ['<<>>', '<>', '<><>', '>>', '<<>', '><><', '<<>>>>>>']
replacements = [0, 1, 2, 2, 2, 2, 3]
final_list = []

for i in range(0, len(symbols)):
    stack = deque()
    for j in symbols[i]:
        if j == '<':
            stack.append(j)
        if j == '>':
            if len(stack)!= 0:
                stack.pop()

            else:
                replacements[i] = replacements[i] - 1
                    
    if len(stack) == 0 and replacements[i] >= 0:
        final_list.append(1)

    else:
        final_list.append(0)
    
print(final_list)