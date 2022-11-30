
import sys
import itertools

s1, s2, s3 = map(int, sys.stdin.readline().rstrip().split(" "))

k = [sum(i) for i in itertools.product([i for i in range(1, s1+1)], [i for i in range(1, s2+1)],
                                       [i for i in range(1, s3+1)])]
k2 = [(i, k.count(i)) for i in set(k)]
print(max(k2, key=lambda x: x[1])[0])