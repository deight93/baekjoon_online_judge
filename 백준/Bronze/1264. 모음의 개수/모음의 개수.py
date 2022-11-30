import sys

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

while True:
    sentence = sys.stdin.readline().rstrip()
    if sentence == "#":
        break

    sentence = sentence.replace(" ", "")
    cnt = 0
    for i in sentence:
        if i in vowels:
            cnt += 1
    print(cnt)