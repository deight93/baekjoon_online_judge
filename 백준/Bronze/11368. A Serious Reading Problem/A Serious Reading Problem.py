import sys


while True:
    cwlp = [int(i) for i in sys.stdin.readline().rstrip().split(" ")]
    if sum(cwlp) == 0:
        break
    else:
        print(cwlp[0]**(cwlp[1]*cwlp[2]*cwlp[3]))


