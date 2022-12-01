import sys

n = int(sys.stdin.readline())
input_list = [i for i in sys.stdin.readline().rstrip()]

if input_list.count('A') > input_list.count('B'):
    print("A")
elif input_list.count('A') == input_list.count('B'):
    print("Tie")
elif input_list.count('A') < input_list.count('B'):
    print("B")