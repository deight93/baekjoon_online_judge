def solution(rank, attendance):
    rank = [(v, i)for i, v in enumerate(rank)]
    a = sorted([i[0] for i in zip(rank, attendance) if i[1] == True])
    answer = a[0][1] * 10000 + a[1][1] * 100 + a[2][1]
    return answer