
import sys

id = [sys.stdin.readline().rstrip() for _ in range(3)]
temp = {1:[[':::', ':o:', ':::']],
        2:[['::o', ':::', 'o::'], ['o::', ':::', '::o']],
        3:[['::o', ':o:', 'o::'], ['o::', ':o:', '::o']],
        4:[['o:o', ':::', 'o:o']],
        5:[['o:o', ':o:', 'o:o']],
        6:[['ooo', ':::', 'ooo'], ['o:o', 'o:o', 'o:o']]}

r = "unknown"
for k, v in temp.items():
    if id in v:
        r = k

print(r)
