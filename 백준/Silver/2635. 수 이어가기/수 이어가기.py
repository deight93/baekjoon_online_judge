import sys

n = int(sys.stdin.readline().rstrip())
s_n = int(n/2)

temp2 = []
for i in range(s_n, n+1):
    t_n = n
    t_sn = i
    temp = [t_n, t_sn]
    while True:
        t_tn = t_n - t_sn
        temp += [t_tn]
        if t_tn > t_sn:
            temp2 += [temp]
            break
        t_n = t_sn
        t_sn = t_tn


max_temp = max(temp2, key=lambda x:len(x))
print(len(max_temp))
print(" ".join([str(i) for i in max_temp]))


