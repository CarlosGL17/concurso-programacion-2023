size, r = map(int, input().split())
data = list(map(int, input().split()))
interval = ['', []]
for i in range(r):
    interval[0] = input()
    interval[1] = interval[0].split(' ')
    if(interval[1][0] == 'C'):
        print(min(data[int(interval[1][1])-1:int(interval[1][2])]), max(data[int(interval[1][1])-1:int(interval[1][2])]))
    if(interval[1][0] == 'A'):
        data[int(interval[1][1])-1] = int(interval[1][2])