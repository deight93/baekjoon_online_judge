import sys

s = list(sys.stdin.readline().rstrip())
count = 0
alphabet = [0 for i in range(26)]

for i in range(len(s)):
    alphabet[ord(str(s[i])) - 97] += 1


def backtracking(l, p):
    global count
    
    if l == 0:
        count += 1
    for i in range(26):
        if alphabet[i] > 0 and i != p:
            alphabet[i] -= 1
            backtracking(l-1, i)
            alphabet[i] += 1
        else:
            pass


backtracking(len(s), -1)
print(count)