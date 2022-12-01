n = int(input())
k = [int(i) for i in input().split(" ")]

if n == len(k):
    print(str(min(k))+" "+str(max(k)))