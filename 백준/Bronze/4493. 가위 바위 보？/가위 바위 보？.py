import sys

n = int(sys.stdin.readline())

a = {"0": ["RR", "PP", "SS"],
     "-1": ["RS", "SP", "PR"],
     "1": ["SR", "RP", "PS"]}

for i in range(n):
    input_list = [sys.stdin.readline().rstrip().replace(" ","") for j in range(int(sys.stdin.readline().rstrip()))]
    temp = []
    for j in input_list:
        for k, v in a.items():
            if j in v:
                temp += [int(k)]
                break
    temp_sum = sum(temp)

    if temp_sum > 0:
        print("Player 2")
    elif temp_sum == 0:
        print("TIE")
    elif temp_sum < 0:
        print("Player 1")