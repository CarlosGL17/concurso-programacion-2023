string = input()
op = int(input())
for _ in range(op):
    data = input().split()
    if int(data[2]) < int(data[1]):
        data[1], data[2] = data[2], data[1]
    sub = string[int(data[1]):int(data[2])]
    if int(data[1]) < int(data[2]):
        data[2], data[1] = data[1], data[2]
    print(sub, len(sub), data)


# print(string[int(data[1]):int(data[2])].count(data[0]))