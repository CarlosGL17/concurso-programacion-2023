data = [1000, '']
while(not 'S' in data[1]):
    data[1] = input()
    data[1] = data[1].split(' ')
    if(data[1][0] == 'C'):
        print(f'${data[0]}')
    if(data[1][0] == 'D'):
        data[0] += int(data[1][1])
    if(data[1][0] == 'R'):
        data[0] -= int(data[1][1])