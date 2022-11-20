import sys

n = int(sys.stdin.readline())


temp = [[1 for i in range(0, 10)] for j in range(n)]
temp[0][0] = 0

if n != 1:
    for i in range(1, n):
        temp[i][0] = temp[i - 1][1]
        # 계단 수가 9로 끝나는 경우
        temp[i][9] = temp[i - 1][8]
        for j in range(1, 9):
            temp[i][j] = temp[i - 1][j - 1] + temp[i - 1][j + 1]
print(sum(temp[n-1]) % 1000000000)