import sys

n = int(sys.stdin.readline())
input_list = [sys.stdin.readline().rstrip() for _ in range(n)]
print("".join([tuple(set(i))[0] if len(set(i)) == 1 else "?" for i in list(zip(*input_list))]))