import sys
import heapq

n = int(sys.stdin.readline())

heap = []
for _ in range(n):
    a = int(sys.stdin.readline().rstrip())
    heapq.heappush(heap, a)

    if a == 0:
        heapq.heappop(heap)
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap))