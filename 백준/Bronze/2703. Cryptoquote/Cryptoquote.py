
import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    c_m = sys.stdin.readline().rstrip()
    r_d = {" ": " "}
    for k, j in enumerate(sys.stdin.readline().rstrip()):
        r_d[chr(65+k)] = j

    temp = ""
    for i in c_m:
        temp += r_d[i]
    print(temp)