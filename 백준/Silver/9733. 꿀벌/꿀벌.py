temp = []
while True:
    try:
        temp += input().rstrip().split(" ")
    except EOFError:
        break

cnt = 0
for i in "Re,Pt,Cc,Ea,Tb,Cm,Ex".split(","):
    cnt += temp.count(i)
    print(i, temp.count(i), "{:.2f}".format(temp.count(i)/len(temp)))
print("Total {} {:.2f}".format(len(temp), len(temp)/len(temp)))
 

