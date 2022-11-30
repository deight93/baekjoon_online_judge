import sys

c = sys.stdin.readline().rstrip()

print(int("0x"+c.lower(), 16))