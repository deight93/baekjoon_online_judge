def solution(prices):
    stack = []
    answer = [0 for _ in range(len(prices))]

    for idx, price in enumerate(prices):
        while stack and stack[-1][1] > price:
            b_idx, b_price = stack.pop()
            answer[b_idx] = idx - b_idx
        stack.append((idx, price))

    for i in stack:
        answer[i[0]] = len(prices) - (i[0] + 1)
    return answer