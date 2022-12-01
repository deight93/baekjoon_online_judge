import sys
import itertools

b_dict = {}
for i in range(5):
    temp = sys.stdin.readline().rstrip().split(" ")
    for k, j in enumerate(temp):
        b_dict[j] = {"x": i, "y": k, "check": 1}
input_list = list(itertools.chain.from_iterable([sys.stdin.readline().rstrip().split(" ") for _ in range(5)]))

n = 0
for i in input_list:
    n += 1
    b_dict[i]["check"] = 0

    h_c = [0, 0, 0, 0, 0]
    v_c = [0, 0, 0, 0, 0]
    d_c = [0, 0]
    for k, v in b_dict.items():
        if v["check"] == 0:
            h_c[v['x']] += 1
            v_c[v['y']] += 1
            if v['x'] == v['y']:
                d_c[0] += 1
            if v['x'] + v['y'] == 4:
                d_c[1] += 1
    if h_c.count(5) + v_c.count(5) + d_c.count(5) >= 3:
        break

print(n)