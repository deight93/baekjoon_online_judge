import sys
import heapq

n = int(sys.stdin.readline())

heap = []
for _ in range(n):
    a = int(sys.stdin.readline().rstrip())
    heapq.heappush(heap, (-a, a))
    if a == 0:
        print(heapq.heappop(heap)[1])