
import sys

temp = {"E": "I", "S": "N", "T": "F", "J": "P", "I": "E", "N": "S", "F": "T", "P": "J"}

mbti = sys.stdin.readline().rstrip()

r = ""
for i in mbti:
    r += temp[i]
print(r)


