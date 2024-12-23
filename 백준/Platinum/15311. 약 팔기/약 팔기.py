import sys

n = int(sys.stdin.readline().rstrip())
drugs = ["1" for i in range(1000)] + ["1000" for j in range(1000)]
print(len(drugs))
print(*drugs)