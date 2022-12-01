input_list = [i for i in input().split(" ")]

m_list = []
for i in input_list:
    temp = ""
    for j in range(len(i)):
        temp += i[len(i)-j-1]
    m_list += [int(temp)]

print(max(m_list))