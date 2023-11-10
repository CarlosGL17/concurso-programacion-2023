data = [1000, '', ['', 0]]
while(data[2][0] != 'S'):
    data[1] = input()
    data[2] = data[1].split(' ')
    if(data[2][0] == 'C'):
        print(f'${data[0]}')
    if(data[2][0] == 'D'):
        data[0] += int(data[2][1])
    if(data[2][0] == 'R'):
        data[0] -= int(data[2][1])