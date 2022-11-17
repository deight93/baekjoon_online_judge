import sys

n = int(sys.stdin.readline())
cases = {"a": 0}


def chase(n, q_list, n_q):
    if n_q in q_list:
        return

    for r, c in enumerate(q_list):
        h = len(q_list) - r
        if n_q == c + h or n_q == c - h:
            return

    q_list.append(n_q)
    if len(q_list) == n:
        cases["a"] += 1
        return

    for n_q in range(n):
        chase(n, q_list.copy(), n_q)


for n_q in range(n):
    q_list = []
    chase(n, q_list, n_q)

print(cases["a"])