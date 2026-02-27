from collections import deque

def check_diff(word, begin):
    diff = 0
    for i in range(len(word)):
        if word[i] != begin[i]:
            diff += 1
    return diff == 1


def solution(begin, target, words):
    if target not in words:
        return 0

    visited = [False] * len(words)
    queue = deque()
    queue.append((begin, 0))
    while queue:
        node, step = queue.popleft()

        if node == target:
            return step

        for word in words:
            if check_diff(word, node) and not visited[words.index(word)]:
                queue.append((word, step + 1))
                visited[words.index(word)] = True
    return 0