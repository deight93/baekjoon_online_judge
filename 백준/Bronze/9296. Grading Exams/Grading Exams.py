
import sys

n = int(sys.stdin.readline())


for i in range(n):
    char_len = int(sys.stdin.readline())
    seq1 = sys.stdin.readline().rstrip()
    seq2 = sys.stdin.readline().rstrip()

    count = sum(1 for a, b in zip(seq1, seq2) if a != b)
    print("Case {}: {}".format(i+1, count))

