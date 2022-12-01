import sys

n = int(sys.stdin.readline())
input_list = [sys.stdin.readline().rstrip().upper() for _ in range(n)]

chr_list = [chr(i)for i in range(65, 91)]


for k, i in enumerate(input_list):
    temp = "".join(sorted(i)).replace(" ", "")
    temp = "".join([i for i in temp if ord(i) in range(65, 91)])

    chr_cnt = []
    ck = True
    for j in chr_list:
        if temp.count(j) == 0:
            print("Case {}: Not a pangram".format(k+1))
            ck = False
            break
        else:
            chr_cnt += [temp.count(j)]

    if ck is True:
        if min(chr_cnt) == 1:
            print("Case {}: Pangram!".format(k+1))
        elif min(chr_cnt) == 2:
            print("Case {}: Double pangram!!".format(k+1))
        elif min(chr_cnt) == 3:
            print("Case {}: Triple pangram!!!".format(k+1))
