size = int(input())
data = input().split()
unique = list(dict.fromkeys(data))
count = []
interval = [[0, 0], 0]

for _ in range(len(unique)):
    # print(data.count(unique[_]), unique[_])
    count.append([data.count(unique[_]), unique[_]])

for _ in range(size):
    data[_] = abs(int(data[_]))

for _ in range(len(unique)):
    unique[_] = abs(int(unique[_]))
unique = list(dict.fromkeys(unique))

interval[0][1] = unique[0]
for _ in range(len(unique)):
    print(data.count(unique[_]), unique[_])
    interval[0] = interval[0] if interval[0][1] < unique[_] else [data.count(unique[_]), unique[_]]
    # print(data.count(unique[_]), unique[_])

print(count, interval)

#print(max(count))

# data.sort()
# print(data)
# count = []

# for _ in range(size):
    # print(data.count(data[_]), data[_])

# print(count[0])