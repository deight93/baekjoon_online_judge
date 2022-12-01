import sys
n = [int(j) for j in sys.stdin.readline().rstrip().split(" ")]
n_len = abs(n[0]-n[1])+1

if n_len%2 == 0:
    k = (n[0] + n[1]) * (n_len//2)
else:
    k = (n[0] + n[1]) * (n_len//2) + int((n[0] + n[1])/2)
print(k)