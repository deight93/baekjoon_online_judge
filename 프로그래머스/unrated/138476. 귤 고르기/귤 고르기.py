from collections import Counter

def solution(k, tangerine):
    counter = Counter(tangerine)
    counter.most_common(len(set(tangerine)))
    sort_dict = sorted(counter.items(), key=lambda x: x[1], reverse=True)

    answer = 0
    for j in sort_dict:
        k -= j[1]
        answer += 1
        if k <= 0:
            break

    return answer