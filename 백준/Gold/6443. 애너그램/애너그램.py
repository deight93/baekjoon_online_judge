
import sys


def permutations(len_s, n, k):
    global visited
    global s
    global arr
    if len_s == k:
        sys.stdout.write("".join(arr) + "\n")
        return
    for a in visited:
        if visited[a]:
            visited[a] -= 1
            arr[len_s] = a
            permutations(len_s + 1, n, k)
            visited[a] += 1


n = int(sys.stdin.readline())
for _ in range(n):
    s = list(sys.stdin.readline().strip())
    s.sort()
    visited = {}
    for a in range(len(s)):
        if s[a] in visited:
            visited[s[a]] += 1
        else:
            visited[s[a]] = 1
    arr = [0] * len(s)
    permutations(0, len(s), len(s))