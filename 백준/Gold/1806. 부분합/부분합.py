import sys

n, s = map(int, sys.stdin.readline().rstrip().split(" "))
seq = tuple(map(int, sys.stdin.readline().rstrip().split(" ")))
left_idx = 0
right_idx = 0
r = 0
min_len = len(seq)+1

while True:
    if r >= s:
        min_len = min(min_len, right_idx - left_idx)
        r -= seq[left_idx]
        left_idx += 1
    elif right_idx == n:
        break
    else:
        r += seq[right_idx]
        right_idx += 1

if min_len == len(seq)+1:
    print(0)
else:
    print(min_len)
