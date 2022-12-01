import sys
import itertools

input_list = [str(i) for i in range(1, int(sys.stdin.readline().rstrip())+1)]
[print(" ".join(i)) for i in itertools.permutations(input_list)]