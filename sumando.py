from memory_profiler import memory_usage_psutil
size = int(input())
data = list(map(int, input().split()))
sum = [0, 0]

if min(data) < 0:
    if max(data) < 0:
        sum[1] = max(data)
    else:
        for _ in range(size, 0, -1):
            # print(data[0:_])
            for __ in range(_):
                sum[0] = 0
                # print(data[__:_], end=' ')
                for ___ in data[__:_]:
                    sum[0] += ___
                sum[1] = sum[0] if sum[0] > sum[1] else sum[1]
                # print(sum[0], sum[1])
else:
    for _ in data:
        sum[1] += _
print(sum[1])
print(memory_usage_psutil())