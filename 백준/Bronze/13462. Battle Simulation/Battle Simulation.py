import sys
import re

monster_pattern = sys.stdin.readline().rstrip()
counters = re.sub('RBL|RLB|BRL|BLR|LRB|LBR', "C", monster_pattern)
counters = re.sub('R', "S", counters)
counters = re.sub('B', "K", counters)
counters = re.sub('L', "H", counters)
print(counters)

