import heapq

def solution(operations):

    min_heap = []
    max_heap = []
    visited = {}
    idx = 0
    for op in operations:
        if op[0] == "I":
            heapq.heappush(min_heap, (int(op[1:]), idx))
            heapq.heappush(max_heap, (-int(op[1:]), idx))
            visited[idx] = True
            idx += 1
        else:
            if not(any(visited.values())):
                continue

            if op.split(" ")[1] == "1":
                v, i = heapq.heappop(max_heap)
                visited[i] = False

                for m_h in min_heap:
                    if m_h[1] == i:
                        min_heap.remove(m_h)
            else:
                v, i = heapq.heappop(min_heap)
                visited[i] = False

                for m_h in max_heap:
                    if m_h[1] == i:
                        max_heap.remove(m_h)

    if any(visited.values()):
        values = [v for v, _ in min_heap]
        return [max(values), min(values)]
    else:
        return [0, 0]