import sys
import itertools

while True:
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        break
    else:
        c_list = [sys.stdin.readline().rstrip() for _ in range(n)]
        if len(c_list)%2 == 0:
            c_list1 = c_list[:len(c_list) // 2]
            c_list2 = c_list[len(c_list) // 2:]
        else:
            c_list1 = c_list[:(len(c_list) // 2)+1]
            c_list2 = c_list[(len(c_list) // 2)+1:]

        for i in list(itertools.zip_longest(c_list1, c_list2)):
            for j in i:
                if j is not None:
                    print(j)
