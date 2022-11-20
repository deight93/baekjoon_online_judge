import sys
import heapq

abs_heap = []
heap_dict = {}
n = int(sys.stdin.readline().rstrip())

for i in range(n):
    x = int(sys.stdin.readline().rstrip())
    if x != 0:
        heapq.heappush(abs_heap, abs(x))
        if abs(x) not in heap_dict.keys():
            heap_dict[abs(x)] = [x]
        else:
            heap_dict[abs(x)].append(x)
        heap_dict[abs(x)].sort()
    else:
        if len(abs_heap) == 0:
            print(0)
        else:
            temp_val = heapq.heappop(abs_heap)
            if len(heap_dict[temp_val]) != 0:
                print(heap_dict[temp_val][0])
                heap_dict[temp_val].pop(0)
            else:
                print(0)