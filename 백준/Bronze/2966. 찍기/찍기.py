import sys

s = "ABC"
c = "BABC"
h = "CCAABB"

n = int(sys.stdin.readline())
input_list = sys.stdin.readline().rstrip()

s_cnt = 0
c_cnt = 0
h_cnt = 0
for k, i in enumerate(input_list):
    if i == s[k%3]:
        s_cnt += 1

    if i == c[k%4]:
        c_cnt += 1

    if i == h[k%6]:
        h_cnt += 1

cnt_list = [s_cnt, c_cnt, h_cnt]
max_cnt = max(s_cnt, c_cnt, h_cnt)
print(max_cnt)
for k, i in enumerate(cnt_list):
    if i == max_cnt:
        if k == 0:
            print("Adrian")
        elif k == 1:
            print("Bruno")
        elif k == 2:
            print("Goran")