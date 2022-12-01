def solution(elements):
    temp = []
    for i in range(1, len(elements) + 1):
        for j in range(len(elements)):
            if j + i <= len(elements):
                temp.append(sum(elements[j:j + i]))
            else:
                temp.append(sum(elements[j:j + i] + elements[:j + i - len(elements)]))

    return len(set(temp))

