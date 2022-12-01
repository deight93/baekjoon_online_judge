import sys

n = int(sys.stdin.readline())
if n%2 == 1:
    a = sys.stdin.readline().rstrip().replace("1", "2").replace("0", "1").replace("2", "0")
else:
    a = sys.stdin.readline().rstrip()
b = sys.stdin.readline().rstrip()

if a == b:
    print("Deletion succeeded")
else:
    print("Deletion failed")