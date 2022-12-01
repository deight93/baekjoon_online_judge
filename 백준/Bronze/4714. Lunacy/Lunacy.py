
import sys

while True:
    n = float(sys.stdin.readline().rstrip())
    if n < 0:
        break
    else:
        print("Objects weighing {:.2f} on Earth will weigh {:.2f} on the moon.".format(n, n*0.167))


