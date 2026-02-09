from collections import deque

def solution(bridge_length, weight, truck_weights):
    wait_queue = deque([[0, weight] for weight in truck_weights])
    ing_queue = deque()
    end_queue = deque()

    cnt = 0
    while wait_queue or ing_queue:
        cnt += 1

        if wait_queue and weight >= wait_queue[0][1] + sum([ing[1] for ing in ing_queue]):
            ing_queue.append(wait_queue.popleft())

        for i in range(len(ing_queue)):
            ing_queue[i][0] += 1

        if ing_queue[0][0] == bridge_length:
            end_queue.append(ing_queue.popleft())
    return cnt + 1