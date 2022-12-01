a = [int(input()) for i in range(9)]

max_int = 0
idx = 0
max_idx = 0
for i in a:
    idx += 1
    if max_int < i:
        max_int = i
        max_idx = idx

print(max_int)
print(max_idx)