import sys


n = int(sys.stdin.readline())
for i in range(n):
    input_list = [int(i) for i in sys.stdin.readline().rstrip().split(" ")]
    n = input_list[0]
    m = input_list[1]

    cnt = 0
    for j in range(1, n):
        for k in range(j + 1, n):
            if (j**2+k**2+m) % (j*k) == 0:
                cnt += 1
    print(cnt)