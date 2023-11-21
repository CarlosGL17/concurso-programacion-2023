import math

data = list(map(int, input().split()))
print(data[0] < data[1], data[2] > data[1], data[0] == data[1], data[0] != data[2], data[2] <= data[1])