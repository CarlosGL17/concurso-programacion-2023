size = list(map(int, input().split()))
init = list(map(int, input().split()))
end = list(map(int, input().split()))
map_ = [[None] * size[0] for _ in range(size[1]) ]

for _ in range(size[0]):
    # map_[_] = [_ if _  != '#' else None for _ in input()]
    map_[_] = [_ if _  != '.' else 1 for _ in input()]
print()
for _ in range(size[0]):
    for __ in range(size[1]):
        print(map_[_][__], end=' ')
    print()

# print(map_)