numeros = list(map(int, input().split()))
if(abs(numeros[2]-numeros[1]) == abs(numeros[2]-numeros[0])):
    print("raton C")
else: 
    if(numeros[2] / numeros[1] < numeros[2] / numeros[0]):
        print("gato B")
    else:
        print("gato A")