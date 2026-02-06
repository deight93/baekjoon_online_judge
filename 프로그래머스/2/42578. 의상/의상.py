import collections

def solution(clothes):
    counter = collections.Counter(c[1] for c in clothes)

    answer = 1
    for v in counter.values():
        answer *= (v+1)
    answer -= 1

    return answer