def solution(participant, completion):
    counter = {}

    for p in participant:
        counter[p] = counter.get(p, 0) + 1

    for c in completion:
        counter[c] -= 1

    for k, v in counter.items():
        if v != 0:
            answer = [k]

    return answer.pop()