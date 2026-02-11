def solution(sizes):
    answer = 0
    sorted_sizes = [sorted(s) for s in sizes]
    max_w, max_h = 0, 0
    for w, h in sorted_sizes:
        max_w = max(max_w, w)
        max_h = max(max_h, h)
    answer += max_w * max_h
    return answer