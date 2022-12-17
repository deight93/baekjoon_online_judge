import sys

w = sys.stdin.readline().rstrip().upper()

kangaroo = {}
for i in "KANGAROO".upper():
    if i in kangaroo.keys():
        kangaroo[i] += 1
    else:
        kangaroo[i] = 1

kiwi = {}
for i in "KIWIBIRD".upper():
    if i in kiwi.keys():
        kiwi[i] += 1
    else:
        kiwi[i] = 1

kangaroo_cnt = 0
kiwi_cnt = 0
for i in w:
    if i in kangaroo.keys():
        kangaroo_cnt += kangaroo[i]

    if i in kiwi.keys():
        kiwi_cnt += kiwi[i]

if kangaroo_cnt > kiwi_cnt:
    print("Kangaroos")
elif kangaroo_cnt < kiwi_cnt:
    print("Kiwis")
else:
    print("Feud continues")

