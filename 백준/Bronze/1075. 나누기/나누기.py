
import sys

n = sys.stdin.readline().rstrip()
f = int(sys.stdin.readline().rstrip())
temp_n = int(n[:-2]+"00")

if temp_n % f != 0:
    print(str((f * (temp_n // f)) + f)[-2:])
else:
    print(str(f * (temp_n // f))[-2:])