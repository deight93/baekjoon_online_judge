import sys
from itertools import permutations

# p = 9999999
# eratos = [True] * (p + 1)
# eratos[0] = False
# eratos[1] = False
#
# for i in range(2, int((p**0.5+1))):
#     if eratos[i]:
#         j = 2
#         while (i * j) <= p:
#             eratos[i * j] = False
#             j += 1


def is_prime_num(n):
    for i in range(2, int((n**0.5) + 1)):
        if n % i == 0:
            return False
    return True


c = int(sys.stdin.readline().rstrip())

for _ in range(c):
    n = list(sys.stdin.readline().rstrip())
    paper = []
    for i in range(1, len(n)+1):
        paper += list(permutations(n, i))
    paper = set([int("".join(i)) for i in paper])
    paper.discard(0)
    paper.discard(1)

    cnt = 0
    for j in paper:
        if is_prime_num(j):
            cnt += 1
    print(cnt)


