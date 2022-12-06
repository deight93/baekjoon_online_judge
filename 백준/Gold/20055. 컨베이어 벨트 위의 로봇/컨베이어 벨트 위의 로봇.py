import sys
from collections import deque


# 1. 벨트 회전
def belt_move(belt, ckeck_robot):
    belt.rotate(1)
    ckeck_robot.rotate(1)
    return belt, ckeck_robot


# 2. 로봇 이동
def robot_move(belt, ckeck_robot, n):
    for i in range(n, 0, -1):
        if i == n:
            ckeck_robot[i - 1] = False
        else:
            if ckeck_robot[i - 1] is True and belt[i] != 0 and ckeck_robot[i] is False:
                belt[i] -= 1
                ckeck_robot[i] = True
                ckeck_robot[i - 1] = False
    ckeck_robot[n - 1] = False

    return belt, ckeck_robot


# 3. 로봇 올림
def robot_append(belt, ckeck_robot):
    if belt[0] != 0:
        belt[0] -= 1
        ckeck_robot[0] = True
    return belt, ckeck_robot


n, k = map(int, sys.stdin.readline().rstrip().split(" "))
a2n = deque(list(map(int, sys.stdin.readline().rstrip().split(" "))))
ck_robot = deque([False for i in range(n)])

step = 0
while True:
    step += 1
    a2n, ck_robot = belt_move(a2n, ck_robot)
    a2n, ck_robot = robot_move(a2n, ck_robot, n)
    a2n, ck_robot = robot_append(a2n, ck_robot)

    # 4. 내구도 0인게 k개면 종료
    cnt = a2n.count(0)
    if cnt >= k:
        break
print(step)

