c = int(input())
for i in range(c):
    input_list = [int(i) for i in input().split(" ")]
    avg = sum(input_list[1:])/len(input_list[1:])
    avg_l = [i for i in input_list[1:] if i > avg]
    print("{:.3f}%".format(round(len(avg_l)/len(input_list[1:])*100, 3)))