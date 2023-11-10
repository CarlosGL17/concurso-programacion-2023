size = int(input())
data = input().split()
unique = list(dict.fromkeys(data))
count = []
interval = [0, 0]

for _ in range(len(unique)):
    count.append([data.count(unique[_]), unique[_]])

for _ in range(size):
    data[_] = abs(int(data[_]))

for _ in range(len(unique)):
    unique[_] = abs(int(unique[_]))
unique = list(dict.fromkeys(unique))

for _ in range(len(unique)):
    # print(interval[1], unique[_], data.count(unique[_]))
    if interval[0] >= data.count(unique[_]):
        if interval[1] < unique[_]:
            interval = [data.count(interval[1]), interval[1]]
        else:
            interval = interval
    else:
        interval = [data.count(unique[_]), unique[_]]
data = [0, 0]
# print(count, interval, data) 

for _ in range(len(count)):
    # print(abs(int(count[_][1])) == interval[1], count[_][1])
    if int(count[_][1]) == interval[1]:
        data[0] = count[_][0]
    elif int(count[_][1]) == (-1 * interval[1]):
        data[1] = count[_][0]

print(interval[1])
print(data[0], data[1])