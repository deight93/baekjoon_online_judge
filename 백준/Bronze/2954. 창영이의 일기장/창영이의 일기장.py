import sys

a = sys.stdin.readline().rstrip()
temp = ['apa', 'epe', 'ipi', 'opo', 'upu']

for i in temp:
    a = a.replace(i, i[0])

print(a)