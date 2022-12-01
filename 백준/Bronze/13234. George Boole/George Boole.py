import sys

input_list = sys.stdin.readline().rstrip().split(" ")
input_set = sorted(list(set(input_list)))
if input_set[0] == "AND":
    if len(input_set) == 2:
        if input_set[1] == 'true':
            print('true')
        elif input_set[1] == 'false':
            print('false')
    else:
        print('false')
elif input_set[0] == "OR":
    if len(input_set) == 2:
        if input_set[1] == 'true':
            print('true')
        elif input_set[1] == 'false':
            print('false')
    else:
        print('true')

