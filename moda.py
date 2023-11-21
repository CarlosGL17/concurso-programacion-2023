size = int(input())
data = input().split()
unique = list(dict.fromkeys(data))
count = []
interval = [0, 0]

for _ in range(len(unique)):
    count.append([data.count(unique[_]), unique[_]])
    unique[_] = abs(int(unique[_]))
unique = list(dict.fromkeys(unique))

for _ in range(size):
    data[_] = abs(int(data[_]))

for _ in range(len(unique)):
    interval = [data.count(unique[_]), unique[_]] if data.count(unique[_]) > interval[0] else interval

data = [0, 0]
for _ in range(len(count)):
    if int(count[_][1]) == interval[1]:
        data[0] = count[_][0]
    elif int(count[_][1]) == -interval[1]:
        data[1] = count[_][0]

print(interval[1])
print(data[0], data[1])