
import sys

while True:
    p = int(sys.stdin.readline().rstrip())
    if p == 0:
        break 
        
    if p <= 1000000:
        print(p)
    elif 1000000 < p <= 5000000:
        print(int(p*0.9))
    else:
        print(int(p*0.8))
