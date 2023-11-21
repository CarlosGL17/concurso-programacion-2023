strings = input().split(',')
for _ in range(len(strings)):
    print(strings[_][::-1], end='' if _ == len(strings) - 1 else ',')