def solution(word):
    answer = 0
    alphabets = ["A", "E", "I", "O", "U"]
    for a in alphabets:
        answer += 1
        if a == word: return answer
        for b in alphabets:
            answer += 1
            if a+b == word: return answer
            for c in alphabets:
                answer += 1
                if a+b+c == word: return answer
                for d in alphabets:
                    answer += 1
                    if a+b+c+d == word: return answer
                    for e in alphabets:
                        answer += 1
                        if a+b+c+d+e == word: return answer
    return answer