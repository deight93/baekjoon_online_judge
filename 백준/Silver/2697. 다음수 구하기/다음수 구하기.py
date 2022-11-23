
import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = [i for i in sys.stdin.readline().rstrip()]

    idx = 0
    for i in range(1, len(n)):
        if n[len(n)-i] > n[len(n)-i-1]:
            idx = len(n)-i
            break

    if idx == 0:
        print("BIGGEST")
    else:
        min_a = str(min([int(i) for i in n[idx:] if int(n[idx-1]) < int(i)]))
        temp = n[idx:]
        temp.remove(min_a)
        temp += [n[idx - 1]]
        n[idx - 1] = min_a

        print("".join(n[:idx] + sorted(temp)))