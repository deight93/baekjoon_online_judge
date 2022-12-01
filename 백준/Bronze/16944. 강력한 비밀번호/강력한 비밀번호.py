
import sys
import itertools as it
import string
from collections import Counter

n = int(sys.stdin.readline().rstrip())
s = sys.stdin.readline().rstrip()

classification_char_type = lambda c: 'lower' if c in string.ascii_lowercase else 'upper' \
    if c in string.ascii_uppercase else 'digit' if c in string.digits else 'special'

counter = Counter(list(iter(lambda s=iter(s): classification_char_type(next(s)), [])))

cnt = 0
if "upper" not in counter.keys():
    cnt += 1
if "digit" not in counter.keys():
    cnt += 1
if "special" not in counter.keys():
    cnt += 1
if "lower" not in counter.keys():
    cnt += 1

if n+cnt < 6:
    cnt += 6-(n+cnt)

print(cnt)

