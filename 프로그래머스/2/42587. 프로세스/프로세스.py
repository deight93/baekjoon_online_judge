from collections import deque

def solution(priorities, location):
    queue = deque([(i, v) for i, v in enumerate(priorities)])

    cnt = 0
    while queue:
        i, v = queue.popleft()
        if not any(p > v for _, p in queue):
            cnt += 1
            if i == location:
                break
        else:
            queue.append((i, v))

    answer = cnt
    return answer