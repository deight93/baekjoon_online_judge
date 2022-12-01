import sys

l = int(sys.stdin.readline().rstrip())
s = int(sys.stdin.readline().rstrip())
f = s-l

if f < 1:
    print("Congratulations, you are within the speed limit!")
elif 1 <= f < 21:
    print("You are speeding and your fine is $100.")
elif 21 <= f < 31:
    print("You are speeding and your fine is $270.")
else:
    print("You are speeding and your fine is $500.")

