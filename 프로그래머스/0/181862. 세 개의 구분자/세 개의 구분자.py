import re

def solution(myStr):
    answer = re.split(r"[abc]+", myStr)
    answer = [v for v in answer if v]

    return answer or ["EMPTY"]