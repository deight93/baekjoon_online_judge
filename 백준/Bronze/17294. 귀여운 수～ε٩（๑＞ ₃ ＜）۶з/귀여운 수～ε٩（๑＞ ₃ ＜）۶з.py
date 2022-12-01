import sys

temp = [int(i) for i in sys.stdin.readline().rstrip()]
ap = set([temp[i-1]-temp[i] for i in range(1, len(temp))])

if len(ap) <= 1:
    print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")
else:
    print("흥칫뿡!! <(￣ ﹌ ￣)>")

