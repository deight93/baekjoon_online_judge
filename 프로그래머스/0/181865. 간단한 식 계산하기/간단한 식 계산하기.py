def solution(binomial):
    answer = 0
    binomial = binomial.split()
    a = int(binomial[0])
    b = int(binomial[2])
    op = binomial[1]
    
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    else:
        return a * b
