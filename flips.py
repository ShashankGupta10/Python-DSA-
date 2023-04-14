s = "00000000"
target = "11011001"
flip = 0
s_list = list(s)

for i in range(len(s)):
    if s_list[i] != target[i]:
        flip = flip + 1
        for j in range(i, len(s)):
            if s_list[j] == '0':
                s_list[j] = '1'
            else:
                s_list[j] = '0'

s = "".join(s_list)
print(flip)
